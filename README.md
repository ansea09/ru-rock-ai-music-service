# Rock Music Generator

Prototype REST service for local Russian rock-song generation.

The repository currently targets **Profile A — API/mock prototype** from
`docs/delivery/16_acceptance_profiles.md`: the API, job lifecycle, artifact layout, OpenAPI schema,
and tests work with a deterministic mock backend. This does not prove real local AI music
generation, vocal generation, lyric alignment, Suno parity, or GPU execution.

No public license is granted yet. See `LICENSE_PENDING.md`.

## What This Repo Contains

```text
.
├── rock_music_generator/        # FastAPI application package
│   ├── api/                     # API routes and schemas
│   ├── core/                    # Configuration
│   ├── models/                  # Backend interface and mock backend
│   ├── storage/                 # Artifact storage
│   └── workers/                 # In-memory job store
├── benchmark/                   # Benchmark workspace
├── docs/                        # Task, architecture, research, delivery, API
├── scripts/                     # Local smoke-test helpers
├── tests/                       # API tests
├── .github/                     # CI and issue templates
├── AGENTS.md                    # Codex/coding-agent instructions
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install ".[dev]"
uvicorn rock_music_generator.main:app --reload
```

Equivalent project commands:

```bash
make install
make run
make test
make lint
make smoke
make openapi
```

Open:

- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

Run tests:

```bash
pytest
```

Run a mock smoke test:

```bash
python scripts/run_mock_smoke.py
```

Docker:

```bash
docker compose up --build
```

## API Surface

Implemented scaffold endpoints:

- `POST /v1/tracks`
- `GET /v1/tracks/{job_id}`
- `GET /v1/tracks/{job_id}/lyrics`
- `GET /v1/tracks/{job_id}/audio`
- `GET /v1/models`
- `GET /health`

The mock backend writes artifacts under `artifacts/{job_id}/`:

- `request.json`
- `lyrics.json`
- `audio.wav`
- `metadata.json`

## Output Modes

The project distinguishes generated lyrics from sung lyrics:

- `instrumental_with_lyrics_file`: lyrics are returned, audio does not claim to sing them.
- `lyrics_conditioned`: lyrics or a structured summary condition the model,
  but alignment is not verified.
- `sung_lyrics_unverified`: vocals are present, but alignment is not verified.
- `sung_lyrics_aligned`: evaluation supports that the audio sings or aligns to the returned lyrics.

The mock backend supports only `instrumental_with_lyrics_file`.

## Acceptance Boundary

Do not claim any of the following from the current scaffold:

- Real local model inference.
- Verified sung Russian lyrics.
- Fine-tuning.
- Suno parity.
- GPU execution or GPU farm integration.

Use `docs/delivery/16_acceptance_profiles.md` to select the target profile before
implementation work.

## Documentation Map

Start with `docs/README.md`.

Key files:

- `AGENTS.md` — instructions for Codex and other coding agents.
- `docs/delivery/16_acceptance_profiles.md` — selectable acceptance profiles.
- `docs/architecture/05_api_contract.md` — REST API contract.
- `docs/api/openapi.json` — exported OpenAPI schema for machines and diffs.
- `docs/engineering/naming_conventions.md` — naming convention and semio checks.
