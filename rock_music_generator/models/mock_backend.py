from __future__ import annotations

import math
import struct
import time
import wave
from pathlib import Path

from rock_music_generator.api.schemas import (
    AudioMode,
    LyricsResponse,
    TrackCreateRequest,
    TrackMetadata,
)
from rock_music_generator.models.backend import MusicBackend
from rock_music_generator.storage.artifact_store import ArtifactStore


class MockMusicBackend(MusicBackend):
    model_id = "mock"
    model_version = "0.1.0"

    def __init__(self, artifact_store: ArtifactStore) -> None:
        self.artifact_store = artifact_store

    def generate_for_job(self, job_id: str, request: TrackCreateRequest, store) -> None:
        started = time.perf_counter()
        store.mark_running(job_id)
        try:
            lyrics = self._lyrics(job_id, request)
            audio_path = self.artifact_store.audio_path(job_id)
            self._write_tone(audio_path)
            elapsed = time.perf_counter() - started
            metadata = TrackMetadata(
                job_id=job_id,
                model_id=self.model_id,
                model_version=self.model_version,
                runtime="mock-local-worker",
                device="cpu",
                duration_sec_target=request.duration_sec,
                duration_sec_actual=1.0,
                language=request.language,
                genre=request.genre,
                seed=request.seed,
                generation_time_sec=round(elapsed, 4),
                target_audio_mode=request.target_audio_mode,
                actual_audio_mode=AudioMode.instrumental_with_lyrics_file,
                lyrics_used_for_conditioning=False,
                lyrics_aligned_to_vocals=False,
                instrumental_only=True,
                warnings=["Mock backend: not real local AI music generation."],
            )
            self.artifact_store.write_request(job_id, request)
            self.artifact_store.write_lyrics(job_id, lyrics)
            self.artifact_store.write_metadata(job_id, metadata)
            store.mark_completed(job_id, metadata)
        except Exception as exc:  # pragma: no cover - defensive job failure path
            store.mark_failed(job_id, code="MOCK_BACKEND_ERROR", message=str(exc))

    def _lyrics(self, job_id: str, request: TrackCreateRequest) -> LyricsResponse:
        if request.lyrics_mode.value == "provided" and request.lyrics:
            text = request.lyrics
        else:
            text = (
                "[Куплет 1]\n"
                f"{request.prompt}\n"
                "Город гаснет, но гитары держат свет.\n\n"
                "[Припев]\n"
                "Мы идем сквозь шум и ветер,\n"
                "Рок звучит, и страха нет.\n\n"
                "[Куплет 2]\n"
                "Новый путь открыт за линией огней.\n\n"
                "[Припев]\n"
                "Мы идем сквозь шум и ветер,\n"
                "Рок звучит, и страха нет."
            )
        return LyricsResponse(
            job_id=job_id,
            language=request.language,
            structure=["verse_1", "chorus", "verse_2", "chorus"],
            lyrics=text,
        )

    def _write_tone(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        sample_rate = 44100
        duration_sec = 1
        amplitude = 8000
        frequency = 440
        with wave.open(str(path), "w") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(sample_rate)
            for i in range(sample_rate * duration_sec):
                value = int(amplitude * math.sin(2 * math.pi * frequency * i / sample_rate))
                wav.writeframes(struct.pack("<h", value))
