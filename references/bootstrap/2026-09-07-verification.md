# Bootstrap Step 9 independent verification

Reviewed 2026-09-07. Read-only review of canonical content; no repository files changed.

## Result

No confirmed blocking defect found. The current structure is suitable for bootstrap review, subject to the main agent's build, repository validation and final diff checks.

## Scope and findings

Read AGENTS.md, the governing charter/editorial/update policies, taxonomy, glossary, page schema, bootstrap prompt, all 18 canonical Markdown pages, both source registries, watch entries and bootstrap changelog. Reviewed the research synthesis after independently inspecting the completed content.

- Taxonomy has five meaningful domains with substantive parent indexes. The action domain's one child is justified: knowledge/action/index.md:25 owns tool contracts and action surfaces, while knowledge/action/interoperability.md:22 and :28 own independent integration contracts. This is not an empty single-child wrapper.
- Recovery, memory and context boundaries remain clear. knowledge/context/index.md:23 distinguishes working context, durable task state and retained knowledge; knowledge/execution/durable-execution.md:25 owns recovery boundaries. No duplicate canonical home found.
- Reusable procedures has an independent authoring, discovery and versioning lifecycle at knowledge/context/reusable-procedures.md:22, :28 and :32. Its emerging label and limited evidence are explained at :20 and :24. A standalone page is defensible despite one format source.
- Coordination's core/medium labels are qualified at knowledge/execution/multi-agent-coordination.md:21; contrary engineering accounts are explicitly scoped at :25. Interoperability similarly limits core maturity to the problem boundary at knowledge/action/interoperability.md:20, and rejects arbitrary collaboration/portability claims at :38. No maturity contradiction found with the two watch entries.
- Recommendations are generally distinguished from empirical findings. Historical benchmark results are not converted into universal current performance claims. No unsupported numerical/adoption/industry-consensus claim found.
- Independent Python inspection found 18 unique page IDs, 17 core pages including the structural index, one emerging page, 30 source records and 34 seen records. Every related ID resolves; every source reference and used_by membership is reciprocal; every canonical source has a matching seen URL. Checked Markdown local paths and explicit target anchors across knowledge/, watchlist/ and changelog/: no failures.

## Primary-source spot verification

Retrieved these primary sources independently; no mismatch was found in the corresponding narrow claims:

- SWE-agent abstract and submission history: https://arxiv.org/abs/2405.15793 — interface effect and 2024-05-06 date match references/sources.jsonl:17 and knowledge/action/index.md.
- BrowseComp abstract: https://arxiv.org/abs/2504.12516 — hard search, short verifiable answers, and limited realistic-query coverage support knowledge/assurance/evaluation-design.md and knowledge/context/retrieval-grounding.md.
- Anthropic sandboxing account: https://www.anthropic.com/engineering/claude-code-sandboxing — filesystem/network restrictions, approval fatigue and cloud Git credential proxy support the narrow summaries; canonical text does not repeat the source's absolute security assurances.
- Anthropic eval account: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — 2026-01-09 date, outcome-versus-transcript distinction, graders and complete-system evaluation agree.
- Managed Agents account: https://www.anthropic.com/engineering/managed-agents — 2026-04-08 date, session/harness/sandbox decomposition and model-specific context-reset example agree with knowledge/execution/index.md and knowledge/assurance/index.md.
- Agent Skills: https://agentskills.io/specification — required entry file, optional directories and progressive disclosure agree with knowledge/context/reusable-procedures.md:24.
- LangGraph persistence: https://docs.langchain.com/oss/python/langgraph/persistence — checkpoint/store scope and RAM checkpoint loss on restart agree with knowledge/execution/durable-execution.md:23.
- MCP security guidance: https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices — token audience/passthrough, confused deputy and scope guidance support knowledge/security/isolation-authorization.md.

These URLs already occur in seen.jsonl; no new research lead was introduced by the spot checks.

## Non-blocking maintenance opportunity

references/sources.jsonl:21 and knowledge/action/interoperability.md:30 use A2A's mutable latest URL. The record explicitly discloses this and provides a verification date, so it does not violate current governance or make the narrow claim false. Capturing a reviewed revision or commit in future source notes would improve reproducibility as the specification evolves. This is optional, not a required bootstrap correction.

## Limits

This was a semantic and structural audit plus targeted source re-retrieval, not an independent reproduction of every original research run or benchmark. Research coverage is weighted toward software agents, and that limitation is disclosed. The main agent owns the production build, full validation and secret/diff review.

## Main-agent completion checks

- `python3 scripts/validate-data.py`: passed.
- Additional read-only validation: 18 page frontmatters, 17 taxonomy nodes, 30 canonical sources, 34 examined records, unique IDs, related IDs and reciprocal source usage passed; 39 local Markdown links and explicit anchors resolved.
- `npm --prefix website ci`: passed with the existing lockfile using local Node 22.17.0. The installer reported 27 audit findings (9 moderate, 18 high); dependency versions were not changed by this bootstrap.
- `npm --prefix website run build`: passed, including after category metadata was added. The build's new-file update-date warning reflects files not yet committed at build time, not a broken route.
- Generated root navigation inspected: entry page followed by the five domain titles in taxonomy order. Autogenerated sidebars remain in use.
- Final diff reviewed: changes confined to canonical knowledge, taxonomy/glossary, provenance, watchlist and changelog. No translations, frozen snapshots, dependency changes or credential patterns were introduced.
