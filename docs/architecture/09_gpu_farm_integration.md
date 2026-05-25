# 09 — GPU execution and optional GPU farm integration

## Goal

Allow the REST API to dispatch generation jobs to GPU workers. Treat a real GPU farm as the stronger case: a managed pool of multiple GPU resources with scheduling, lifecycle, and observability.

This is optional for the prototype unless explicitly required.

If the implementation uses one fixed GPU worker, call it `GPU execution`, not `GPU farm`.

## Minimal architecture

```text
API Service
  ↓
Job Queue
  ↓
GPU Worker
  ↓
Local Model Runtime
  ↓
Artifact Store
  ↓
API Service
```

## Full architecture

```text
API Service
  ↓
Queue
  ↓
Scheduler Adapter
  ├── Kubernetes Job Adapter
  ├── Slurm Job Adapter
  ├── Ray Task/Actor Adapter
  └── Static Worker Adapter
  ↓
GPU Worker Container
  ↓
Model Cache / Model Runtime
  ↓
Artifact Store
  ↓
Metadata Store
```

This full architecture becomes a GPU farm only when the scheduler can allocate among multiple GPU resources or nodes. A dry-run adapter, one static worker, or one manually selected GPU machine is not a GPU farm.

## Required job lifecycle

Statuses:

- `queued`
- `scheduled`
- `starting_worker`
- `loading_model`
- `running`
- `post_processing`
- `completed`
- `failed`
- `cancelled`

## Cold-start vs warm-start

Document which strategy is implemented.

### Cold start

A worker is created for each job.

Pros:

- Lower idle cost.
- Cleaner isolation.

Cons:

- Slow startup.
- Repeated model loading.
- More orchestration complexity.

### Warm pool

Workers stay alive with model loaded.

Pros:

- Low latency.
- Good for repeated generation.

Cons:

- Higher idle GPU cost.
- Requires worker health and recycling.

## Kubernetes option

If using Kubernetes:

- Use GPU node labels.
- Request GPU resources explicitly.
- Store artifacts outside the pod.
- Avoid losing artifacts when pods terminate.
- Record pod name, node name, GPU type, image tag, and model cache path in metadata.
- Document whether NVIDIA GPU Operator, the NVIDIA device plugin, or another GPU enablement path is used.
- Record driver/CUDA/container runtime assumptions when they affect reproducibility.

Example conceptual worker spec fields:

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

## Slurm option

If using Slurm:

- Submit one generation job per request or batch.
- Capture Slurm job ID.
- Map Slurm status to API job status.
- Write artifacts to shared storage.

## Ray option

If using Ray:

- Use a remote actor for warm model runtime.
- Use placement groups or GPU resource requests.
- Return artifact paths rather than large audio blobs through the scheduler.

## Static worker option

For MVP:

- Run one worker process on a known GPU machine.
- Use Redis/SQLite queue.
- Avoid claiming “GPU farm” unless multiple GPU resources are actually managed.

## Metadata requirements

For GPU execution, add:

```json
{
  "scheduler": "kubernetes|slurm|ray|static",
  "worker_id": "...",
  "node_id": "...",
  "gpu_type": "...",
  "gpu_count": 1,
  "container_image": "...",
  "model_cache_hit": true,
  "cold_start_sec": 43.2,
  "model_load_sec": 21.8
}
```

## Acceptance criteria for GPU farm bonus

The bonus is accepted if:

- API creates a job.
- Job is dispatched to a GPU worker.
- Worker generates or mocks generation through the same interface.
- Worker stores artifacts and metadata.
- API returns final status and artifact links.
- Failure states are visible.
- The implemented on-demand behavior is documented precisely.

For a real GPU farm claim, also require:

- More than one GPU resource or node is schedulable, or the infrastructure contract explicitly describes the managed GPU pool.
- Scheduler metadata identifies the allocated worker/resource.
- Cold-start, warm-start, and model-cache behavior are measured or explicitly marked unmeasured.
- The documentation distinguishes real scheduler execution from dry-run or static-worker simulation.
