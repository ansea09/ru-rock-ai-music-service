# AGENTS.md — Instructions for Codex

Scope: this file governs the whole repository tree.

## Mission

Implement or extend a prototype REST service for local AI music generation based on
the requirements in `docs/`.
The target system accepts a Russian-language text prompt and produces:

1. Russian song lyrics.
2. A rock-style audio track.
3. Generation metadata.
4. A benchmark/evaluation report comparing the result against a declared reference baseline.

External commercial music-generation SaaS systems may be used only as manually
captured reference baselines, not as the production generation backend.

## Required operating discipline

Before implementing, read these files in order:

1. `docs/README.md`
2. `docs/task/00_bounded_context.md`
3. `docs/task/01_formal_task.md`
4. `docs/task/02_terms_local_model_and_gpu_farm.md`
5. `docs/architecture/04_architecture.md`
6. `docs/architecture/05_api_contract.md`
7. `docs/research/10_evaluation_benchmark.md`
8. `docs/delivery/11_acceptance_criteria.md`
9. `docs/delivery/14_codex_work_items.md`
10. `docs/delivery/16_acceptance_profiles.md`

When the task touches model choice, read `docs/research/06_model_selection.md` and
`docs/research/08_finetuning_and_configuration.md`.
When the task touches distributed GPU execution, read
`docs/architecture/09_gpu_farm_integration.md`.
When the task touches rationale or terminology, read `docs/task/15_fpf_trace.md`.

## Engineering rules

- Keep the model, model runtime, API service, job queue, worker, storage,
  benchmark report, and generated artifacts separate.
- Do not claim that the system is “not worse than Suno” without running the
  benchmark protocol described in `docs/research/10_evaluation_benchmark.md`.
- Treat fine-tuning as optional unless a licensed dataset, training plan, and
  evaluation protocol exist.
- Prefer prompt/config tuning for the first prototype unless the issue explicitly
  asks for training work.
- Pin model names, model versions, seeds, generation parameters, and environment
  metadata wherever possible.
- Every generation job must produce an auditable metadata record.
- If a requirement is ambiguous, implement the smallest safe version and write the
  limitation in the relevant report or TODO.
- Do not silently call external music-generation APIs from the core generation pipeline.
- Do not count a mock backend as satisfying the real local model requirement.
  Mock backends satisfy only API/mock acceptance.
- Always distinguish generated lyrics, lyrics-conditioned audio, unverified sung
  lyrics, and verified lyric alignment.
- Treat project/model marketing claims as candidate claims until verified by local
  spike or benchmark evidence.
- Follow `docs/engineering/naming_conventions.md` before adding new top-level files,
  directories, modules, job statuses, artifact names, or benchmark verdict names.

## Suggested repository layout

If implementing from scratch, use this layout unless there is an existing repository structure:

```text
.
├── AGENTS.md
├── README.md
├── docs/
├── rock_music_generator/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── workers/
│   └── storage/
├── tests/
├── scripts/
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

## Testing expectations

For code changes, run the most specific available checks. Preferred order:

1. Unit tests for the changed module.
2. API contract tests.
3. Static checks / type checks / linting if configured.
4. A smoke test that creates a generation job using a mock or lightweight backend.

A full audio-generation test may be skipped in CI if it requires GPU or large
weights, but provide a mock backend and document the real GPU smoke test command.

## Output discipline

When you finish a task, report:

- Files changed.
- What works now.
- What remains unimplemented or unverified.
- Tests run and their result.
- Any model/license/GPU assumptions you had to make.
- Which acceptance profile was targeted and which profile, if any, was actually satisfied.
