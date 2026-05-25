# 00 — Bounded context

## Context name

`LocalAIMusicGenerationPrototype_2026`

## Problem boundary

This assignment concerns a prototype of a locally controlled AI music-generation service.
The service must accept a Russian-language prompt and generate:

- Russian lyrics.
- A rock-style musical audio artifact.
- Metadata about the generation run.
- A quality report against a declared baseline.

## In scope

- Local model or local model pipeline selection.
- Local inference setup.
- REST API design.
- Asynchronous job lifecycle.
- Russian lyrics generation.
- Rock-style audio generation.
- Artifact storage and retrieval.
- Metadata and reproducibility fields.
- Benchmark protocol against a reference baseline such as Suno.
- Optional GPU farm integration.
- Optional prompt/config tuning.
- Optional fine-tuning only if data, license, and evaluation conditions exist.
- Acceptance profile selection: API/mock, real local inference, lyrics/vocal target, benchmark, or GPU execution.

## Out of scope for the first prototype

- Guaranteed commercial parity with Suno.
- Unlicensed training on copyrighted music.
- Hidden calls to external music-generation SaaS systems.
- Full production observability stack unless requested.
- Billing, multi-tenant account management, RBAC, and abuse monitoring.
- Production legal clearance for generated music.
- Unbounded “all possible models” research.
- Treating mock generation as proof of real model capability.
- Treating generated lyrics as sung lyrics unless alignment is verified.

## Key ambiguity repairs

The source wording says: “рассматривай все варианты”. For a test assignment, this must be bounded as:

> Analyze model and architecture classes sufficient to justify the prototype path. Minimum: three local model/pipeline candidates and three architecture options.

The source wording says: “не хуже чем в Suno”. For an implementable assignment, this must be rewritten as:

> Evaluate against a fixed, dated reference baseline using a rubric and benchmark report. Do not claim parity unless the benchmark supports it.

The source wording says: “файнтюнинг / настройки”. These are different kinds of work:

- Fine-tuning changes model weights.
- Prompt/config tuning changes inference behavior without changing weights.
- Post-processing changes generated artifacts after inference.

They must not be treated as interchangeable.

The source wording says that the service must generate text as well as music. This must be split into explicit output modes:

- `instrumental_with_lyrics_file`: Russian lyrics are generated and returned, but the audio is instrumental.
- `lyrics_conditioned`: Russian lyrics or a lyrics summary are passed to the audio backend as conditioning, but exact sung alignment is not claimed.
- `sung_lyrics_unverified`: the backend appears to generate vocals, but exact alignment to returned lyrics has not been verified.
- `sung_lyrics_aligned`: the returned lyrics are verified as sung or aligned to the audio within the declared benchmark protocol.

The implementation must not silently upgrade one mode into another.
