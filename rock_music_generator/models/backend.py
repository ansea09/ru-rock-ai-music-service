from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

from rock_music_generator.api.schemas import AudioMode, TrackMetadata


@dataclass(frozen=True)
class GenerationResult:
    lyrics_path: Path
    audio_path: Path
    metadata: TrackMetadata
    actual_audio_mode: AudioMode


class MusicBackend(ABC):
    model_id: str

    @abstractmethod
    def generate_for_job(self, job_id: str, request, store) -> None:
        """Generate artifacts for a job and update the job store."""
