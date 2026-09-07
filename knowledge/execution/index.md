---
id: execution
title: Execution and control
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- execution
related:
- context
- action
- security
- assurance
sources:
- building-agents
- managed-agents
sidebar_position: 1
---

# Execution and control

An agent system turns a task into actions and checks their effects. This knowledge base uses **agent** for a system in which a model can choose subsequent actions from observations, and **Agent Harness** for the surrounding software that runs that process. These are editorial working definitions: industry usage overlaps, and a framework or hosted runtime may supply only part of the harness.

Anthropic distinguishes predefined workflows from model-directed control. Its later hosted design separates the session record, harness loop, and sandbox. These support useful boundaries without requiring that every deployment use separate services. [building-agents](https://www.anthropic.com/engineering/building-effective-agents) [managed-agents](https://www.anthropic.com/engineering/managed-agents)

## Responsibility boundaries {#responsibility-boundaries}

| Component | Responsibility | Failure to distinguish it |
| --- | --- | --- |
| Model | Propose next actions or output | Treating a prediction as a completed action |
| Harness | Assemble inputs, dispatch allowed actions, track progress | Losing ownership of stopping and errors |
| Environment | Execute operations and expose observations | Assuming a transcript restores files or remote state |
| Task contract | Define requested result and constraints | Declaring success because the loop stopped |

This decomposition is an engineering model, not a standardized API. A compact local process offers straightforward setup and debugging. Separating services allows different lifetimes and access boundaries, but introduces message delivery, versioning and recovery work.

## Task and environment lifecycle {#task-and-environment-lifecycle}

As a design practice, establish inputs, permitted scope, output artifacts and observable completion criteria before an extended run. Initialize the workspace from an identifiable baseline; record which artifacts the run owns and which are shared. A browser session, repository checkout and remote database have different restoration needs. Define retention and cleanup separately from model context disposal.

Use [control flow](control-flow.md) to choose actions and stopping rules, [durable execution](durable-execution.md) to survive interruptions, and [coordination](multi-agent-coordination.md) when work has multiple owners. General release and rollback decisions belong in [evaluation and operations](../assurance/index.md).

## Established boundary, evolving implementation {#maturity}

Explicit ownership of state and effects is a stable design concern. The best placement of that ownership, and how much model-specific scaffolding is useful, remain deployment-dependent. Benchmark the complete system when replacing either the model or harness.

## References {#references}

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — `building-agents`.
- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents) — `managed-agents`.
