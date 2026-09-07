---
id: human-oversight
title: Human oversight
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- security
related:
- control-flow
- durable-execution
- evaluation-design
sources:
- langgraph-interrupts
- sandboxing
---

# Human oversight

Human oversight supplies missing intent, authorization or judgment and gives users a way to redirect or stop work. Useful oversight must preserve enough task state to continue correctly. LangGraph demonstrates persisted interrupts and explicit resume values, including replay constraints. [langgraph-interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

## Different reasons to pause {#pause-reasons}

| Reason | Information needed | Resume condition |
| --- | --- | --- |
| Clarification | A missing task requirement | Requirement is incorporated into task state |
| Approval | A concrete proposed effect | Authorized decision matches that effect |
| Escalation | Judgment beyond automated policy | Responsible person selects the next action |
| Cancellation | User wants execution to end | Stop new work and reconcile pending effects |

These are recommended interaction distinctions, not a requirement to ask about every reversible step. Use the authorization already supplied for the task. Anthropic's sandboxing account identifies repeated permission prompts as a source of approval fatigue, motivating explicit boundaries within which work can proceed. [sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)

## Make decisions reviewable {#reviewable-decisions}

Show the target, proposed change, important consequences and unresolved uncertainty. An approval for one recipient, amount or artifact version should not cover a materially different operation after a long pause. Revalidate relevant state and authority before executing.

For example, an agent can prepare a draft message and show its recipient and content before sending. If resumed after the recipient changes, the earlier decision no longer describes the pending effect. Keep the decision associated with the operation record, not only with a free-form chat sentence.

## Continuation and user control {#continuation}

Persist what was approved, denied or clarified, and surface whether work is active, waiting or finished. Avoid treating lack of a response as consent. Let the user inspect completed artifacts and remaining obligations.

Cancellation is not automatic rollback: [durable execution](../execution/durable-execution.md) owns reconciliation of in-flight effects. Evaluate whether users can understand and correct a proposal, whether interruption loses constraints, and how often unnecessary prompts prevent progress. The mechanics of pause and resume are core; an optimal threshold for requesting human judgment depends on task impact and measured error rates.

## References {#references}

- [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — `langgraph-interrupts`.
- [Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing) — `sandboxing`.
