---
id: durable-execution
title: Durable execution
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- execution
related:
- persistent-memory
- human-oversight
- observability
- isolation-authorization
sources:
- langgraph-persistence
- safe-retries
- langgraph-interrupts
- long-running-harnesses
---

# Durable execution

Durable execution preserves enough state to resume a task after interruption. LangGraph distinguishes thread checkpoints from cross-thread stores and notes that in-memory checkpointers do not survive process restart. A saved conversation is only one part of recovery. [langgraph-persistence](https://docs.langchain.com/oss/python/langgraph/persistence)

## Recovery boundaries {#recovery-boundaries}

A recovery design should identify the next runnable step, completed observations, pending actions and artifact versions. Checkpoint frequency trades write overhead against repeated work. Snapshotting after each meaningful boundary is easier to reason about than persisting arbitrary execution stacks, but any work between checkpoints may run again.

An engineering acceptance test is to terminate the worker after an external action succeeds but before its result is recorded. On restart, the system must reconcile the outcome rather than assume the action never happened.

## Side effects {#side-effects}

AWS describes caller-supplied request identifiers and atomic deduplication for idempotent APIs. Reuse the operation identity for the same logical request; a fresh identity can produce another effect. This is a service contract, not a property obtained merely by checkpointing the agent. [safe-retries](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

LangGraph resumes interrupted nodes by reexecuting them, so effects before an interrupt may repeat. Separate approval from effect execution and understand the runtime's replay boundary. [langgraph-interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)

Where a tool lacks deduplication, use an observable operation record or reconcile external state before retrying. Compensation is a new action with its own possible failures; it does not erase a sent message or guarantee transaction rollback.

## Handover across context windows {#long-horizon-handover}

Anthropic's coding harness uses incremental work, progress records and environment checks to orient subsequent sessions. This supports retaining verifiable artifacts and unfinished obligations beyond a model window, not a claim of unlimited autonomous reliability. [long-running-harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

Recommended handover records include task constraints, artifact locations, checks already run, unresolved outcomes and the next useful step. Recheck mutable external state. Version persisted state alongside compatible execution code. On cancellation, stop new dispatches and record which in-flight effects remain uncertain; consult [human oversight](../security/human-oversight.md) for the user-facing decision.

## References {#references}

- [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — `langgraph-persistence`.
- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — `safe-retries`.
- [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — `langgraph-interrupts`.
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — `long-running-harnesses`.
