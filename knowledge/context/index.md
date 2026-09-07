---
id: context
title: Context and memory
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- context
related:
- execution
- security
- resource-budgets
sources:
- context-engineering
- lost-in-middle
sidebar_position: 1
---

# Context and memory

Context engineering manages the information available to a model at each decision. Instructions are one input alongside task state, tool definitions, retrieved material and prior observations. Anthropic's engineering account describes selective loading and compaction as ways to manage this changing working set. [context-engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## Three kinds of state {#state-boundaries}

| State | Main purpose | Primary home |
| --- | --- | --- |
| Working context | Inform the next model invocation | This page |
| Durable task state | Resume execution and reconcile effects | [Durable execution](../execution/durable-execution.md) |
| Persistent memory | Reuse retained knowledge across interactions | [Persistent memory](persistent-memory.md) |

The same fact may appear in all three, but their correctness conditions differ. A summary can be useful context while being insufficient to replay an operation. A database entry can be durable while irrelevant to the current task.

## Assembly and compaction {#assembly-and-compaction}

Recommended assembly preserves the current objective, applicable instructions, unresolved constraints and evidence needed for the next action. Label external content by origin. A retrieved instruction-shaped document does not acquire authority merely by entering the prompt.

Compaction reduces accumulated history to a smaller representation. It can discard exact values, qualifications and failed attempts. Keep authoritative artifacts addressable outside the summary, and verify them before consequential action. Test resumed tasks that depend on an early correction, not just whether the summary sounds complete.

## Capacity is not effective use {#capacity-and-effective-use}

Lost in the Middle found position-sensitive retrieval and question-answering performance in the models it tested. That motivates testing information placement and distractors; it does not establish the same curve for every current model. [lost-in-middle](https://arxiv.org/abs/2307.03172)

Loading more content costs tokens and can make relevance harder to inspect; aggressive selection risks excluding a necessary dependency. Choose a measured balance. [Retrieval](retrieval-grounding.md) handles finding evidence; [authored procedures](reusable-procedures.md) handle reusable task guidance. Neither requires putting every available document into every invocation.

## References {#references}

- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — `context-engineering`.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — `lost-in-middle`.
