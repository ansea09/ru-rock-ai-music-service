import json
from pathlib import Path

from rock_music_generator.api.schemas import LyricsResponse, TrackCreateRequest, TrackMetadata
from rock_music_generator.core.config import settings


class ArtifactStore:
    def __init__(self, root: Path | None = None) -> None:
        self.root = root or settings.artifact_root

    def job_dir(self, job_id: str) -> Path:
        path = self.root / job_id
        path.mkdir(parents=True, exist_ok=True)
        return path

    def audio_path(self, job_id: str) -> Path:
        return self.job_dir(job_id) / "audio.wav"

    def write_request(self, job_id: str, request: TrackCreateRequest) -> None:
        self._write_json(self.job_dir(job_id) / "request.json", request.model_dump(mode="json"))

    def write_lyrics(self, job_id: str, lyrics: LyricsResponse) -> None:
        self._write_json(self.job_dir(job_id) / "lyrics.json", lyrics.model_dump(mode="json"))

    def read_lyrics(self, job_id: str) -> LyricsResponse:
        data = json.loads((self.job_dir(job_id) / "lyrics.json").read_text(encoding="utf-8"))
        return LyricsResponse.model_validate(data)

    def write_metadata(self, job_id: str, metadata: TrackMetadata) -> None:
        self._write_json(self.job_dir(job_id) / "metadata.json", metadata.model_dump(mode="json"))

    def _write_json(self, path: Path, payload: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
