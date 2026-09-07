---
id: persistent-memory
title: Persistent memory
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- context
related:
- retrieval-grounding
- durable-execution
- isolation-authorization
sources:
- langgraph-memory
- reflexion
---

# Persistent memory

Persistent memory retains information for future interactions. Its defining concern is a managed lifecycle of retained knowledge, not a particular vector database or the current prompt length. LangChain distinguishes thread-scoped state from cross-thread memory and discusses profiles, collections, and synchronous or background updates. [langgraph-memory](https://docs.langchain.com/oss/python/concepts/memory)

## Scope and representation {#scope-and-representation}

Decide whether a memory belongs to a user, project, organization or task before choosing storage. A compact profile makes selected facts easy to inspect; a collection supports narrower records but needs reconciliation and retrieval. Neither representation automatically resolves contradictions.

Semantic, episodic and procedural are useful labels for facts, experiences and retained ways of doing work. They are descriptive categories, not separate required services. **Authored procedures** have a distinct lifecycle in [reusable procedures](reusable-procedures.md): a reviewed instruction package is not interchangeable with a model's inferred lesson.

## Writes and forgetting {#writes-and-forgetting}

Recommended memory records carry origin, scope, confidence or review status, and a way to update or remove them. Separate an explicit user preference from an agent inference. For example, one request for a terse answer should not silently become an organization-wide communication policy.

Writing before answering makes a memory immediately available but adds latency and exposes the request to write failures. Background processing decouples this work, requiring a freshness policy. Test conflicting updates and deletion propagation through caches and retrieval indexes.

## Learning without weight updates {#feedback-memory}

Reflexion retains textual feedback between trials without updating model parameters. It supports a narrow distinction between experience-conditioned behavior and model training; it does not validate arbitrary self-generated memories as accurate or transferable. [reflexion](https://arxiv.org/abs/2303.11366)

Evaluate whether retained information improves subsequent tasks and whether incorrect memories persist. More stored history is not itself better memory. The lifecycle and access-control problem is core; autonomous selection, consolidation and generalization of experience remain unsettled. Recovery checkpoints are owned by [durable execution](../execution/durable-execution.md), even when an implementation calls them short-term memory.

## References {#references}

- [Memory overview](https://docs.langchain.com/oss/python/concepts/memory) — `langgraph-memory`.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — `reflexion`.
