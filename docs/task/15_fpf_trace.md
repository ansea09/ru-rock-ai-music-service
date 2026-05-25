# 15 — FPF trace and rationale

This file records how the technical assignment was structured using the FPF patterns that were available in the checked repository chunks.

## Source of FPF chunks

Repository:

- `ansea09/fpf-spec-mirror`

Main navigation files:

- `fpf_chunks/000-index.md`
- `fpf_chunks/metadata.jsonl` when available

The checked index identifies the specification source as `FPF-Spec.md`, chunking method `pattern-aware`, and 211 patterns.

## Patterns used

### A.1.1 — Bounded Context

Used to bound the assignment as `LocalAIMusicGenerationPrototype_2026`, not the entire AI music domain.

Project effect:

- Defined in-scope and out-of-scope work.
- Prevented “all variants” from becoming unbounded research.

### A.1 — Holonic Foundation

Used to separate systems, artifacts, models, and reports.

Project effect:

- API service, worker, model runtime, GPU farm, and artifact store are active systems.
- Model selection report, benchmark report, and OpenAPI specification are epistemic artifacts.
- Acceptance profile is an interpretation artifact, not proof that work happened.

### A.2 / A.2.1 — Role and role assignment

Used to separate actor identity from contextual responsibility.

Project effect:

- ML engineer, backend engineer, MLOps engineer, evaluator, worker, and GPU provider are roles in this context.
- Role assignment is not evidence that work happened.

### A.2.2 — Capability

Used to separate “can do” from “is assigned to do”.

Project effect:

- A model being selected does not prove it can generate Russian rock songs at the required quality.
- Capability claims require work scope and measures.
- A mock backend does not prove the capability of a local AI music model.

### A.2.4 — EvidenceRole

Used to treat benchmark reports and model cards as evidence artifacts, not as actors.

Project effect:

- Benchmark report can support a quality claim only within declared scope and time.

### A.3.1 — Method

Used to separate the way of doing generation from the code or run.

Project effect:

- Prompt tuning, fine-tuning, inference, post-processing, and benchmarking are different methods/work families.
- Generated lyrics, lyrics conditioning, vocal generation, and verified lyric alignment are different work/result claims.

### A.3.3 — Dynamics

Used to describe state changes:

- model unselected → selected → deployed → tuned → evaluated;
- service absent → API skeleton → worker-backed service → GPU-backed service;
- quality claim unsupported → benchmarked.

### A.4 — Temporal Duality

Used to separate design-time artifacts from run-time jobs.

Project effect:

- OpenAPI, prompts, model selection, and benchmark rubric are design-time artifacts.
- Generation jobs and benchmark runs are run-time work.

### A.2.6 — Unified Scope Mechanism

Used to define work scope:

- Russian language.
- Rock genre.
- Local execution.
- REST interface.
- Optional GPU farm integration.

### A.6 / A.6.B / A.6.P

Used to repair boundary and relation ambiguity.

Project effect:

- “REST service with input/output” became endpoint contract.
- “GPU farm integration” became queue + scheduler + worker + artifact flow.
- “Not worse than Suno” became a benchmark claim with evidence requirements.

### A.7 — Strict Distinction

Used to prevent category errors.

Project effect:

- Model ≠ runtime.
- Prompt ≠ generated track.
- MethodDescription ≠ Work.
- Benchmark rubric ≠ benchmark evidence.
- Explanation ≠ proof.

### A.10 — Evidence Graph

Used to require claim/evidence chains.

Project effect:

- Quality claims need benchmark artifacts, metadata, reference baseline, and scoring notes.

### A.11 — Ontological Parsimony

Used to avoid unnecessary new concepts.

Project effect:

- “Local model” and “GPU farm” are defined with existing engineering concepts rather than invented as new ontology nodes.

### A.15 / A.15.1 — Role–Method–Work Alignment and Work

Used to separate role, method, plan, and actual work.

Project effect:

- Test assignment decomposed into deliverables and implementation work items.
- Codex tasks are scoped as actual work units.

### A.17 / A.18 / C.16 / G.3

Used for measurement discipline.

Project effect:

- Quality criteria are expressed as characteristics with scales and polarity.
- “Not worse than Suno” is replaced with prompt adherence, genre adherence, lyrics quality, vocal intelligibility, artifact severity, latency, and failure rate.
- The benchmark keeps evaluator mode and scoring policy explicit, avoiding false precision from ordinal aggregation.

### C.27

Used for temporal claims.

Project effect:

- “On-demand” GPU startup must state cold/warm behavior and measured windows.
- Generation latency and throughput are not left as vague promises.
- Static GPU execution and managed GPU farm behavior are not treated as the same temporal or infrastructure claim.

### C.28

Used to avoid unsupported causal claims.

Project effect:

- Fine-tuning is not assumed to improve quality unless before/after evidence supports it.

### E.17.0 / E.17.1 / E.17.EFP

Used to organize viewpoints and explanation faithfulness.

Project effect:

- ML, backend, MLOps, evaluation, product, and legal/licensing viewpoints are separated.
- Explanatory notes are not treated as evidence or acceptance proof.
- Acceptance profiles separate API/mock, real local inference, lyrics/vocal alignment, benchmark, GPU execution, and GPU farm viewpoints.

## Pattern not strictly used

`C.7 CHR-CAL – Characterisation Kit` was requested in the protocol, but a direct `C.7` chunk was not found in the checked index/search context. This package therefore uses the available measurement-related patterns `A.17`, `A.18`, `C.16`, and `G.3` for characterization work. If an exact `C.7` file/path is later provided, this trace should be updated.

## External references used for domain grounding

These are not implementation commitments. They are candidate-source references for model and infrastructure analysis.

- AudioCraft / MusicGen repository: https://github.com/facebookresearch/audiocraft
- Stable Audio Open model card: https://huggingface.co/stabilityai/stable-audio-open-1.0
- ACE-Step project: https://ace-step.github.io/
- ACE-Step 1.5 project: https://ace-step.github.io/ace-step-v1.5.github.io/
- ACE-Step 1.5 repository: https://github.com/ace-step/ACE-Step-1.5
- NVIDIA GPU Operator documentation: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html
- OpenAI Codex introduction and AGENTS.md behavior: https://openai.com/index/introducing-codex/

Model and infrastructure claims should be rechecked against these sources on the implementation date. Project pages are source carriers for project claims; they are not independent benchmark evidence.

## Consistency check

The package avoids the following overclaims:

- It does not state that local open models equal Suno.
- It does not state that fine-tuning will improve quality.
- It does not treat model documentation as benchmark evidence.
- It does not treat GPU hardware alone as a GPU farm.
- It does not treat a REST endpoint as proof that generation works.
- It does not treat mock output as proof of real local AI generation.
- It does not treat generated lyrics as proof that lyrics were sung.
