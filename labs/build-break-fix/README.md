# Build. Break. Fix. Explain.

A tiny HTTP lab that demonstrates an important distinction: **a process can be alive while the service is unable to serve users.** Python 3.11+ is enough. No packages, cloud credentials or cloud resources are required.

This uses Python’s development HTTP server for local learning. The application has no authentication and is not intended for internet-facing production hosting.

## Run with Python

From the repository root:

```bash
python3 labs/build-break-fix/app.py
```

In another terminal:

```bash
curl -i http://127.0.0.1:8080/
curl -i http://127.0.0.1:8080/healthz
curl -i http://127.0.0.1:8080/readyz
```

All three return HTTP 200. Stop the server with Ctrl+C. If port 8080 is occupied, set `PORT=8081` and update your curl URLs.

## Break it deliberately

In a POSIX shell (Linux, macOS or WSL), restart the server with failure mode enabled:

```bash
FAIL_MODE=1 python3 labs/build-break-fix/app.py
```

For PowerShell, set `$env:FAIL_MODE="1"` before running the Python command, and set it to `"0"` for recovery.

| Endpoint | Healthy | Failure mode | Meaning in this lab |
|---|---|---|---|
| `/` | 200 | 503 | Simulated user request succeeds or fails |
| `/healthz` | 200 | 200 | Process can still answer a liveness request |
| `/readyz` | 200 | 503 | Instance should stop receiving workload traffic |
| Unknown route | 404 | 404 | Route does not exist |

Observe the structured logs, repeat the curl requests and record your hypothesis. The failure is simulated by configuration; no actual external dependency is contacted. Changing the shell environment does not change an already-running process: restart it to change modes.

Stop the failing process, restart normally, and verify `/` and `/readyz` return 200 again. If you set an environment variable persistently in your shell, reset it first.

## Optional Docker path

Requires a working Docker Engine/Desktop and Compose. Downloading the base image needs network access. Local image storage and compute are used; Docker product licensing depends on your circumstances.

```bash
docker compose -f labs/build-break-fix/compose.yaml up --build -d
docker compose -f labs/build-break-fix/compose.yaml ps
docker compose -f labs/build-break-fix/compose.yaml logs app
FAIL_MODE=1 docker compose -f labs/build-break-fix/compose.yaml up -d --force-recreate
```

After repeated failed readiness checks, the container becomes **unhealthy**. Docker’s standalone health check reports status; it does not automatically remove the container from a load balancer or restart it. Kubernetes probe behavior is a later exercise.

Recover and stop:

```bash
FAIL_MODE=0 docker compose -f labs/build-break-fix/compose.yaml up -d --force-recreate
docker compose -f labs/build-break-fix/compose.yaml down
```

The image uses a readable version tag for beginner convenience. For a reproducibility exercise, record the resolved base-image digest and compare a digest-pinned build. This starter is not a complete hardened production image.

## Verify the behavior

```bash
python3 -m unittest discover -s labs/build-break-fix -p 'test_*.py' -v
```

## Explain before moving on

1. Why would a liveness-only monitor miss the user-visible failure?
2. What could go wrong if a temporary dependency failure triggered constant process restarts?
3. What would a reverse proxy need to do with the readiness signal?
4. Which signal would you use for an SLI, and why?

Complete a [short incident review](../../templates/postmortem.md). Extend the lab with bounded metrics or an automated recovery drill in your own project.
