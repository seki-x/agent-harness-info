---
id: isolation-authorization
title: Isolation and authorization
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- security
related:
- action
- persistent-memory
- durable-execution
sources:
- sandboxing
- mcp-security
---

# Isolation and authorization

Isolation limits what execution can reach. Authorization decides which principal may perform which operation on which resource. They complement one another: code can stay inside a sandbox and still misuse an overprivileged API credential.

## Execution boundaries {#execution-boundaries}

Anthropic describes filesystem and network restrictions and a credential proxy in its coding-agent sandbox design. This is a concrete enforcement example. Its effectiveness depends on configuration and the operations still allowed; sandboxing does not establish that an agent's business decisions are correct. [sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)

As a design practice, enumerate readable and writable paths, outbound destinations, executable capabilities and resource limits. Apply restrictions to spawned processes as well as the initial command. Separate temporary workspaces from retained artifacts and verify cleanup between tenants. A container boundary and an application permission check solve different problems.

## Identity and delegated authority {#delegated-authority}

MCP's security guidance addresses token passthrough, confused-deputy risks and scope minimization. Authenticate the caller, validate the intended token audience, and authorize the resource operation; session identifiers should not substitute for these controls. [mcp-security](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices)

Recommended credential handling keeps broad secrets outside model-visible context and narrows downstream authority where possible. A proxy can mediate operations, but it becomes part of the trusted enforcement path and needs its own tests. Avoid giving a worker broader access simply because the parent has it.

## Verify the boundary, not its label {#boundary-validation}

For a document-editing agent, test allowed project edits, denied sibling-project reads, denied outbound destinations and revocation during a run. Also test an allowed endpoint receiving data it should not receive: network allowlisting alone cannot distinguish every legitimate payload from an unauthorized one.

Inspect tool packages and executable dependencies under the same authority model. Human approval may permit an operation within policy, but should not silently rewrite permanent access rules. Durable recovery must recheck current authority when resuming work after permissions change.

The enforcement concepts are established. Specific mechanisms differ by operating system, hosting model and remote service; this page does not prescribe one universal isolation technology.

## References {#references}

- [Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing) — `sandboxing`.
- [MCP security best practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices) — `mcp-security`.
