# Bootstrap research and editorial synthesis

This is research memory, not canonical evidence. Reviewed on 2026-09-07.

## Starting state and discovery

The repository had only knowledge/index.md, an uninitialized taxonomy, empty source registries and no bootstrap changelog. The working tree was clean. Research examined primary specifications, technical documentation, engineering accounts and research abstracts. Paper abstracts support only the narrow method/findings descriptions used here; this was not a full-paper systematic review or benchmark replication.

Discovery covered control loops, task definitions, harness/runtime boundaries, context selection, retrieval, memory, procedure packaging, tool interfaces, remote integration, coordination, security, evaluation, telemetry and resource control. Bibliographic dates are original publication/submission dates where verified, not a claim that the retrieved body is unchanged since publication. Mutable documentation is scoped to its verification date. The MCP tools source is explicitly revision 2025-11-25; no claim that this is the latest protocol revision is made.

The 30 canonical sources and their claim scope are recorded in sources.jsonl. seen.jsonl additionally records three watchlist sources and one unreadable article redirect. Search snippets for incidental leads were discovery only; selected sources were retrieved or their primary research abstracts examined. No forum or social-media claim is used as evidence.

## Candidate map before materialization

Durable questions emerged before directories: who decides the next action; what state survives; what information informs a decision; how operations expose effects; which authority bounds them; and what establishes successful work. These support five domains rather than vendor or framework sections.

- Containment: plans, stopping and failure transitions belong inside control flow; memory representations inside persistent memory; compaction inside working context; sandbox mechanisms inside isolation.
- Specialization: tool and remote task protocols specialize external integration but have different semantics; the accepted interoperability page keeps separate sections.
- Dependency: coordination depends on context, persistence and budgets; memory depends on retrieval and access control. These become links rather than repeated pages.
- Terminology: agent/harness/runtime have overlapping industry meanings. The glossary supplies working definitions without claiming standardization. RAG is not a synonym for all grounding; tool calls are not remote task handoffs; model-visible context is not checkpoint state.
- Maturity: established engineering problems enter core with bounded claims. Authored procedural packaging enters emerging. Open-ended self-modification and universal telemetry portability remain evaluated watch hypotheses.

See the [candidate tree](2026-09-07-candidate-taxonomy.md) for the pre-review proposal and the [independent critique](2026-09-07-taxonomy-review.md) for structural findings.

## Review decisions

Accepted the separation between retained memory and authored procedures; made task contracts and environment/artifact lifecycle explicit; placed deployment and rollback in assurance; assigned replay safety to durable execution, retry eligibility to control flow, error representation to action, and budget ceilings to resource budgets.

Retained reusable procedures as a standalone emerging page because discovery, activation, versioning and evaluation have their own lifecycle and multiple incoming conceptual links. Evidence for packaging is narrow, so no universal host equivalence or adoption claim is made. Retained interoperability as a substantive boundary page with distinct tool and remote-task sections, not separate protocol catalog pages.

Changed coordination and interoperability from proposed emerging labels to core with medium confidence. Their durable trade-offs are established enough for an engineering baseline; autonomous topology selection and arbitrary cross-runtime collaboration are explicitly unsettled. Domain indexes are substantive parent syntheses; an asymmetric action domain with one deeper child is intentional, not an empty one-child navigation wrapper.

## Limits and deferred coverage

Evidence is weighted toward publicly documented software agents, especially coding and research, with support-workflow evidence from tau-bench. Physical robotics, model-training algorithms, detailed serving infrastructure and domain-specific regulation are outside this lean bootstrap's developed coverage. No universal model ranking, price claim, production reliability percentage, adoption count or industry consensus is inferred.

The multi-agent sources have different task scopes and are not a controlled comparison. Older papers motivate design questions without implying their numerical performance applies to current models. Protocol conformance, safe authorization and useful task execution are separate claims. These boundaries should guide later updates and expansion rather than creating placeholder canonical pages now.
