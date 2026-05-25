from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse

from rock_music_generator.api.schemas import (
    AudioMode,
    JobStatus,
    LyricsMode,
    LyricsResponse,
    ModelCapabilities,
    ModelInfo,
    ModelsResponse,
    TrackCreateRequest,
    TrackCreateResponse,
    TrackStatusResponse,
)
from rock_music_generator.models.mock_backend import MockMusicBackend
from rock_music_generator.storage.artifact_store import ArtifactStore
from rock_music_generator.workers.job_store import JobStore

router = APIRouter()
store = JobStore()
artifacts = ArtifactStore()
backend = MockMusicBackend(artifacts)


@router.post(
    "/v1/tracks",
    response_model=TrackCreateResponse,
    status_code=202,
    tags=["tracks"],
)
def create_track(
    request: TrackCreateRequest,
    background_tasks: BackgroundTasks,
) -> TrackCreateResponse:
    if request.lyrics_mode == LyricsMode.provided and not request.lyrics:
        raise HTTPException(status_code=422, detail="lyrics is required when lyrics_mode=provided")
    if request.target_audio_mode == AudioMode.sung_lyrics_aligned:
        raise HTTPException(
            status_code=422,
            detail="mock backend does not support verified sung lyric alignment",
        )

    job = store.create(request)
    background_tasks.add_task(backend.generate_for_job, job.job_id, request, store)
    return TrackCreateResponse(job_id=job.job_id, status=JobStatus.queued)


@router.get("/v1/tracks/{job_id}", response_model=TrackStatusResponse, tags=["tracks"])
def get_track(job_id: str) -> TrackStatusResponse:
    job = store.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")

    return TrackStatusResponse(
        job_id=job.job_id,
        status=job.status,
        lyrics_url=f"/v1/tracks/{job.job_id}/lyrics" if job.status == JobStatus.completed else None,
        audio_url=f"/v1/tracks/{job.job_id}/audio" if job.status == JobStatus.completed else None,
        metadata=job.metadata,
        error=job.error,
    )


@router.get("/v1/tracks/{job_id}/lyrics", response_model=LyricsResponse, tags=["tracks"])
def get_lyrics(job_id: str) -> LyricsResponse:
    job = store.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    if job.status != JobStatus.completed:
        raise HTTPException(status_code=409, detail="job is not completed")
    return artifacts.read_lyrics(job_id)


@router.get("/v1/tracks/{job_id}/audio", tags=["tracks"])
def get_audio(job_id: str) -> FileResponse:
    job = store.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    if job.status != JobStatus.completed:
        raise HTTPException(status_code=409, detail="job is not completed")
    path = artifacts.audio_path(job_id)
    if not path.exists():
        raise HTTPException(status_code=404, detail="audio artifact not found")
    return FileResponse(path, media_type="audio/wav", filename=f"{job_id}.wav")


@router.get("/v1/models", response_model=ModelsResponse, tags=["models"])
def list_models() -> ModelsResponse:
    return ModelsResponse(
        models=[
            ModelInfo(
                model_id="mock",
                display_name="Deterministic mock backend",
                capabilities=ModelCapabilities(
                    text_to_music=False,
                    lyrics_alignment=False,
                    vocals=False,
                    max_duration_sec=30,
                    supported_audio_modes=[AudioMode.instrumental_with_lyrics_file],
                ),
                license_note="Test-only backend; does not satisfy real local model acceptance.",
            )
        ]
    )
