---
id: action
title: Action and integration
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- action
related:
- control-flow
- isolation-authorization
- durable-execution
sources:
- gemini-function-calling
- gemini-structured-output
- tool-design
- swe-agent
sidebar_position: 1
---

# Action and integration

Tools connect model decisions to external observations and effects. Google's function-calling documentation explicitly assigns function execution to the application, while the model selects calls and arguments. This separation makes the tool boundary a place for validation and authority checks. [gemini-function-calling](https://ai.google.dev/gemini-api/docs/function-calling)

## Contracts for model-selected actions {#tool-contracts}

A useful contract identifies the operation, argument meaning, result meaning, errors and effects. Distinct names and bounded, informative results help the model choose and interpret tools; Anthropic describes evaluating these interface choices. [tool-design](https://www.anthropic.com/engineering/writing-tools-for-agents)

Schema-constrained output, illustrated by Gemini's structured-output support, constrains representation. It cannot establish that a selected account is the intended account or that a requested change is authorized. Check business invariants in execution code. [gemini-structured-output](https://ai.google.dev/gemini-api/docs/structured-output)

Recommended design separates transport failure, rejected input, failed operation and successful operation with an unexpected business outcome. Return actionable errors without leaking secrets. Preserve an operation identifier when a response is delayed or uncertain, so the caller can reconcile it.

## Choosing the action surface {#action-surfaces}

| Surface | Useful property | Engineering obligation |
| --- | --- | --- |
| Typed API | Explicit operation and data contract | Maintain schemas and authorization rules |
| Code or shell | Flexible composition and computation | Constrain filesystem, processes and network effects |
| Browser or GUI | Reach workflows without a suitable API | Observe state changes and recover from interface drift |

SWE-agent demonstrates that a purpose-built agent-computer interface affects coding performance in its studied environment. It does not establish one best surface for every task. [swe-agent](https://arxiv.org/abs/2405.15793)

Evaluate realistic sequences, including malformed calls, large results and ambiguous outcomes. Screenshots and text outputs are observations, not proof that the desired state persisted. Tool-result truncation should be visible, with a route to the remaining evidence.

## External integration {#external-integration}

[Interoperability](interoperability.md) addresses discovering and calling capabilities across implementations. Keep tool semantics independently testable even when a protocol transports them. Recovery of side effects belongs in [durable execution](../execution/durable-execution.md#side-effects); permission enforcement belongs in [isolation and authorization](../security/isolation-authorization.md).

## References {#references}

- [Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling) — `gemini-function-calling`.
- [Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output) — `gemini-structured-output`.
- [Writing effective tools for AI agents—using AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — `tool-design`.
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) — `swe-agent`.
