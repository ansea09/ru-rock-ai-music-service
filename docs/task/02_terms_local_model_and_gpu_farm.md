# 02 — Terms: local model and GPU farm

## Local model

A local model is a model or model pipeline whose weights, runtime, and inference code run inside infrastructure controlled by the implementer or customer.

The infrastructure may be:

- A developer workstation.
- A single GPU server.
- On-premise servers.
- A private cloud GPU instance.
- A controlled GPU cluster.

The defining property is control over execution, versioning, environment, and artifact production.

A local model is not automatically:

- Open-source.
- Free to use commercially.
- Suitable for fine-tuning.
- Able to generate vocals.
- Able to generate Russian lyrics.
- Comparable to Suno in quality.
- Usable without GPU.
- Usable without internet for first-time model download.

## GPU farm

A GPU farm is a managed pool of GPU compute nodes exposed as shared execution capacity.

A proper GPU farm includes more than physical GPUs. It normally includes:

- Scheduler or orchestrator.
- Worker lifecycle management.
- Container/runtime setup.
- Driver and CUDA management.
- Queue or job dispatcher.
- Artifact storage.
- Logs and job status.
- Health checks.
- Resource cleanup.

Possible orchestration options:

- Kubernetes + NVIDIA GPU Operator.
- Kubernetes + device plugin + custom worker queue.
- Slurm.
- Ray.
- Nomad.
- Custom queue + persistent GPU workers.
- Private cloud autoscaling GPU workers.

## On-demand GPU execution

“On-demand” must be specified precisely.

Possible meanings:

1. Start a new container on an already running GPU node.
2. Start a new Kubernetes Job or Pod.
3. Start a VM or cloud GPU instance.
4. Load model weights into a warm worker.
5. Route to a pre-warmed worker pool.
6. Allocate a Slurm/Ray job.

Each meaning has different cold-start time, cost, and operational complexity.

## Recommended interpretation for this assignment

For the prototype:

- Mandatory: local inference on one controlled GPU or CPU fallback with documented limitations.
- Optional: queue + GPU worker abstraction.
- Bonus: real cluster orchestration with Kubernetes, Slurm, Ray, or equivalent.

Use the narrower term `GPU execution` when there is only one fixed GPU worker or a local worker process. Use `GPU farm` only when a scheduler or infrastructure contract manages a pool of GPU resources.
