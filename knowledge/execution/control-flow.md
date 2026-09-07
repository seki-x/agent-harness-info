---
id: control-flow
title: Control flow
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- execution
related:
- action
- human-oversight
- resource-budgets
- evaluation-design
sources:
- react
- building-agents
- reflexion
---

# Control flow

Control flow decides what happens next, what evidence changes the plan, and when the task ends. It can mix fixed code paths with model-selected actions. ReAct provides primary evidence for alternating reasoning and environmental actions; it does not establish that one visible reasoning format is required for every agent. [react](https://arxiv.org/abs/2210.03629)

## Fixed and adaptive control {#fixed-and-adaptive-control}

A fixed workflow can enforce an order such as retrieve, draft, validate and publish. An adaptive loop can decide which evidence to retrieve or which repair to attempt. Routing, parallel branches and evaluator feedback are composable approaches documented by Anthropic, rather than mutually exclusive architectures. [building-agents](https://www.anthropic.com/engineering/building-effective-agents)

Choose fixed transitions when the next step follows from known conditions. Delegate a transition to the model when the required action depends on interpretation that cannot usefully be enumerated. This is an editorial decision rule: evaluate the extra flexibility against the additional latency and failure paths on the intended task set.

## Plans, feedback and completion {#plans-and-completion}

Keep a plan as revisable task state. For example, a migration plan may discover another dependent service after inspection; completing its original checklist would not satisfy the expanded dependency evidence. Require outcome checks independent of the agent's completion message.

Feedback loops can retain error observations and change the next attempt. Reflexion studies retained textual feedback without changing model weights; those results support an approach to test, not a guarantee that self-critique improves arbitrary tasks. [reflexion](https://arxiv.org/abs/2303.11366)

## Failure transitions {#failure-transitions}

Recommended control policy distinguishes invalid arguments, denied authority, unavailable dependencies and an uncertain operation outcome. Correct arguments when evidence identifies the error; escalate a missing permission rather than repeatedly requesting the same forbidden action. A transient fault may justify a retry, subject to [side-effect safety](durable-execution.md#side-effects) and a [budget](../assurance/resource-budgets.md).

Represent completed, failed, waiting for input, cancelled and budget-exhausted outcomes distinctly. Repeated identical observations should trigger reassessment. A turn limit provides a termination boundary; it is not evidence that the requested result was achieved.

## References {#references}

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — `react`.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — `building-agents`.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — `reflexion`.
