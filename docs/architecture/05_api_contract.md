# 05 — REST API contract

## API style

The service uses asynchronous job creation.

A generation request creates a job and returns `job_id`. The client polls the job status and downloads artifacts after completion.

## Endpoints

### `POST /v1/tracks`

Create a track-generation job.

Request:

```json
{
  "prompt": "Песня о человеке, который уезжает из города и начинает новую жизнь",
  "genre": "rock",
  "language": "ru",
  "lyrics_mode": "generate",
  "lyrics": null,
  "duration_sec": 60,
  "quality_preset": "balanced",
  "seed": 12345,
  "model_id": "auto",
  "target_audio_mode": "lyrics_conditioned"
}
```

Response:

```json
{
  "job_id": "trk_20260525_001",
  "status": "queued"
}
```

Validation rules:

- `prompt` is required.
- `language` defaults to `ru` for this assignment.
- `genre` defaults to `rock` for this assignment.
- `lyrics_mode` is `generate` or `provided`.
- If `lyrics_mode=provided`, `lyrics` must be non-empty.
- `duration_sec` must be bounded by model capability.
- `seed` is optional but should be stored if present.
- `target_audio_mode` is one of `instrumental_with_lyrics_file`, `lyrics_conditioned`, `sung_lyrics_unverified`, or `sung_lyrics_aligned`.
- If `target_audio_mode=sung_lyrics_aligned`, the selected backend must expose that capability or the job must be rejected with a structured error.

### `GET /v1/tracks/{job_id}`

Return job status and metadata.

Response when completed:

```json
{
  "job_id": "trk_20260525_001",
  "status": "completed",
  "lyrics_url": "/v1/tracks/trk_20260525_001/lyrics",
  "audio_url": "/v1/tracks/trk_20260525_001/audio",
  "metadata": {
    "model_id": "selected-local-model",
    "model_version": "pinned-version",
    "runtime": "local-worker",
    "device": "cuda:0",
    "gpu_type": "unknown-or-detected",
    "duration_sec_target": 60,
    "duration_sec_actual": 58.7,
    "language": "ru",
    "genre": "rock",
    "seed": 12345,
    "generation_time_sec": 184,
    "target_audio_mode": "lyrics_conditioned",
    "actual_audio_mode": "lyrics_conditioned",
    "lyrics_used_for_conditioning": true,
    "lyrics_aligned_to_vocals": false,
    "instrumental_only": false,
    "created_at": "2026-05-25T12:00:00Z",
    "completed_at": "2026-05-25T12:03:04Z",
    "warnings": []
  }
}
```

Response when failed:

```json
{
  "job_id": "trk_20260525_001",
  "status": "failed",
  "error": {
    "code": "MODEL_RUNTIME_ERROR",
    "message": "Model failed during audio generation.",
    "recoverable": false
  }
}
```

### `GET /v1/tracks/{job_id}/lyrics`

Return generated or provided lyrics.

```json
{
  "job_id": "trk_20260525_001",
  "language": "ru",
  "structure": ["verse_1", "chorus", "verse_2", "chorus"],
  "lyrics": "..."
}
```

### `GET /v1/tracks/{job_id}/audio`

Return binary audio.

Preferred content types:

- `audio/wav`
- `audio/mpeg`

### `GET /v1/models`

Return available local model runtimes.

```json
{
  "models": [
    {
      "model_id": "musicgen-small-local",
      "display_name": "MusicGen small local",
      "capabilities": {
        "text_to_music": true,
        "lyrics_alignment": false,
        "vocals": false,
        "max_duration_sec": 30,
        "supported_audio_modes": ["instrumental_with_lyrics_file", "lyrics_conditioned"]
      },
      "license_note": "Check model weights license before commercial use."
    }
  ]
}
```

### `GET /health`

Return service status.

```json
{
  "status": "ok",
  "version": "0.1.0"
}
```

## OpenAPI sketch

This is a sketch, not a complete generated schema.

```yaml
openapi: 3.0.3
info:
  title: Local AI Music Generation API
  version: 0.1.0
paths:
  /v1/tracks:
    post:
      summary: Create a music generation job
      requestBody:
        required: true
      responses:
        '202':
          description: Job accepted
  /v1/tracks/{job_id}:
    get:
      summary: Get generation job status
  /v1/tracks/{job_id}/lyrics:
    get:
      summary: Get generated lyrics
  /v1/tracks/{job_id}/audio:
    get:
      summary: Get generated audio
  /v1/models:
    get:
      summary: List available local models
  /health:
    get:
      summary: Health check
```

## Minimum OpenAPI completeness requirements

The final repository should provide a real OpenAPI schema, not only the sketch above.

The schema must define:

- Request and response models for every endpoint.
- Enumerations for job status, `lyrics_mode`, `target_audio_mode`, and `actual_audio_mode`.
- Structured error responses with stable error codes.
- Validation bounds for `duration_sec`, `prompt`, `lyrics`, and `quality_preset`.
- Metadata schema, including model/version/device/seed/settings and output-mode fields.
- Binary response metadata for `GET /v1/tracks/{job_id}/audio`.

If the framework generates OpenAPI automatically, the generated schema must still expose these fields explicitly.
