# 04 — Architecture

## Recommended MVP architecture

```text
Client
  |
  | POST /v1/tracks
  v
API Service
  |
  | create job
  v
Job Store / Queue
  |
  | dispatch
  v
Generation Worker
  |-- Lyrics Generator
  |-- Prompt/Conditioning Builder
  |-- Local Music/Audio Model Runtime
  |-- Post-processing
  v
Artifact Store
  |-- lyrics.json
  |-- audio.wav or audio.mp3
  |-- metadata.json
  |-- logs.txt
  v
API Service
  |
  | GET status / lyrics / audio
  v
Client
```

## Components

### API service

Responsibilities:

- Validate requests.
- Create generation jobs.
- Return job status.
- Return artifacts.
- Expose model list.
- Expose health checks.

Non-responsibilities:

- It should not directly perform long-running GPU generation inside the request thread.
- It should not hide worker failures.
- It should not silently call external music-generation SaaS systems.

### Job store / queue

Responsibilities:

- Persist job status.
- Carry job payloads to workers.
- Support retry/error states.
- Maintain timestamps.

MVP options:

- In-memory queue for local demo.
- SQLite + background worker.
- Redis/RQ/Celery for a more realistic prototype.

### Generation worker

Responsibilities:

- Load or connect to model runtime.
- Generate lyrics if `lyrics_mode=generate`.
- Validate or normalize provided lyrics if `lyrics_mode=provided`.
- Generate audio.
- Save artifacts.
- Save metadata.
- Report errors.

### Model runtime

Responsibilities:

- Own model loading, inference parameters, seed handling, and device selection.
- Expose a stable interface to the worker.

### Artifact store

MVP options:

- Local filesystem.
- Mounted volume.
- S3-compatible object storage.

Required artifacts:

- `lyrics.json`
- `audio.wav` or `audio.mp3`
- `metadata.json`
- optional `prompt.txt`
- optional `worker.log`

The metadata must state the actual output mode. Returning `lyrics.json` and `audio.wav` is not enough to imply that the audio sings those lyrics.

## Optional GPU execution / GPU farm architecture

```text
API Service
  v
Queue
  v
Scheduler Adapter
  |-- Kubernetes Job adapter
  |-- Slurm adapter
  |-- Ray adapter
  |-- Static worker adapter
  v
GPU Worker Pod/Job/Actor
  v
Artifact Store
```

## Design decisions to pin

- Synchronous vs asynchronous API: choose asynchronous for any real generation.
- Artifact format: WAV for lossless prototype; MP3 optional.
- Storage: filesystem for local demo; object storage for cluster execution.
- Worker warmness: cold start, warm pool, or always-on worker.
- Model cache: local cache path and cache invalidation policy.
- Failure states: `queued`, `running`, `completed`, `failed`, `cancelled`, `expired`.
- Acceptance profile: API/mock, real local inference, lyrics/vocal target, benchmark, or GPU execution.
- Output mode: instrumental with lyrics file, lyrics-conditioned, unverified sung lyrics, or verified aligned sung lyrics.
- Evidence boundary: model card, local smoke test, benchmark report, and production claim are different artifacts.
