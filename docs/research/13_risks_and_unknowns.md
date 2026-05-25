# 13 — Risks and unknowns

## Model quality risk

Local open models may not match commercial closed systems for full-song quality, vocal quality, lyric alignment, and mixing/mastering.

Mitigation:

- Use benchmark report.
- Do not overclaim.
- Use modular pipeline.
- Run candidate spikes.

## Russian-language risk

Many audio/music models are trained primarily on English prompts or do not handle Russian lyrics naturally.

Mitigation:

- Generate Russian lyrics separately.
- Translate/augment conditioning prompt if needed.
- Evaluate Russian lyrics and sung intelligibility separately.

## Vocal generation risk

Some text-to-audio models cannot generate realistic vocals or cannot sing supplied lyrics.

Mitigation:

- Record `instrumental_only` or `lyrics_generated_but_not_sung` in metadata.
- Choose a lyrics-to-song model if vocals are mandatory.
- Consider separate singing synthesis only as a later phase.
- Require `actual_audio_mode` so generated lyrics are not mistaken for sung lyrics.

## License risk

Model code, model weights, training data, and generated outputs may have different licenses.

Mitigation:

- Review license before model use.
- Store license notes in model selection report.
- Do not assume “open weights” means commercial permission.
- Use only licensed datasets for fine-tuning.

## Fine-tuning risk

Fine-tuning can make quality worse, overfit style, or create license problems.

Mitigation:

- Require dataset and evaluation protocol.
- Start with prompt/config tuning.
- Run before/after benchmark.

## GPU cost and latency risk

Music generation can be slow and expensive, especially with cold-start workers.

Mitigation:

- Add mock backend for API tests.
- Measure generation time.
- Document cold start and model load time.
- Consider warm pool.

## Benchmark risk

Human scoring is subjective and reference systems change over time.

Mitigation:

- Fix prompt set.
- Record baseline date and settings.
- Keep reference artifacts where legally permitted.
- Use rubric-based qualitative notes.
- Declare evaluator mode and avoid one aggregate score unless a scoring policy is defined.

## Acceptance profile risk

The project can accidentally accept an API/mock prototype as if it were real local generation.

Mitigation:

- Use `docs/delivery/16_acceptance_profiles.md`.
- State target and actually satisfied profile in every task summary.
- Do not advance from Profile A to Profile B without real local backend evidence.

## Legal/content risk

Generated lyrics and music may resemble training data or reference styles.

Mitigation:

- Avoid artist imitation prompts in acceptance tests.
- Log prompts and outputs.
- Include license and data provenance review before production.

## Unknowns to resolve before production

- Required commercial license for selected model.
- Whether generated audio can be commercially used.
- Target GPU class and maximum acceptable latency.
- Whether exact sung Russian lyrics are required.
- Whether customer accepts instrumental output in MVP.
- Which acceptance profile is required for the test assignment.
- Required audio format and loudness standard.
- Security requirements for public API exposure.
