# Session Handoff

## Purpose

This file transfers the working context from the previous Codex chat into the
repository. It is a context carrier for the next Codex thread, not an acceptance
record and not evidence that implementation work beyond the committed files has
happened.

## First instruction for the next Codex chat

```text
Прочитай docs/engineering/session_handoff.md и продолжай оттуда.
Используй fpf-latest.
```

## Current workspace

Use this workspace path:

```text
/Users/macbook/Desktop/Codex/workspaces/ru-rock-ai-music-service
```

Do not use the old workspace path:

```text
/Users/macbook/Documents/Rock Music Generator
```

The old workspace was removed from `Documents` and moved to the macOS Trash after
the project was moved to the current workspace location.

## Repository state

- GitHub repository: `https://github.com/ansea09/ru-rock-ai-music-service`
- GitHub visibility: public
- Branch: `main`
- Last confirmed commit before this handoff: `6fbba90 Document architecture maturity levels`
- Last confirmed local state before this handoff: `git status` clean
- Active local workspace: `/Users/macbook/Desktop/Codex/workspaces/ru-rock-ai-music-service`

## FPF operating rule

Use the installed FPF skill:

```text
/Users/macbook/.codex/skills/fpf-latest/SKILL.md
```

For substantive reasoning, architecture, research, workspace operations, GitHub
operations, causal-use questions, source-backed answers, and documentation work:

- run the FPF context refresh gate first;
- use the current FPF Codex protocol routing;
- use the complex protocol when the task touches architecture, external
  publication, GitHub mutation, workspace state, causal-use claims, or
  multi-view evaluation;
- disclose cached/fresh FPF status in substantive final answers.

## Conversation boundaries to preserve

The user explicitly asked to ignore a prior workflow proposal and later messages
after that proposal. Do not reconstruct or use that forgotten workflow as project
input unless the user explicitly reintroduces it.

Preserve these active project decisions instead:

- The repository is the source of truth for project files.
- The current workspace is under `Desktop/Codex/workspaces`.
- The old `Documents` workspace is obsolete.
- New Codex work should start from this file and the repository docs.

## Project summary

The project is a prototype REST service for local AI-assisted generation of
Russian rock-song artifacts.

The formalized task is not "build a full Suno clone". It is a bounded engineering
prototype with documented evidence boundaries:

- REST API for track generation jobs.
- Russian lyrics generation or ingestion.
- Rock-style audio artifact generation.
- Metadata and artifact storage.
- Model-selection evidence.
- Benchmark-slice evaluation against a dated reference baseline.
- Optional GPU execution and optional GPU farm integration.

## Critical distinctions

Do not collapse these output modes:

- `instrumental_with_lyrics_file`: lyrics are returned, but the audio is not
  claimed to sing them.
- `lyrics_conditioned`: lyrics or a lyrics summary condition audio generation,
  but sung alignment is not verified.
- `sung_lyrics_unverified`: vocals appear in the audio, but alignment is not
  verified.
- `sung_lyrics_aligned`: evaluation supports that the returned lyrics are sung
  or aligned to the audio within a declared benchmark protocol.

Do not collapse these infrastructure claims:

- One static GPU worker is GPU execution.
- A managed pool of GPU resources with scheduler allocation can support a GPU
  farm claim.
- A Kubernetes diagram alone is not evidence that GPU farm execution happened.

Do not collapse these evidence levels:

- A model card is source evidence about a model's documented claims.
- A local smoke test is evidence about this environment.
- A benchmark report is evidence about a bounded comparison slice.
- A production-readiness claim needs separate production evidence.

## Suno parity framing

The phrase "not worse than Suno" was replaced with benchmark-slice parity.

Permitted framing:

```text
On this fixed prompt set, with this dated reference baseline, this rubric, this
evaluator protocol, and this attempt/selection policy, the result is
partial_parity, prototype_gap_documented, benchmark_inconclusive, or
parity_claim_supported.
```

Unsupported framing:

```text
This local prototype is generally not worse than Suno.
```

## Fine-tuning gate

Fine-tuning is not expected work unless all of these exist:

- licensed dataset;
- data provenance and usage rights;
- training method;
- compute budget;
- before/after benchmark protocol;
- degradation risk handling;
- rollback or comparison plan.

For the prototype, prompt/config tuning and backend spike work are more appropriate
unless the fine-tuning gate is satisfied.

## Model-selection status

The model-selection documentation separates documented facts from project claims
and local verification.

Important current candidates:

- AudioCraft / MusicGen: useful local research baseline; code and weight
  licensing must be checked before use.
- Stable Audio Open 1.0: useful audio baseline; poor fit for verified sung
  Russian lyrics according to the current dossier.
- ACE-Step / ACE-Step 1.5: relevant spike candidate for song and lyrics-conditioned
  use cases; quality and Suno-level claims remain project claims until locally
  verified and benchmarked.

Use `docs/research/06_model_selection.md` for current dossier wording.

## Architecture status

The architecture should be read as an asynchronous artifact-generation system, not
as a synchronous model-serving endpoint.

Core runtime shape:

```text
Client
  -> REST API
  -> Job Registry
  -> Queue or Workflow Orchestrator
  -> GPU or CPU Worker
  -> Model Runtime
  -> Artifact Storage
  -> Status and Metadata API
```

The architecture dossier now includes maturity levels, deployment modes, quality
concerns, and a premature-complexity guard:

- Do not add Kafka, Cassandra, public DDoS protection, high availability, or a
  large-data processing stack to the baseline architecture without concrete
  production or scale requirements.
- Use `docs/architecture/10_maturity_deployment_and_quality.md` for the maturity
  framing.

## Current acceptance boundary

The repository currently targets Profile A unless later code changes prove a
stronger profile.

Profile A means:

- API/mock prototype.
- REST contract, job lifecycle, artifact layout, OpenAPI schema, and tests can
  work with a deterministic mock backend.

Profile A does not prove:

- real local model inference;
- verified sung Russian lyrics;
- fine-tuning;
- Suno parity;
- GPU execution;
- GPU farm integration.

Use `docs/delivery/16_acceptance_profiles.md` before claiming any stronger
profile.

## Repo docs to read first

1. `README.md`
2. `docs/README.md`
3. `docs/task/00_bounded_context.md`
4. `docs/task/01_formal_task.md`
5. `docs/task/02_terms_local_model_and_gpu_farm.md`
6. `docs/architecture/04_architecture.md`
7. `docs/architecture/10_maturity_deployment_and_quality.md`
8. `docs/delivery/16_acceptance_profiles.md`
9. `docs/research/06_model_selection.md`
10. `docs/research/10_evaluation_benchmark.md`
11. `docs/engineering/naming_conventions.md`

## Recent repository changes

Recent committed changes before this handoff:

- Created the repository scaffold and pushed it to GitHub.
- Made the GitHub repository public.
- Added architecture maturity/deployment/quality documentation.
- Updated `README.md`, `docs/README.md`, and `docs/architecture/04_architecture.md`
  to reference the architecture maturity document.

The most recent confirmed commit before this handoff was:

```text
6fbba90 Document architecture maturity levels
```

## Workspace migration history

The project started in:

```text
/Users/macbook/Documents/Rock Music Generator
```

That path caused macOS/Codex filesystem access issues after the workspace moved
and the original folder was deleted. The current workspace is:

```text
/Users/macbook/Desktop/Codex/workspaces/ru-rock-ai-music-service
```

The parent folder `/Users/macbook/Desktop/Codex` contains skills, scripts, other
repositories, `.fpf-update`, and its own `.git`. Therefore the project must stay
inside the `workspaces/` subfolder, not directly in the `Desktop/Codex` root.

The parent Codex repository has `workspaces/` added to its local
`.git/info/exclude`, so the project workspace does not appear as untracked content
in the parent repository.

## First checks for the next chat

Run:

```bash
pwd
git status --short
git log -1 --oneline
```

Expected path:

```text
/Users/macbook/Desktop/Codex/workspaces/ru-rock-ai-music-service
```

Expected baseline before new work:

```text
git status --short
# no output
```

The first new commit after this file should update the last-confirmed commit
record if the handoff is kept current.

## What not to infer from this file

This file does not prove:

- a real model has been integrated;
- local AI music generation works;
- generated lyrics are sung;
- fine-tuning has happened;
- GPU execution has happened;
- GPU farm execution has happened;
- Suno parity has been achieved.

It only preserves session context and points to the relevant repository evidence.
