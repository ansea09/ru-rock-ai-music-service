# 12 — Implementation plan

## Phase 0 — Repository setup

- Create project skeleton.
- Add AGENTS.md and docs.
- Add README.
- Select the target acceptance profile from `docs/delivery/16_acceptance_profiles.md`.
- Choose Python/FastAPI or equivalent stack.
- Add basic tests and lint/type config if desired.

Exit criteria:

- Service starts.
- Health endpoint works.
- Tests run.
- Target profile is documented.

## Phase 1 — API skeleton

- Implement request/response schemas.
- Implement `POST /v1/tracks` with job creation.
- Implement job status store.
- Implement artifact path conventions.
- Implement `GET /health` and `GET /v1/models`.
- Include `target_audio_mode` and output-mode metadata in schemas.

Exit criteria:

- API contract works with mock backend.
- OpenAPI is generated.

## Phase 2 — Mock backend

- Implement deterministic mock lyrics generator.
- Implement deterministic mock audio artifact writer.
- Save metadata.
- Add tests.

Exit criteria:

- Full job lifecycle works without GPU.
- Tests do not require model weights.
- Only Profile A is claimed unless a real local backend is also integrated.

## Phase 3 — Real local model backend spike

- Select first real backend.
- Implement model loading.
- Implement generation adapter.
- Add device selection.
- Store warnings and limitations.

Exit criteria:

- One local generation succeeds on target hardware.
- Metadata captures model/version/device/seed/settings.
- Profile B evidence exists or the remaining blocker is explicit.

## Phase 4 — Lyrics and prompt pipeline

- Improve lyrics generation or integrate a selected local/text model.
- Add structure planner.
- Add prompt builder per backend.
- Add validation for provided lyrics.

Exit criteria:

- Generated lyrics are returned and saved.
- Conditioning prompt is saved or included in metadata.
- Actual output mode is set correctly; lyrics are not claimed as sung unless verified.

## Phase 5 — Benchmark harness

- Add benchmark prompt set.
- Add scoring sheet/report template.
- Add command to run local generations for benchmark cases.
- Add report output directory.

Exit criteria:

- Benchmark report can be produced.
- Verdict class is explicit.
- Evaluator mode and unsupported claims are documented.

## Phase 6 — GPU worker / queue

- Add queue backend.
- Add worker process.
- Move generation from API thread to worker.
- Add worker logs.

Exit criteria:

- API creates job; worker completes job asynchronously.

## Phase 7 — GPU execution / GPU farm adapter

- Add Kubernetes/Slurm/Ray/static adapter.
- Add worker container.
- Add artifact storage outside worker.
- Add scheduler metadata.

Exit criteria:

- One job runs through selected scheduler path or well-documented local simulation.
- The report distinguishes static GPU execution from a real GPU farm.

## Phase 8 — hardening

- Add cancellation if needed.
- Add cleanup policy.
- Add artifact expiry.
- Add structured errors.
- Add basic observability.

Exit criteria:

- Prototype is reviewable and limitations are documented.
