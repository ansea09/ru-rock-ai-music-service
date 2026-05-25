# 06 — Model selection

## Selection question

Choose a local model or local model pipeline for a prototype that generates Russian rock-song artifacts.

The model decision must be evidence-backed and explicitly scoped. The first prototype may use a model that is not at Suno quality if the limitation is documented and the evaluation protocol is honest.

## Selection criteria

| Criterion | Why it matters |
|---|---|
| Local deployability | Required by assignment. |
| License | Determines whether prototype, commercial, or research-only use is allowed. |
| Audio quality | Core output quality. |
| Vocal support | Required if the target is a full song with sung lyrics. |
| Lyrics alignment | Required if the output must sing the generated Russian lyrics. |
| Russian-language support | Required by target language. |
| Rock genre adherence | Required by target genre. |
| Inference cost | Determines feasibility. |
| Fine-tuning support | Relevant only if training data exists. |
| API integration complexity | Affects prototype speed. |
| Reproducibility | Needed for benchmark and debugging. |
| Evidence quality | Separates project claims, model-card facts, local smoke tests, and independent benchmark evidence. |

## Source register required for each candidate

For every candidate, maintain a source register. Do not leave claims as free text.

```text
Candidate:
Source URL:
Accessed date:
Claim checked:
Source type: official repo | model card | paper | local smoke test | benchmark report | other
Evidence status: project_claim | documented_fact | locally_verified | independently_benchmarked | unknown
License verdict:
Hardware/VRAM claim:
Vocal/lyrics claim:
Russian-language claim:
Remaining uncertainty:
```

Use official repositories, model cards, papers, or local test records as primary evidence. Avoid treating blog posts, demos, or generated summaries as authoritative.

## Current source-backed candidate notes

Last checked for this dossier: 2026-05-26.

These notes are not a final model decision. They are source-backed inputs for the candidate spike and must be rechecked on the implementation date.

| Candidate | Source-backed claims | Evidence status | Implication for this assignment |
|---|---|---|---|
| AudioCraft / MusicGen | Official AudioCraft repository states that AudioCraft is a PyTorch library with inference and training code for MusicGen and other audio models. The repository states that code is MIT-licensed and model weights are CC-BY-NC 4.0. Source: https://github.com/facebookresearch/audiocraft | `documented_fact` for repository/code/weight license statements; `locally_verified` only after a local run. | Good local research baseline for text-to-music/audio experiments. Not suitable for commercial acceptance without license review. Not sufficient evidence for full Russian sung-song generation. |
| Stable Audio Open 1.0 | Official Hugging Face model card states variable-length stereo generation up to 47 seconds at 44.1 kHz, English language, Stability AI Community License, and commercial use via separate Stability AI licensing. It also states the model is not able to generate realistic vocals and is trained with English descriptions. Source: https://huggingface.co/stabilityai/stable-audio-open-1.0 | `documented_fact` for model-card claims; `locally_verified` only after a local run. | Useful audio baseline for text-to-audio/music texture. Poor fit for verified sung Russian lyrics. Should not be selected for `sung_lyrics_aligned` MVP. |
| ACE-Step / ACE-Step 1.5 | Official repository states local execution paths, MIT license, flexible duration from 10 seconds to 10 minutes, and 50+ language lyrics prompt support. It also claims commercial-grade/Suno-level quality and fast generation. Source: https://github.com/ace-step/ACE-Step-1.5 | `documented_fact` for repository license and stated feature support; `project_claim` for quality/Suno-level claims until independently benchmarked or locally evaluated. | Most relevant spike candidate for song-level and lyrics-conditioned generation. Must still pass local reproducibility, license/weights review, Russian output check, and benchmark evaluation before any parity claim. |

Evidence rule:

- Treat official README/model-card statements as source-backed claims about the project documentation.
- Treat quality superiority, “commercial-grade”, or “Suno-level” wording as `project_claim` unless the local benchmark or an independent benchmark supports it.
- Move runtime claims from `documented_fact` to `locally_verified` only after a successful local run on the target hardware.
- Move output-quality claims to `parity_claim_supported` only through `docs/research/10_evaluation_benchmark.md`.

## Candidate classes

### Candidate A — AudioCraft / MusicGen family

Use when the prototype can accept instrumental or weak-vocal generation and prioritizes a known local research stack.

Strengths:

- Local PyTorch library.
- Inference and training code are available.
- MusicGen supports text-conditioned music generation.
- Good candidate for a first local prototype.

Risks:

- Weight license must be checked carefully.
- Not a guaranteed vocal or Russian lyrics solution.
- May not match commercial music-generation quality.
- Treat as a local music/audio baseline, not as evidence of full Russian sung-song parity.

### Candidate B — Stable Audio Open

Use when the prototype needs open-weights text-to-audio experimentation.

Strengths:

- Local usage through stable-audio-tools or diffusers.
- Generates stereo audio up to a documented duration limit.
- Useful for research and prompt/config experiments.

Risks:

- Primarily English-prompt trained.
- Model card states it cannot generate realistic vocals.
- Commercial use and downstream use require license/risk review.
- Better suited for audio/music texture than complete Russian rock songs.
- Should not be selected if verified sung Russian lyrics are mandatory for MVP.

### Candidate C — ACE-Step / ACE-Step 1.5 family

Use when the prototype strongly needs song-level generation, lyric alignment, and multilingual support.

Strengths:

- Project claims open-source music foundation model direction.
- Project materials claim lyric alignment and multilingual support.
- The v1.5 project page claims local execution and low VRAM.
- More directly aligned with full-song and lyrics-conditioned targets than instrumental-only backends, if local reproducibility and license review pass.

Risks:

- Claims must be verified in a local spike.
- License, weights, and exact reproducibility must be checked.
- Quality claims on project pages should not be treated as independent benchmark proof.
- Vocal quality limitations are acknowledged by the project page.
- Any “commercial-grade” or “Suno-level” wording from project materials remains a project claim until validated by the local benchmark.

### Candidate D — Modular pipeline

Use when the end-to-end target is more important than a single model.

Possible modules:

1. LLM for Russian lyrics.
2. Structure planner for verse/chorus/bridge.
3. Text-to-music or lyrics-to-song model.
4. Optional singing/vocal component.
5. Post-processing / loudness normalization.

Strengths:

- Decomposable and testable.
- Russian lyrics can be improved independently from audio generation.
- Easier to benchmark sub-components.

Risks:

- Integration complexity.
- Vocal alignment may still be weak.
- More moving parts.

## Recommended prototype path

For the first implementation:

1. Start with a modular pipeline.
2. Use prompt/config tuning before fine-tuning.
3. Implement a pluggable model backend interface.
4. Provide at least one real local backend and one mock backend for tests.
5. Treat ACE-Step-like song-generation candidates as a spike if local reproducibility and license are acceptable.
6. Treat Stable Audio Open or MusicGen-like backends as baseline local audio backends, not guaranteed full-song equivalents.

## Decision matrix template

| Candidate | Local | License acceptable | Vocals | Russian lyrics | Fine-tune/adapt | Prototype effort | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| AudioCraft/MusicGen | TBD | TBD | weak/TBD | weak/TBD | yes/TBD | medium | Spike or baseline |
| Stable Audio Open | yes | review required | no realistic vocals | weak | TBD | medium | Audio baseline |
| ACE-Step / 1.5 | claimed | review required | claimed/limited | claimed | claimed | medium/high | Candidate spike |
| Modular pipeline | yes | per component | per backend | yes for lyrics | per component | high | Best architecture |

## Evidence status legend

- `project_claim`: claimed by the project page, README, demo, or paper, but not verified locally.
- `documented_fact`: stated in an official model card, license, or repository documentation.
- `locally_verified`: reproduced in the target environment or a controlled spike.
- `independently_benchmarked`: measured by a benchmark not controlled by the model project.
- `unknown`: not yet checked.

Model selection should prefer candidates whose critical claims are at least `documented_fact` and whose runtime claims can be moved to `locally_verified` before acceptance.

## Required final model decision

The implementation report must state:

```text
Selected backend: <model or pipeline>
Why selected: <evidence and constraints>
Rejected alternatives: <reason>
Known gap to Suno: <explicit gap>
Next step to improve: <bounded experiment>
```
