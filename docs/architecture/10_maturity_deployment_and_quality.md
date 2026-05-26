# 10 — Maturity, deployment, and quality concerns

## Purpose

This file prevents a generic AI-service diagram from becoming the architecture claim.

The system is best described as an asynchronous artifact-generation service, not as a
synchronous model-serving endpoint.

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

Primary artifacts:

- `request.json`
- `lyrics.json`
- `audio.wav` or `audio.mp3`
- `metadata.json`
- optional `benchmark_record.json`
- optional `worker.log`

## Quality concerns

Use these as architecture concerns, not as automatic production requirements.

| Concern | MVP reading | Stronger reading |
| --- | --- | --- |
| Reproducibility | Pin model id, seed, parameters, backend, and output mode. | Pin model weights, container image, hardware class, benchmark set, and runtime version. |
| Artifact traceability | Store lyrics, audio, request, and metadata together. | Store immutable artifacts with content hashes and benchmark links. |
| Failure visibility | Expose `failed` status and error metadata. | Add retry policy, cancellation, dead-letter handling, and alerting. |
| Local/cloud portability | Run locally with filesystem storage and a mock backend. | Run with object storage, external queue, containerized workers, and GPU scheduling. |
| GPU cost control | Keep GPU execution optional and visible. | Use cold start, warm pool, quotas, cache policy, and cost telemetry. |
| Benchmark evidence | Do not claim Suno parity without a benchmark slice. | Publish dated parity reports with prompt set, rubric, evaluator mode, and unsupported claims. |
| Operational reliability | Keep job state recoverable enough for prototype review. | Add SLOs, HA, incident response, and public traffic defenses only when production scope exists. |

## Deployment modes

### Mode A — Local mock or CPU demo

Purpose:

- Prove API contract, job lifecycle, artifact layout, and tests.

Typical shape:

```text
FastAPI -> local job store -> mock backend -> local filesystem artifacts
```

This mode supports Profile A only.

### Mode B — Local controlled model runtime

Purpose:

- Prove that a real local backend can create an audio artifact through the same service interface.

Typical shape:

```text
FastAPI -> local job store or simple queue -> local model worker -> filesystem artifacts
```

This mode can support Profile B if metadata and model evidence are present.

### Mode C — Single controlled GPU worker

Purpose:

- Move generation outside the API request path and run it on one known GPU resource.

Typical shape:

```text
FastAPI -> queue -> static GPU worker -> artifact store
```

This is GPU execution, not a GPU farm.

### Mode D — Managed GPU pool

Purpose:

- Dispatch jobs to a scheduler that can allocate among multiple GPU resources.

Typical shape:

```text
FastAPI -> job registry -> queue or workflow engine -> Kubernetes/Slurm/Ray workers -> object storage
```

This mode can support a GPU farm claim only when the scheduler or infrastructure
contract actually manages a pool of GPU resources.

### Mode E — Production service

Purpose:

- Serve external users under explicit traffic, reliability, security, and cost constraints.

Typical additions:

- authentication and authorization;
- quotas and rate limits;
- model registry and rollout controls;
- audit logs;
- public observability and alerting;
- SLO/SLA definitions;
- incident handling;
- cost tracking.

Do not treat this as the default target for a test assignment.

## Maturity levels

### Level 1 — Local prototype

Goal:

- Demonstrate the end-to-end service shape.

Architecture:

```text
FastAPI
  -> local job registry
  -> in-process or background worker
  -> mock or local model runtime
  -> local filesystem artifacts
```

Expected evidence:

- OpenAPI is available.
- Job lifecycle works.
- Artifacts are saved.
- Tests pass without model weights or GPU.
- Current acceptance profile is stated.

Avoid:

- Kafka.
- Cassandra.
- Kubernetes.
- high-availability claims.
- public production security claims.

### Level 2 — Service MVP

Goal:

- Make the prototype operationally realistic without requiring a full GPU farm.

Architecture:

```text
FastAPI
  -> Postgres job registry
  -> Redis/RabbitMQ queue
  -> Celery/RQ workers
  -> filesystem or MinIO/S3-compatible artifact storage
```

Expected evidence:

- Jobs survive API process restarts, if persistence is claimed.
- Worker failures are visible.
- Artifacts are retrievable by API.
- Metadata records model, version, backend, device, seed, settings, and output mode.

### Level 3 — GPU farm candidate

Goal:

- Separate API, scheduling, and GPU compute.

Architecture:

```text
REST API
  -> Job Registry
  -> Queue or Workflow Engine
  -> Scheduler Adapter
  -> GPU Worker Container
  -> Model Runtime and Model Cache
  -> Object Storage
```

Expected evidence:

- The scheduler path is real or explicitly marked as simulation.
- Worker allocation metadata is recorded.
- Artifact storage survives worker termination.
- Cold start, warm pool, and model cache behavior are measured or explicitly unmeasured.
- One static worker is not called a GPU farm.

### Level 4 — Production service

Goal:

- Operate under real user, traffic, security, cost, and reliability constraints.

Architecture additions:

- API gateway or ingress policy;
- authentication and authorization;
- tenant or quota model, if users are distinct actors;
- observability stack;
- alerting and incident process;
- model/version registry;
- rollout and rollback process;
- cost controls;
- security review;
- data retention policy.

This level requires explicit production requirements. It should not be smuggled into
the MVP through generic phrases such as "high availability" or "large data volumes".

## Premature complexity guard

Do not add these technologies or claims to the baseline architecture unless the
project has a concrete requirement that makes them necessary:

| Item | Keep out of MVP because | Reconsider when |
| --- | --- | --- |
| Kafka | A simple job queue is enough for one generation workflow. | Multiple event consumers, high event throughput, replay, or long event retention are required. |
| Cassandra | Job state and artifact metadata are relational enough for Postgres or SQLite in early stages. | Write scale, partition strategy, or multi-region data requirements are explicit. |
| DDoS protection | It is a public-traffic security concern, not a prototype architecture concern. | The service is publicly exposed or has an abuse model. |
| High availability | It requires SLOs, redundancy, failover, and operational ownership. | A production SLO/SLA is declared. |
| Large-data processing stack | Generation creates artifacts, but the MVP is not a bulk data ingestion platform. | Training pipelines, dataset curation, or high-volume analytics are in scope. |
| Multi-tenant account system | It is not required to prove generation architecture. | Distinct users, quotas, billing, or access control become acceptance criteria. |

## Dossier rule

When summarizing architecture for this project, prefer this claim:

```text
The project is an asynchronous artifact-generation service with explicit job state,
artifact storage, model-runtime metadata, and benchmark-slice evidence.
```

Avoid this claim unless evidence exists:

```text
The project is a production-ready, highly available AI music platform.
```
