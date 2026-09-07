---
id: assurance
title: Evaluation and operations
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- assurance
related:
- execution
- security
sources:
- agent-evals
- managed-agents
sidebar_position: 1
---

# Evaluation and operations

Evaluation and operations connect intended outcomes to evidence about a running system. A plausible demonstration is not enough to choose a harness or approve a change. Anthropic's evaluation account distinguishes capability exploration from regression protection and connects automated testing with production feedback. [agent-evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## Define the system under test {#system-under-test}

Recommended evaluation records identify the model, instructions, tool versions, procedure packages, initial environment and resource policy. Changing any of these can change task behavior. Anthropic's managed-agent account gives a concrete example of model-specific scaffolding becoming unnecessary after a model change. [managed-agents](https://www.anthropic.com/engineering/managed-agents)

The practical implication is to compare complete configurations. A model leaderboard cannot isolate how a particular harness will behave with different tools, data and permissions.

## Three complementary questions {#measurement-boundaries}

[Evaluation design](evaluation-design.md) asks whether outcomes satisfy a task contract. [Observability](observability.md) reconstructs what occurred. [Resource budgets](resource-budgets.md) control how much time, computation and external activity a run may consume. Their data should connect through task identity without conflating successful transport, fluent output and successful work.

For a support agent, a fast response, a successful API request and a correct account resolution are three separate observations. Track the last one as the product outcome while retaining the others for diagnosis.

## Release and feedback lifecycle {#release-lifecycle}

As an editorial operating model, keep representative regression tasks, investigate failures, and add cases only after establishing what behavior should have occurred. Compare a proposed configuration against the accepted baseline. Use bounded rollout where production uncertainty remains and define a rollback decision before expanding exposure.

A rollback can restore code and configuration; it cannot undo every external action already taken. Coordinate deployment compatibility with persisted task state and retain enough provenance to identify affected runs. Production incidents should update evaluation coverage and, where necessary, tool or policy design.

The measurement loop is core. There is no universal success threshold across domains, and this bootstrap does not treat a benchmark score or vendor report as a production reliability guarantee.

## References {#references}

- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — `agent-evals`.
- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents) — `managed-agents`.
