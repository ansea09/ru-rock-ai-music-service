# Contributing

This repository is currently a prototype scaffold. Contributions should state which
acceptance profile they target.

## Local Setup

```bash
make install
make run
```

## Checks

```bash
make lint
make test
make smoke
make openapi
```

If a change touches the API, regenerate `docs/api/openapi.json` and include it in the
same change.

## Contribution Boundaries

- Do not add external music-generation SaaS calls to the core generation pipeline.
- Do not claim Suno parity without the benchmark protocol in
  `docs/research/10_evaluation_benchmark.md`.
- Do not treat mock output as evidence of local model inference.
- Follow `docs/engineering/naming_conventions.md` for new files, modules, statuses,
  artifacts, and benchmark verdict names.
