---
id: multi-agent-coordination
title: Multi-agent coordination
status: core
last_verified: '2026-09-07'
confidence: medium
tags:
- execution
related:
- context
- durable-execution
- resource-budgets
- interoperability
sources:
- multi-agent-research
- coordination-caution
---

# Multi-agent coordination

Multi-agent coordination allocates work among model-driven workers and reconciles their outputs. Delegation is a usable engineering pattern; reliable autonomous decomposition and coordination remain sensitive to task coupling. The core label here applies to the design problem and trade-offs, not to a claim that multi-agent systems are generally preferable.

## When decomposition helps {#decomposition}

Anthropic reports benefits for research with multiple independent search directions and substantial token costs. Cognition argues that partial histories and conflicting implicit decisions make parallel construction fragile. These are differently scoped engineering reports, not a matched head-to-head experiment. [multi-agent-research](https://www.anthropic.com/engineering/multi-agent-research-system) [coordination-caution](https://cognition.com/blog/dont-build-multi-agents)

The synthesis is to assess independence before worker count. Gathering separate source dossiers is often easier to reconcile than having multiple workers change the same interface while its contract is unsettled. Model diversity or different role names alone does not establish independent evidence.

## Ownership and communication {#ownership-and-communication}

| Approach | Useful property | Main coordination obligation |
| --- | --- | --- |
| Coordinator with workers | One place integrates partial results | Coordinator must detect omissions and conflicting assumptions |
| Sequential handoff | Next owner can use previous decisions | Transfer constraints, artifacts and unresolved work |
| Shared workspace | Immediate access to common artifacts | Control concurrent writes and define final authority |

These are design options, not a ranking. A delegation contract should state scope, inputs, permitted effects, expected evidence and completion criteria. Give a worker the context required by its assignment and a way to obtain missing information. Summaries reduce transfer size but may omit decisive assumptions; preserve references to original evidence and artifacts.

## Integration is part of the task {#integration}

Reserve time and budget for checking outputs together. A worker's success message does not establish that the combined result satisfies the parent task. Handle late results, cancellation and failed workers explicitly. Require the integrating owner to resolve disagreements using evidence rather than majority vote alone.

Local workers and remote agents share coordination problems but differ in authority and visibility. [Interoperability](../action/interoperability.md#remote-task-boundary) covers the remote task boundary. Autonomous topology selection and open-ended teams remain unsettled; evaluate them against simpler control on equal task and resource budgets.

## References {#references}

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — `multi-agent-research`.
- [Don’t Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) — `coordination-caution`.
