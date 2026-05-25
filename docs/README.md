# Documentation Entry Point

This folder separates the project documents by the role they play. Use this file
instead of scanning every Markdown file in order.

## Fast Routes

For a quick project overview:

1. `../README.md`
2. `delivery/16_acceptance_profiles.md`
3. `architecture/05_api_contract.md`
4. `engineering/naming_conventions.md`

For implementation work:

1. `task/00_bounded_context.md`
2. `architecture/04_architecture.md`
3. `architecture/05_api_contract.md`
4. `architecture/07_generation_pipeline.md`
5. `delivery/11_acceptance_criteria.md`
6. `delivery/14_codex_work_items.md`

For model research:

1. `research/06_model_selection.md`
2. `research/08_finetuning_and_configuration.md`
3. `research/10_evaluation_benchmark.md`
4. `research/13_risks_and_unknowns.md`

For GPU execution and orchestration:

1. `architecture/09_gpu_farm_integration.md`
2. `delivery/16_acceptance_profiles.md`
3. `research/13_risks_and_unknowns.md`

## Folder Roles

- `task/` contains the formalized assignment and terminology.
- `architecture/` contains system structure, API, pipeline, and GPU execution design.
- `research/` contains model selection, fine-tuning, benchmark, and risk notes.
- `delivery/` contains acceptance profiles, work items, and implementation planning.
- `engineering/` contains repository conventions and coding-agent guidance.
- `api/` contains machine-readable API artifacts such as exported OpenAPI JSON.

## Source Of Truth

Runtime API behavior is implemented in `../rock_music_generator/`. The Markdown API
contract explains intent; `api/openapi.json` is the generated machine-readable schema.
When these disagree, inspect the FastAPI code first and regenerate `api/openapi.json`.
