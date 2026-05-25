from dataclasses import dataclass, field
from itertools import count
from threading import Lock

from rock_music_generator.api.schemas import (
    ErrorPayload,
    JobStatus,
    TrackCreateRequest,
    TrackMetadata,
)

_counter = count(1)


@dataclass
class JobRecord:
    job_id: str
    request: TrackCreateRequest
    status: JobStatus = JobStatus.queued
    metadata: TrackMetadata | None = None
    error: ErrorPayload | None = None
    events: list[str] = field(default_factory=list)


class JobStore:
    def __init__(self) -> None:
        self._jobs: dict[str, JobRecord] = {}
        self._lock = Lock()

    def create(self, request: TrackCreateRequest) -> JobRecord:
        job_id = f"trk_{next(_counter):06d}"
        job = JobRecord(job_id=job_id, request=request, events=["queued"])
        with self._lock:
            self._jobs[job_id] = job
        return job

    def get(self, job_id: str) -> JobRecord | None:
        with self._lock:
            return self._jobs.get(job_id)

    def mark_running(self, job_id: str) -> None:
        self._set_status(job_id, JobStatus.running)

    def mark_completed(self, job_id: str, metadata: TrackMetadata) -> None:
        with self._lock:
            job = self._jobs[job_id]
            job.status = JobStatus.completed
            job.metadata = metadata
            job.events.append("completed")

    def mark_failed(self, job_id: str, code: str, message: str) -> None:
        with self._lock:
            job = self._jobs[job_id]
            job.status = JobStatus.failed
            job.error = ErrorPayload(code=code, message=message, recoverable=False)
            job.events.append("failed")

    def _set_status(self, job_id: str, status: JobStatus) -> None:
        with self._lock:
            job = self._jobs[job_id]
            job.status = status
            job.events.append(status.value)
