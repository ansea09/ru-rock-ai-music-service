# 10 — Evaluation benchmark

## Purpose

Replace the vague criterion “not worse than Suno” with an auditable benchmark protocol.

The benchmark does not need to prove market-level parity. It must show what was tested, how, against what reference, and with what result.

## Benchmark objects

For each test prompt, store:

```text
benchmark/{case_id}/
├── prompt.md
├── local_result/
│   ├── lyrics.json
│   ├── audio.wav
│   └── metadata.json
├── reference_result/
│   ├── source.md
│   ├── audio_reference_link_or_file_note.md
│   └── metadata.md
└── evaluation.md
```

## Reference baseline

If Suno is used as a baseline, record:

- Date of generation.
- Product/version/mode if visible.
- Prompt used.
- Number of attempts.
- Whether the best candidate was manually selected.
- Reference artifact path or link if permitted.
- Any unavailable metadata.

Do not compare against an unspecified “Suno quality” memory.

Parity claims are scoped to the captured reference baseline only. Record the product date/mode and do not generalize to all Suno versions or future Suno behavior.

## Minimum prompt set

Use at least 10 prompts.

Example prompt classes:

1. Energetic Russian rock anthem.
2. Melancholic ballad rock.
3. Punk-rock short song.
4. Alternative rock with chorus emphasis.
5. Hard rock with dramatic lyrics.
6. Slow rock with narrative lyrics.
7. Female vocal style if backend supports it.
8. Male vocal style if backend supports it.
9. Guitar-driven instrumental with generated lyrics saved separately.
10. Prompt with specific theme and structure constraints.

## Scoring rubric

Each criterion should use a declared scale.

| Characteristic | Scale | Polarity | Notes |
|---|---|---|---|
| Prompt adherence | 1–5 ordinal | higher better | Does output match theme/style? |
| Genre adherence | 1–5 ordinal | higher better | Is it recognizably rock? |
| Russian lyrics quality | 1–5 ordinal | higher better | Grammar, naturalness, coherence. |
| Song structure | 1–5 ordinal | higher better | Verse/chorus/arc. |
| Vocal intelligibility | 1–5 ordinal | higher better | Only if vocals are generated. |
| Audio artifact severity | 1–5 ordinal | lower better | Glitches, clipping, noise. |
| Musicality | 1–5 ordinal | higher better | Subjective but rubric-bound. |
| Generation latency | seconds | lower better | Measured. |
| Failure rate | percent | lower better | Over benchmark run. |

## Suggested evaluator protocol

1. Blind or semi-blind listening where possible.
2. Same prompt for local and reference systems.
3. Same number of candidate generations per prompt where possible.
4. Evaluators score each criterion independently.
5. Report mean/median per criterion, but do not average ordinal scales into false precision unless a scoring policy is explicitly declared.
6. Keep qualitative notes.

## Evaluator modes

Use one of these modes explicitly:

- `single_reviewer_exploratory`: one evaluator produces a structured qualitative review. Good for early spikes; insufficient for strong parity claims.
- `multi_reviewer_benchmark`: two or more evaluators score independently, then the report summarizes agreement and disagreements.
- `automated_screening_only`: automated checks such as duration, clipping, loudness, or model-provided quality scores. Useful for filtering; insufficient for subjective musical parity.

Do not mix these modes without saying which result came from which mode.

## Scoring policy

Ordinal scores must not be collapsed into a single “overall score” unless the report declares:

- The aggregation method.
- Why aggregation is meaningful for the selected scale.
- How missing values are handled.
- Whether any characteristic is a hard gate rather than part of a weighted score.

Prefer per-characteristic verdicts and a final verdict class over a single number.

## Verdict classes

Use these instead of “not worse than Suno”:

- `parity_claim_supported`: benchmark supports parity within declared scope.
- `partial_parity`: comparable on some characteristics, worse on others.
- `prototype_gap_documented`: prototype works but is below baseline.
- `benchmark_inconclusive`: evidence insufficient.

The verdict must state the supported scope, for example:

```text
Verdict: partial_parity
Scope: 10-prompt Russian rock benchmark, single_reviewer_exploratory, Suno reference captured on <date>.
Unsupported claim: general Suno parity or production-ready commercial quality.
```

## Evaluation report template

```markdown
# Benchmark report

## Baseline

Reference system:
Date:
Mode/version:
Prompt set:
Candidate count per prompt:

## Local system

Model:
Model version:
Runtime:
GPU:
Settings:

## Rubric

<scales and scoring method>

## Results

<table or per-case notes>

## Verdict

<one of the verdict classes>

## Gaps

- Gap 1
- Gap 2

## Next experiments

- Experiment 1
- Experiment 2
```
