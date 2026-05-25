# 16 — Acceptance profiles

## Purpose

This file prevents one kind of artifact from being accepted as another.

The project may pass different profiles at different times. A profile is a bounded acceptance target, not a claim that the whole original assignment is complete.

## Profile A — API/mock prototype

Purpose:

- Prove the REST contract, job lifecycle, artifact layout, and tests.

Accepted evidence:

- API starts locally.
- OpenAPI schema exists.
- Mock backend creates deterministic lyrics and a valid placeholder audio file.
- Tests pass without model weights or GPU.

Does not prove:

- Real local AI music generation.
- Vocal generation.
- Lyric alignment.
- Suno parity.
- GPU execution.

## Profile B — Real local inference prototype

Purpose:

- Prove that at least one locally controlled model backend can generate an audio artifact through the same service interface.

Accepted evidence:

- Selected backend is documented with model name, version, license notes, and runtime assumptions.
- A generation job runs without external music-generation SaaS.
- The output audio file is produced by the local backend.
- Metadata records model, version, seed, parameters, device, duration, warnings, and actual output mode.
- The service still has a mock backend for tests.

Does not prove:

- The output is competitive with Suno.
- The output contains verified sung Russian lyrics.
- The model is commercially usable.

## Profile C — Russian lyrics and vocal target

Purpose:

- Separate generated lyrics, lyrics-conditioned audio, and verified sung lyric alignment.

Output modes:

- `instrumental_with_lyrics_file`: lyrics are returned, audio does not claim to sing them.
- `lyrics_conditioned`: lyrics or a structured summary condition the model, but alignment is not verified.
- `sung_lyrics_unverified`: vocals are present, but alignment is not verified.
- `sung_lyrics_aligned`: evaluation supports that the audio sings or aligns to the returned lyrics.

Accepted evidence for `sung_lyrics_aligned`:

- Returned lyrics and audio are stored together.
- Evaluation notes or tooling check whether the lyrics are actually sung.
- The benchmark report states tolerance and failure cases.

Non-acceptance:

- A lyrics file alone is not proof that lyrics were sung.
- A model README claim is not proof that this implementation aligned Russian lyrics.

## Profile D — Benchmark/parity report

Purpose:

- Replace “not worse than Suno” with a scoped comparison.

Accepted evidence:

- Fixed prompt set.
- Captured reference baseline with date, product/mode if visible, prompt, attempt count, and selection policy.
- Local outputs generated under pinned model/settings.
- Scoring rubric with scales, polarity, and evaluator mode.
- Per-characteristic results and qualitative notes.
- Verdict class: `parity_claim_supported`, `partial_parity`, `prototype_gap_documented`, or `benchmark_inconclusive`.

Non-acceptance:

- No unspecified “Suno quality” memory.
- No single aggregate score without a declared scoring policy.
- No general parity claim outside the benchmark slice.

## Profile E — GPU execution

Purpose:

- Prove asynchronous execution outside the API request path.

Accepted evidence:

- API creates a job.
- Queue or worker executes the job.
- Worker stores artifacts and metadata.
- API returns final status and artifact links.
- Metadata records worker/device fields.

This profile may be satisfied by one static worker. It should be called GPU execution, not GPU farm.

## Profile F — GPU farm integration

Purpose:

- Prove dispatch to a managed pool of GPU resources.

Accepted evidence:

- Scheduler or orchestrator adapter is implemented or integrated.
- More than one GPU resource or node is schedulable, or the infrastructure contract explicitly describes the managed GPU pool.
- Scheduler metadata identifies the allocated worker/resource.
- Cold-start or warm-pool behavior is documented.
- Artifact storage survives worker termination.
- Failure states are visible.

Non-acceptance:

- A dry-run adapter is not a GPU farm.
- One manually selected GPU machine is not a GPU farm.
- A Kubernetes diagram is not evidence that cluster execution happened.

## Reporting rule

Every implementation summary must state:

```text
Target profile:
Actually satisfied profile:
Evidence:
Known gaps:
Unsupported claims:
```
