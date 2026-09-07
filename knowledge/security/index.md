---
id: security
title: Security and human control
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- security
related:
- context
- action
- observability
sources:
- indirect-injection
- agentdojo
sidebar_position: 1
---

# Security and human control

Agent security controls what information can influence decisions and what those decisions can affect. The model may encounter adversarial content through otherwise legitimate work. Indirect prompt-injection research demonstrates attacks placed in retrieved data; AgentDojo evaluates tool-using agents under such attacks. [indirect-injection](https://arxiv.org/abs/2302.12173) [agentdojo](https://arxiv.org/abs/2406.13352)

## Threat model {#threat-model}

Identify the attacker-controlled surfaces, valuable data and available effect channels. Surfaces include documents, tool results and dependencies. An attacker may try to change the requested task, extract data or induce unauthorized actions. A tool being authenticated does not make every document it returns an instruction source.

Recommended design distinguishes user intent, trusted application policy, externally supplied evidence and model-generated proposals. Preserve those distinctions when summarizing or delegating; laundering hostile text through a summary does not make it trusted.

## Defense in depth {#defense-in-depth}

[Isolation and authorization](isolation-authorization.md) limit reachable effects. [Human oversight](human-oversight.md) supplies decisions where policy or task ambiguity requires them. Input handling and output checks can reduce exposure, but neither a warning prompt nor a model classifier should be treated as a complete authority boundary.

For example, a document-processing agent with both confidential-file access and unrestricted outbound requests has an exfiltration route even if its nominal task is read-only. Scope data access and destinations to the actual task, and validate the proposed operation before dispatch. This is an engineering threat-model inference, not a claim that any specific sandbox eliminates all attacks.

## Test usefulness and resistance {#security-evaluation}

A system that blocks every action can appear secure while being unusable. AgentDojo's environment motivates evaluating legitimate task completion alongside attack outcomes. [agentdojo](https://arxiv.org/abs/2406.13352)

Maintain adversarial cases that exercise the application's real trust boundaries, including retrieved content, persisted memory and tool output. Track false denials as well as unauthorized effects. The existence of prompt injection and the need for enforced boundaries are core; the effectiveness of a particular defense remains conditional on its threat model and evidence.

## References {#references}

- [Not what you have signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — `indirect-injection`.
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) — `agentdojo`.
