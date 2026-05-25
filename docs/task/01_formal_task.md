# 01 — Formal task statement

## Title

Prototype REST service for local Russian rock-song generation with optional GPU farm execution.

## Goal

Develop a prototype service that accepts a Russian-language user prompt and produces a rock-style song artifact using a locally controlled AI model or model pipeline.

The service must return:

1. Generated Russian lyrics.
2. Generated audio file.
3. Generation metadata.
4. Status and error information.
5. A documented quality evaluation procedure.

## Target output modes

The assignment must not collapse “lyrics exist” and “lyrics are sung” into one requirement.

The implementation must declare one or more supported output modes:

| Mode | Meaning | Acceptance implication |
|---|---|---|
| `instrumental_with_lyrics_file` | The service returns generated Russian lyrics and an instrumental or weak-vocal audio artifact. | Acceptable only if the target profile allows instrumental output. |
| `lyrics_conditioned` | The lyrics or a derived song brief are passed to the audio backend as conditioning. | Must record that exact sung alignment is not guaranteed. |
| `sung_lyrics_unverified` | The generated audio contains vocals, but exact alignment to the returned lyrics has not been verified. | Must not be described as verified lyric singing. |
| `sung_lyrics_aligned` | The generated audio is evaluated as singing the returned Russian lyrics within the declared protocol. | Requires a benchmark/evaluation check. |

If the customer expects a full song with sung Russian lyrics, `sung_lyrics_aligned` is the target mode. If the prototype cannot support it, the gap must be explicit.

## Mandatory deliverables

### 1. Model selection report

The implementer must compare at least three local model or pipeline candidates.
For each candidate, document:

- Model name and version.
- License and usage constraints.
- Local deployment feasibility.
- GPU/VRAM requirements if known.
- Supported audio duration.
- Whether it can produce vocals.
- Whether it can use or align lyrics.
- Russian-language suitability.
- Fine-tuning or adaptation support.
- Known risks.

### 2. Local generation pipeline

The prototype must include a pipeline that can:

1. Accept a user prompt.
2. Generate or accept Russian lyrics.
3. Build a music-generation prompt or conditioning payload.
4. Generate an audio artifact locally.
5. Store the generated artifacts.
6. Return artifacts through REST endpoints.

### 3. REST API

The service must provide:

- `POST /v1/tracks`
- `GET /v1/tracks/{job_id}`
- `GET /v1/tracks/{job_id}/lyrics`
- `GET /v1/tracks/{job_id}/audio`
- `GET /v1/models`
- `GET /health`

The API must have an OpenAPI/Swagger description.

### 4. Quality benchmark

The implementer must provide a benchmark report. The report must not simply say “not worse than Suno”. It must define:

- Test prompts.
- Reference baseline source and date.
- Generation settings.
- Scoring rubric.
- Evaluator protocol.
- Results.
- Gaps and next steps.

Parity claims are valid only inside the declared benchmark slice. Do not generalize from “partial parity on this prompt set” to “not worse than Suno” without scope.

### 5. Reproducible run instructions

The repository must include a README, dependency instructions, and a reproducible launch path such as Dockerfile, docker-compose, or scripts.

## Optional deliverables

### GPU farm integration

The implementer may add:

- Queue-based asynchronous generation.
- GPU worker process.
- Kubernetes/Slurm/Ray/Nomad/similar orchestration adapter.
- On-demand worker startup.
- Artifact storage integration.
- GPU usage metadata.
- Worker health and failure reporting.

### Fine-tuning / adaptation

The implementer may add fine-tuning or LoRA only if the following are specified:

- Dataset source.
- Dataset license.
- Training format.
- Training budget.
- Evaluation before/after.
- Rollback plan.

## Non-negotiable constraints

- Do not use external music-generation SaaS as the actual generator.
- Do not make commercial parity claims without benchmark evidence.
- Do not train on unlicensed music or lyrics.
- Do not hide model limitations.
- Do not conflate prompt tuning with fine-tuning.
- Do not count a mock backend as satisfying real local inference.
- Do not claim that returned lyrics are sung unless the output mode and evaluation evidence support that claim.
