---
id: observability
title: Observability
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- assurance
related:
- durable-execution
- security
sources:
- otel-traces
---

# Observability

Observability connects task outcomes to the operations that produced them. OpenTelemetry's trace model supplies spans, parent-child relationships and distributed context propagation. Applying that model to agent runs is a useful engineering synthesis, not proof that all agent telemetry fields have a stable shared schema. [otel-traces](https://opentelemetry.io/docs/concepts/signals/traces/)

## Reconstruct the execution {#execution-record}

Recommended records associate a task with model invocations, tool attempts, returned outcomes, approvals, checkpoints and produced artifacts. Use separate identities for the logical operation and each retry attempt. Record timestamps, configuration versions and explicit completion states.

A trace should help distinguish a model that chose the wrong tool from a valid call rejected by policy, a network timeout, or a successful action whose result was lost. A single error counter obscures these different repair paths.

## Correlate without overcollecting {#data-minimization}

Metadata can locate many failures without storing every document or prompt. Raw inputs and outputs may contain credentials, private records or attacker-supplied text. Use scoped retention and access control, redact sensitive fields, and decide which artifacts must be retained for reproducibility. Sampling reduces cost but may omit rare failures; define how failed or consequential runs are captured.

Do not require hidden model reasoning for an audit trail. Observable requests, policy decisions, tool results and artifact changes provide concrete evidence. A generated explanation of why an action occurred is not a substitute for those records.

## From telemetry to diagnosis {#diagnosis}

For a duplicate external write, correlate the logical request, retry attempts and checkpoint sequence. For an incorrect answer, inspect the evidence actually supplied to the model and the task configuration. Keep outcome grading separate: a complete trace can describe an incorrect run.

Test correlation across process restart and remote delegation. Pin the instrumentation schema used by producers and consumers; evaluate migration before treating unfamiliar fields as equivalent. General tracing is established, while portable agent-specific conventions need separate verification. [Evaluation design](evaluation-design.md) supplies correctness criteria, and [durable execution](../execution/durable-execution.md) owns recovery semantics.

## References {#references}

- [Traces](https://opentelemetry.io/docs/concepts/signals/traces/) — `otel-traces`.
