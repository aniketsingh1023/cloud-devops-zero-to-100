# Start here

You can begin with a laptop, Git, and Python 3.11 or later. A cloud account is optional for the first stage. Windows users can use WSL2 for Linux commands; macOS users should use a Linux VM or container when a lesson depends on Linux-specific behavior.

## Your first session

1. Read this page and choose **one** learning track below.
2. Create a learning repository or fork this one. Copy the [learning log](templates/learning-log.md).
3. Run the [local build-and-break lab](labs/build-break-fix/README.md). It makes no cloud API calls.
4. Change one behavior, observe the result, and explain it in your log.
5. Pick the next task from the [roadmap](roadmap/100-days.md).

## Choose one cloud

| Track | Start with | First objective |
|---|---|---|
| AWS | [AWS learning resources](resources/cloud.md) | Explain IAM, VPC, compute and object storage |
| Azure | [Microsoft Learn in the cloud catalog](resources/cloud.md) | Explain identity, resource groups, networking and compute |
| Google Cloud | [Google training in the cloud catalog](resources/cloud.md) | Explain projects, IAM, networks and compute |
| Local first | [Local lab](labs/build-break-fix/README.md), then [containers](resources/containers.md) | Run, inspect, break and recover a service |

Choose the provider your work, community or project uses. You can learn the others later by mapping concepts rather than starting from zero.

## A sustainable daily loop

Use about 60–90 minutes when available: read for 15 minutes, build or debug for 40, explain for 10, then pick the next question. Adjust the pace for your circumstances. Protect focused time; rest and a sustainable routine support learning too.

Before opening a tutorial, write a question. After following it, close it and recreate the important step from memory. Keep a note of what you cannot yet explain.

## Before a cloud lab

- Use a separate learning account/project and protect administrative access with MFA.
- Review the provider’s current pricing and each lab’s billable resources. “Free tier” does not mean every action is free.
- Set billing alerts. A budget alert alone does not stop resource spending.
- Use short-lived credentials when possible. Keep secrets and state files out of Git.
- Write cleanup steps before provisioning. Check disks, snapshots, load balancers, IP addresses and other resources after teardown.

## What counts as progress?

A screenshot is supporting evidence. A stronger deliverable includes your code/configuration, instructions someone else can follow, a diagram, a failure you investigated, and cleanup steps. See the [project rubric](projects/README.md#portfolio-rubric).
