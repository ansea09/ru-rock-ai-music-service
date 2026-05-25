# 08 — Fine-tuning and configuration tuning

## Key distinction

Fine-tuning and “settings” are different engineering actions.

| Action | Changes model weights? | Requires dataset? | Typical cost | Evidence required |
|---|---:|---:|---:|---|
| Prompt tuning | No | No | Low | Before/after examples |
| Config tuning | No | No | Low/medium | Parameter sweep results |
| Seed search | No | No | Low/medium | Selection log |
| Post-processing | No | No | Low | Audio checks |
| LoRA/fine-tuning | Yes | Yes | Medium/high | Dataset, training logs, benchmark |
| Full fine-tuning | Yes | Yes | High | Strong dataset/license/eval evidence |

## Recommended first step

Start with prompt/config tuning.

Reasons:

- It is cheaper.
- It is faster.
- It does not require licensed training data.
- It gives a baseline before changing weights.
- It reduces the risk of making unsupported improvement claims.

For this test assignment, fine-tuning should not be assumed as required work unless the requester provides or approves a dataset and evaluation budget. A valid engineering response may implement the interface and experiment plan while explicitly deferring weight updates.

## Prompt/config tuning plan

1. Define 10 fixed prompts for Russian rock songs.
2. For each prompt, generate 3–5 candidates with different seeds/settings.
3. Score candidates using the benchmark rubric.
4. Select default settings.
5. Record parameter values and seeds.

Parameters to test depend on backend, but may include:

- `duration_sec`
- `seed`
- `cfg_scale`
- `temperature`
- `top_k`
- `top_p`
- `num_inference_steps`
- `negative_prompt`
- style keywords
- structure hints

## Fine-tuning prerequisites

Do not start fine-tuning unless all prerequisites are satisfied.

Required:

- Licensed dataset.
- Dataset provenance.
- Lyrics/audio alignment if needed.
- Train/validation split.
- Baseline before training.
- Evaluation rubric.
- Compute budget.
- Model license permits adaptation.
- Rollback plan.
- Legal review outcome for model license, data license, and generated-output use.
- A declared target characteristic to improve, not a general “make it like Suno” objective.

## Fine-tuning report template

```text
Objective:
  Improve <specific characteristic> for <scope>.

Dataset:
  Source:
  License:
  Size:
  Language:
  Genre:
  Lyrics alignment:

Training method:
  Method:
  Hyperparameters:
  GPU:
  Duration:

Evaluation:
  Baseline model:
  Test prompts:
  Metrics/rubric:
  Before:
  After:
  Verdict:

Risks:
  Overfit:
  License:
  Quality regression:
  Bias/style narrowness:
```

## Unsupported claim examples

Do not write:

> Fine-tuning will make it not worse than Suno.

Write:

> Fine-tuning is a candidate method to improve the declared benchmark characteristics. Whether it improves quality must be tested against the benchmark before/after.

Do not write:

> Fine-tuning was completed.

unless the repository contains training configuration, dataset provenance, run logs, output checkpoints or adapter artifacts, and before/after evaluation.
