# 14 — Codex work items

This file decomposes the project into small tasks suitable for Codex.

Before starting any work item, state the target acceptance profile from `docs/delivery/16_acceptance_profiles.md`.

## Work item 1 — Create API skeleton

Task:

> Implement a FastAPI service with endpoints described in `docs/architecture/05_api_contract.md`. Use an in-memory job store and return mock responses. Add tests for request validation and job status retrieval.

Acceptance:

- Endpoints exist.
- OpenAPI is generated.
- Tests pass without GPU.
- Profile A is the only profile claimed at this stage.

## Work item 2 — Add job store and artifact layout

Task:

> Add a filesystem-backed artifact store following `docs/architecture/07_generation_pipeline.md`. Each job should have `request.json`, `lyrics.json`, `metadata.json`, and an audio placeholder for mock backend.

Acceptance:

- Artifacts are written per job.
- API can return lyrics and audio placeholder.
- Missing artifact errors are structured.
- Metadata includes `target_audio_mode` and `actual_audio_mode`.

## Work item 3 — Implement mock backend

Task:

> Implement a deterministic mock generation backend that produces Russian placeholder lyrics and a short valid WAV file. It must follow the same interface intended for real local models.

Acceptance:

- Mock backend creates valid artifacts.
- Tests can run in CI without model weights.
- Documentation states that mock output is not real local AI music generation.

## Work item 4 — Add model backend interface

Task:

> Create a pluggable model backend interface and registry. Add `GET /v1/models` based on registered backends.

Acceptance:

- Backend interface exists.
- Mock backend is registered.
- Model list endpoint exposes capabilities.
- Backend capabilities include supported output modes.

## Work item 5 — Add real local backend spike

Task:

> Add a first real local model backend behind a feature flag. Keep it optional and do not make tests depend on large model downloads. Document installation and runtime assumptions.

Acceptance:

- Backend can be configured.
- If model is unavailable, service still runs with mock backend.
- Documentation states limitations.
- Successful local generation moves evidence toward Profile B.
- If only project/model documentation exists, record it as unverified candidate evidence.

## Work item 6 — Add lyrics generator module

Task:

> Implement a lyrics generation module that produces structured Russian lyrics for rock songs. Start with a deterministic template or local text model adapter. Store structure metadata.

Acceptance:

- `lyrics_mode=generate` works.
- `lyrics_mode=provided` works.
- Lyrics are saved and returned.
- The implementation does not claim lyrics are sung unless `actual_audio_mode=sung_lyrics_aligned` is supported by evaluation evidence.

## Work item 7 — Add benchmark harness

Task:

> Create a `benchmark/` directory with prompt cases and a script that runs the local service or backend for each case, saving outputs and a report template.

Acceptance:

- Benchmark cases exist.
- Local outputs can be generated with mock backend.
- Report template is produced.
- Report template includes evaluator mode, unsupported claims, and per-characteristic verdicts.

## Work item 8 — Add queue and worker

Task:

> Move generation execution out of the request path into a background worker. Use a simple local queue first.

Acceptance:

- Job status transitions from `queued` to `running` to `completed` or `failed`.
- API remains responsive.

## Work item 9 — Add GPU scheduler adapter abstraction

Task:

> Add an abstraction for GPU execution adapters: static worker, Kubernetes, Slurm, or Ray. Implement only static worker or a dry-run adapter unless infrastructure is available.

Acceptance:

- Adapter interface exists.
- Worker metadata includes adapter information.
- No false claim of real GPU farm if only dry-run is implemented.
- Static worker, dry-run adapter, and real GPU farm are reported as different profiles.

## Work item 10 — Add README and runbook

Task:

> Write developer README sections for setup, running API, running tests, using mock backend, using real backend, artifact paths, and benchmark procedure.

Acceptance:

- New developer can run the service locally.
- Limitations are documented.
- README states target profile, actual profile, and unsupported claims.
