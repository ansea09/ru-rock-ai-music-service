# 03 — Roles, systems, and work scope

## Active systems

The following systems perform work in the assignment context.

| System | Role in this context | Work performed |
|---|---|---|
| API service | Request intake and result publication | Receives jobs, validates input, returns status/artifacts. |
| Lyrics generator | Text-generation component | Produces Russian lyrics from prompt and structure constraints. |
| Music/audio generator | Audio-generation component | Produces rock-style audio from conditioning payload. |
| Worker process | Generation executor | Runs lyrics/audio generation, writes outputs and metadata. |
| Queue/scheduler | Work dispatcher | Moves jobs from API to workers. |
| GPU farm / GPU node | Compute provider | Provides GPU resources for generation/fine-tuning. |
| Artifact store | Result carrier system | Stores audio, lyrics, metadata, logs. |
| Benchmark evaluator | Evaluation system/person | Produces quality report and scores. |
| Acceptance profile | Requirement interpretation artifact | States which level of deliverable is being judged. |

## Non-active epistemic artifacts

These do not perform work. They describe, justify, or evidence work.

| Artifact | Purpose |
|---|---|
| Model selection report | Justifies model choice. |
| OpenAPI specification | Describes API contract. |
| Benchmark report | Evidence about quality claims. |
| README | Describes setup and operation. |
| Metadata record | Evidence carrier for a generation run. |
| Reference baseline capture | Baseline evidence for comparison. |

## Key role separation

Do not conflate these:

- A model file is not the running service.
- A model card is not generation evidence.
- A prompt template is not a generated song.
- A fine-tuning plan is not a fine-tuned model.
- A benchmark rubric is not benchmark evidence.
- A generated explanation is not proof of quality.
- A mock backend is not a local AI music model.
- A returned lyrics file is not evidence that the lyrics were sung.
- A model project page is not independent benchmark evidence.

## WorkScope for MVP

Minimum work scope:

- Language: Russian.
- Genre: rock.
- Output: lyrics + audio artifact.
- Interface: REST API.
- Execution: local or controlled infrastructure.
- Quality claim: benchmarked, not assumed.
- Output mode: explicitly declared, not inferred.

Out-of-scope for MVP unless explicitly added:

- Production-grade vocals.
- Commercial release readiness.
- Legal clearance for all generated outputs.
- Guaranteed parity with Suno.
- Multi-tenant SaaS operation.
- Real GPU farm claims unless multiple GPU resources are actually scheduled or managed.
