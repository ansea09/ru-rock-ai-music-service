# 07 — Generation pipeline

## Pipeline overview

```text
User prompt
  ↓
Input validation
  ↓
Lyrics generation or lyrics validation
  ↓
Song structure planning
  ↓
Music conditioning prompt construction
  ↓
Local audio generation
  ↓
Post-processing
  ↓
Artifact storage
  ↓
Metadata and status update
```

## Step 1 — Input validation

Validate:

- Prompt is non-empty.
- Language is `ru` for the target assignment.
- Genre is `rock` for the target assignment.
- Duration is within backend capability.
- `lyrics_mode` is valid.
- User-provided lyrics are present if required.

## Step 2 — Lyrics generation

For `lyrics_mode=generate`, create Russian lyrics with an explicit song structure.

Recommended structure:

```text
[Куплет 1]
...

[Припев]
...

[Куплет 2]
...

[Припев]
...
```

Lyrics metadata should include:

- `language`
- `structure`
- `theme`
- `style_notes`
- `warnings`

## Step 3 — Conditioning prompt construction

Build a model-specific conditioning prompt.

Example:

```text
Russian rock song, energetic electric guitars, strong drums, emotional male vocal,
verse chorus structure, theme: leaving the city and starting a new life.
Lyrics: <lyrics here if backend supports lyrics conditioning>.
```

If the backend does not support lyrics alignment, record this limitation in metadata.

## Step 4 — Local audio generation

The backend must expose a stable interface, for example:

```python
class MusicBackend:
    def generate(self, request: GenerationRequest) -> GenerationResult:
        ...
```

The result should include:

- Audio path.
- Actual duration.
- Seed.
- Parameters.
- Backend metadata.
- Warnings.

## Step 5 — Post-processing

Minimum post-processing:

- Normalize peak/loudness conservatively.
- Convert to requested format if needed.
- Validate audio file exists and is readable.
- Measure actual duration.

Optional post-processing:

- Loudness normalization to target LUFS.
- Fade in/out.
- Silence trimming.
- MP3 encoding.

## Step 6 — Artifact storage

Store per job:

```text
artifacts/{job_id}/
├── request.json
├── lyrics.json
├── audio.wav
├── metadata.json
└── worker.log
```

## Step 7 — Metadata

Mandatory metadata fields:

```json
{
  "job_id": "...",
  "model_id": "...",
  "model_version": "...",
  "backend": "...",
  "device": "...",
  "seed": 12345,
  "duration_sec_target": 60,
  "duration_sec_actual": 58.7,
  "generation_time_sec": 184,
  "target_audio_mode": "lyrics_conditioned",
  "actual_audio_mode": "lyrics_conditioned",
  "lyrics_used_for_conditioning": true,
  "lyrics_aligned_to_vocals": false,
  "instrumental_only": false,
  "created_at": "...",
  "completed_at": "...",
  "warnings": []
}
```

## Required limitation handling

If the backend cannot sing the exact Russian lyrics, the service must not pretend it did. It should record one of:

- `lyrics_used_for_conditioning=true`
- `lyrics_aligned_to_vocals=true`
- `lyrics_generated_but_not_sung=true`
- `instrumental_only=true`

Use these output modes consistently:

| `actual_audio_mode` | Required meaning |
|---|---|
| `instrumental_with_lyrics_file` | Lyrics were generated or accepted and returned separately; audio is instrumental or lyrics are not used. |
| `lyrics_conditioned` | Lyrics, structure, or a summary were passed to the backend, but exact sung alignment is not claimed. |
| `sung_lyrics_unverified` | Vocals appear to exist, but no alignment check supports the returned text being sung. |
| `sung_lyrics_aligned` | Evaluation evidence supports that the returned lyrics are sung or aligned within the declared tolerance. |

Only `sung_lyrics_aligned` supports a claim that the service generated a song singing the returned Russian lyrics.
