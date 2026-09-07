---
id: reusable-procedures
title: Reusable procedures
status: emerging
last_verified: '2026-09-07'
confidence: medium
tags:
- context
related:
- action
- persistent-memory
- isolation-authorization
- evaluation-design
sources:
- agent-skills
---

# Reusable procedures

Reusable procedures package deliberately authored instructions and supporting resources for repeated tasks. They solve a context distribution and maintenance problem: keeping specialized guidance available without placing all of it in every prompt. This page is emerging because the cross-runtime packaging and activation contract remains less established than ordinary instruction reuse.

## Packaging and discovery {#packaging-and-discovery}

The Agent Skills specification describes a required `SKILL.md`, metadata, and optional scripts, references and assets. Its loading model progressively exposes metadata, activated instructions and supporting resources. This is evidence for a concrete format, not proof that every host selects or follows the same package identically. [agent-skills](https://agentskills.io/specification)

A useful package boundary is a repeatable task with recognizable triggers, inputs and expected outputs. A title alone is inadequate discovery metadata. Conversely, placing an entire organizational handbook in one package makes activation broad and review difficult. Keep subordinate reference details addressable and document dependencies.

## Procedure, tool and memory {#procedure-tool-memory}

A procedure tells an agent how to perform work; a tool executes an operation. A package can include executable helpers, but loading its instructions does not authorize those helpers to access data or change systems. A remembered lesson can become a procedure after deliberate review; automatic retention and authored publication remain separate decisions.

## Versioning and evaluation {#versioning-and-evaluation}

Recommended practice records the package version used for a task, reviews executable resources, and tests activation as well as results. Include negative cases where similar wording should not activate the package. Test precedence conflicts against the host's instruction policy instead of assuming the format defines that policy.

For example, an export procedure can specify the expected workbook structure and a verification command. Its test should check the produced workbook and dependencies, rather than merely whether the agent read `SKILL.md`.

Progressive loading reduces initial context but can miss guidance through poor discovery. Eager loading makes instructions visible but adds irrelevant material. The balance and portability require evaluation in each host; this bootstrap makes no universal adoption or safety claim.

## References {#references}

- [Agent Skills specification](https://agentskills.io/specification) — `agent-skills`.
