from enum import StrEnum

from pydantic import BaseModel, Field


class LyricsMode(StrEnum):
    generate = "generate"
    provided = "provided"


class AudioMode(StrEnum):
    instrumental_with_lyrics_file = "instrumental_with_lyrics_file"
    lyrics_conditioned = "lyrics_conditioned"
    sung_lyrics_unverified = "sung_lyrics_unverified"
    sung_lyrics_aligned = "sung_lyrics_aligned"


class JobStatus(StrEnum):
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"
    expired = "expired"


class TrackCreateRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=4000)
    genre: str = "rock"
    language: str = "ru"
    lyrics_mode: LyricsMode = LyricsMode.generate
    lyrics: str | None = None
    duration_sec: int = Field(default=30, ge=1, le=600)
    quality_preset: str = "balanced"
    seed: int | None = None
    model_id: str = "mock"
    target_audio_mode: AudioMode = AudioMode.instrumental_with_lyrics_file


class TrackCreateResponse(BaseModel):
    job_id: str
    status: JobStatus


class ErrorPayload(BaseModel):
    code: str
    message: str
    recoverable: bool = False


class TrackMetadata(BaseModel):
    job_id: str
    model_id: str
    model_version: str
    runtime: str
    device: str
    duration_sec_target: int
    duration_sec_actual: float
    language: str
    genre: str
    seed: int | None
    generation_time_sec: float
    target_audio_mode: AudioMode
    actual_audio_mode: AudioMode
    lyrics_used_for_conditioning: bool
    lyrics_aligned_to_vocals: bool
    instrumental_only: bool
    warnings: list[str] = []


class TrackStatusResponse(BaseModel):
    job_id: str
    status: JobStatus
    lyrics_url: str | None = None
    audio_url: str | None = None
    metadata: TrackMetadata | None = None
    error: ErrorPayload | None = None


class LyricsResponse(BaseModel):
    job_id: str
    language: str
    structure: list[str]
    lyrics: str


class ModelCapabilities(BaseModel):
    text_to_music: bool
    lyrics_alignment: bool
    vocals: bool
    max_duration_sec: int
    supported_audio_modes: list[AudioMode]


class ModelInfo(BaseModel):
    model_id: str
    display_name: str
    capabilities: ModelCapabilities
    license_note: str


class ModelsResponse(BaseModel):
    models: list[ModelInfo]
