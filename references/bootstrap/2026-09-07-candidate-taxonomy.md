# Candidate conceptual tree, 2026-09-07

Proposed nodes below are conceptual, not a fixed page count. Each domain has a substantive overview; named children are proposed standalone concepts. Items in parentheses are H2/H3 sections, not peer pages. Non-hierarchical dependencies use cross-links.

- Execution and control [domain + substantive overview: agent/model/harness/environment boundary]
  - Control flow [page: workflows, adaptive loops, plans, stopping and completion checks]
  - Durable execution [page: checkpointing, replay, side-effect recovery, long-horizon task handover, deployment lifecycle]
  - Multi-agent coordination [emerging page: decomposition, delegation, handoff, shared artifact ownership]
- Context and memory [domain + substantive overview: model-visible working set, instruction assembly, compaction]
  - Retrieval and grounding [page: indexed retrieval, iterative search, evidence attribution]
  - Persistent memory [page: scope, write policies, provenance, forgetting; semantic/episodic/procedural as sections]
  - Reusable procedural context [emerging page: skill packages, discovery, versioning, loading; Agent Skills as example]
- Action and integration [domain + substantive overview: tool contracts, schemas, errors, API versus code/browser surfaces]
  - Interoperability [emerging page: tool/resource protocol boundary, remote task delegation boundary; MCP and A2A as examples]
- Security and human control [domain + substantive overview: threat model, indirect prompt injection, trust boundaries]
  - Isolation and authorization [page: execution sandbox, filesystem/network access, credentials, tenant boundaries]
  - Human oversight [page: approval, clarification, interruption, cancellation and escalation]
- Evaluation and operations [domain + substantive overview: outcome requirements, offline/online feedback, release decisions]
  - Evaluation design [page: task environments, graders, repeated trials, benchmark limitations]
  - Observability [page: traces, outcome correlation, data minimization, telemetry conventions]
  - Resource budgets [page: model selection, latency/cost, timeouts/backoff, bounded concurrency]

Watchlist candidates outside the tree: open-ended self-modifying harnesses (Darwin Godel Machine); universal portable agent telemetry schema (OpenTelemetry GenAI convention movement, no stable interoperability claim).

Cross-links: coordination -> context, recovery, budgets; memory -> retrieval, authorization; tools -> authorization, recovery; oversight -> recovery; skills -> context and security; interoperability -> coordination and authorization; evaluation -> all design decisions.
