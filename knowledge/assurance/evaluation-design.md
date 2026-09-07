---
id: evaluation-design
title: Evaluation design
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- assurance
related:
- control-flow
- retrieval-grounding
- human-oversight
sources:
- agent-evals
- tau-bench
- browsecomp
- agentdojo
---

# Evaluation design

Agent evaluation measures whether an interaction reaches the intended outcome under specified conditions. It must account for environment changes and variable trajectories. tau-bench compares final database state with task goals; this illustrates why a final assistant message is not enough to grade an action-taking system. [tau-bench](https://arxiv.org/abs/2406.12045)

## Tasks and graders {#tasks-and-graders}

Define initial state, allowed actions, expected outcomes and relevant constraints. Reset mutable environments between trials. Keep test fixtures and graders outside the agent's writable task artifacts when possible; otherwise an apparent improvement may be a changed test rather than improved work.

Code-based checks work for objective properties; model-based judges accommodate more open-ended criteria but require calibration; human reviewers help establish ambiguous expectations. Anthropic documents these trade-offs. Combine checks according to the product contract rather than forcing one grader to decide everything. [agent-evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## Reliability over trials {#repeated-trials}

Distinguish **pass@k**, success at least once in k attempts, from **pass^k**, success in every one of k trials. The latter addresses consistency emphasized by tau-bench. Report the number of trials, environment and budget; do not compare a many-attempt score with first-attempt reliability. [agent-evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) [tau-bench](https://arxiv.org/abs/2406.12045)

Useful checks include task outcome, prohibited effects and unnecessary effort. Avoid requiring an exact trajectory unless that order is part of the requirement: multiple valid approaches may exist.

## Validity and transfer {#validity}

BrowseComp intentionally emphasizes difficult search with short verifiable answers and does not capture every real user-query requirement. AgentDojo targets adversarial tool interaction, a different dimension. Neither benchmark alone covers an application's behavior. [browsecomp](https://arxiv.org/abs/2504.12516) [agentdojo](https://arxiv.org/abs/2406.13352)

Recommended practice separates development tasks from held-out assessment, investigates possible answer leakage, and records infrastructure failures apart from model errors. Use production failures to improve coverage without silently tuning on the only test set. Validate disagreement between graders before interpreting small score changes.

Evaluation principles are core; any measured result remains conditional on task distribution, model and harness versions, grader quality and execution budget.

## References {#references}

- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — `agent-evals`.
- [tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — `tau-bench`.
- [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516) — `browsecomp`.
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) — `agentdojo`.
