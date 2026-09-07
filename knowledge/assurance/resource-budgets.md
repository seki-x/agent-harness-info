---
id: resource-budgets
title: Resource budgets
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- assurance
related:
- control-flow
- durable-execution
- context
sources:
- aws-backoff
- multi-agent-research
---

# Resource budgets

Resource budgets bound the time, computation and external activity spent on a task. The objective is useful completion under constraints, not minimizing tokens in isolation. Anthropic's multi-agent research account reports significant token overhead; those ratios describe that system, not universal cost multipliers. [multi-agent-research](https://www.anthropic.com/engineering/multi-agent-research-system)

## Allocate by task outcome {#allocation}

Recommended limits include model tokens, tool calls, elapsed time, worker concurrency and external service quotas. Share the task budget across child workers and reserve capacity for integration and verification. Otherwise successful subtasks can exhaust the resources needed to deliver the result.

A smaller or faster model can reduce cost per call while requiring more retries. Compare total cost per accepted task, latency percentiles and failure rates on the actual workload. Route by measured task needs and provide a bounded fallback path; no model ranking or current price is assumed here.

## Timeouts and retries {#timeouts-and-retries}

AWS's backoff analysis explains why deterministic retry timing can preserve synchronized contention and why jitter helps spread attempts. Applying randomized delays and bounded retries to remote model or tool calls is a distributed-systems adaptation. [aws-backoff](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)

Control flow owns whether a retry is justified; [durable execution](../execution/durable-execution.md#side-effects) owns whether repeating its effect is safe. This page owns the ceilings. Account for retries performed inside SDKs as well as those scheduled by the harness. A request timeout limits waiting; it does not prove that the remote effect was cancelled.

## Degrade explicitly {#budget-exhaustion}

When capacity runs low, reduce optional exploration or return a clearly bounded partial result with unresolved work. Do not label budget exhaustion as success. Define fairness across users so one expansive run cannot consume all worker slots.

For example, parallel research may reduce elapsed search time while increasing total calls and synthesis work. Measure both dimensions. More context, more workers and more retries are choices to test, not monotonic improvements. Budgeting is core; optimal allocation and automatic model routing remain workload-dependent.

## References {#references}

- [Exponential Backoff And Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) — `aws-backoff`.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — `multi-agent-research`.
