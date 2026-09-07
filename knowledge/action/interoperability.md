---
id: interoperability
title: Interoperability
status: core
last_verified: '2026-09-07'
confidence: medium
tags:
- action
related:
- multi-agent-coordination
- isolation-authorization
- durable-execution
sources:
- mcp-tools-2025-11-25
- a2a-spec
---

# Interoperability

Interoperability lets independently implemented components discover capabilities and exchange requests and results. A compatible message format is only one layer: task meaning, authorization and recovery still need agreements. This page treats the boundary as core while identifying protocol-specific and cross-runtime behavior as evolving.

## Tool and resource boundary {#tool-boundary}

MCP's reviewed 2025-11-25 tools specification defines listing and calling tools, input and optional output schemas, and protocol versus tool-execution errors. It also says annotations from untrusted servers must be treated as untrusted. A claimed read-only annotation is therefore not a substitute for enforced permissions. [mcp-tools-2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)

Use a protocol adapter when independent clients and servers need a shared integration contract. A direct in-process function can be simpler when both sides share a release lifecycle. An adapter adds capability negotiation, version handling and remote failure modes; it does not eliminate application-specific semantics.

## Remote task boundary {#remote-task-boundary}

A2A specifies discovery through Agent Cards and exchanges involving tasks, messages and artifacts. This concerns delegation to a remote agent, rather than merely exposing an individual tool. A remote task can still call tools internally. [a2a-spec](https://a2a-protocol.org/latest/specification/)

Recommended integration contracts define who owns task completion, what an accepted request means, which artifacts are authoritative, and how to handle cancellation or reconnection. A remote success status should be checked against the requested deliverable. Local [coordination](../execution/multi-agent-coordination.md) remains responsible for integrating results.

## Compatibility is layered {#compatibility}

Test schema support, capability changes, unsupported operations, duplicate requests and interrupted delivery. Bind identity and authority to the correct caller and resource; forwarding a request must not silently widen access. Pin a supported protocol revision and record optional capabilities rather than assuming a mutable latest document matches a deployed server.

The specifications establish concrete contracts, not broad evidence that arbitrary agents can collaborate successfully. Portability of procedures, memory, authorization and task semantics is not claimed here. Preserve these distinctions when evaluating a framework's interoperability claims.

## References {#references}

- [MCP tools specification, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) — `mcp-tools-2025-11-25`.
- [Agent2Agent protocol specification](https://a2a-protocol.org/latest/specification/) — `a2a-spec`.
