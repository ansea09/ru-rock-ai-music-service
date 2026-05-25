# Naming Conventions

Names in this repository should help humans, GitHub, search engines, and LLMs infer
the role of a file without overclaiming what the system can do.

## Semio Rule

A path is a sign carrier, not evidence that work happened. A filename may describe
the artifact type or intended role, but it must not imply an unverified capability.

Examples:

- Use `mock_backend.py` for a deterministic test backend.
- Do not name a module `suno_parity_backend.py` unless a benchmark supports that claim.
- Use `benchmark_report.md` for a report artifact; use verdict fields inside the
  report for `partial_parity` or `gap_documented`.
- Use `openapi.json` for the exported schema; do not call it `final_api.json`.

## Repository Names

- Python package: `rock_music_generator`.
- Import path: `rock_music_generator.<module>`.
- Distribution name: `rock-music-generator`.
- Top-level folders use nouns that name work-object roles: `docs`, `benchmark`,
  `scripts`, `tests`, `rock_music_generator`.

The package name is project-specific so stack traces, imports, and code search do not
collapse into a generic `app` result.

## Documentation Names

Documentation lives under role folders:

- `task/` for assignment boundary and terminology.
- `architecture/` for system shape and runtime design.
- `research/` for model, fine-tuning, benchmark, and risk material.
- `delivery/` for acceptance profiles, implementation phases, and work items.
- `engineering/` for repository conventions.
- `api/` for machine-readable API artifacts.

The numbered Markdown files keep the original task-dossier order. The folder names
state the current repository role of each document.

## Code Names

- Modules use `snake_case`.
- Classes use `PascalCase`.
- Functions and variables use `snake_case`.
- Mock or fake implementations must carry `mock_` or `Mock` in the name.
- Runtime statuses use plain state names: `queued`, `running`, `completed`, `failed`,
  `cancelled`, `expired`.
- Output modes use factual capability names:
  `instrumental_with_lyrics_file`, `lyrics_conditioned`, `sung_lyrics_unverified`,
  `sung_lyrics_aligned`.

Avoid generic names such as `service.py`, `manager.py`, or `utils.py` unless the file
has exactly that narrow role. Prefer names that identify the work object:
`artifact_store.py`, `job_store.py`, `mock_backend.py`.

## Claim Hygiene

Do not put these claims in file or directory names unless the corresponding evidence
exists in the repository:

- `production`
- `suno_parity`
- `aligned_lyrics`
- `fine_tuned`
- `gpu_farm`
- `real_model`

Use neutral names for plans and interfaces, then record evidence in metadata,
benchmark reports, model-selection notes, or acceptance profile records.
