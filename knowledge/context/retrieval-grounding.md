---
id: retrieval-grounding
title: Retrieval and grounding
status: core
last_verified: '2026-09-07'
confidence: high
tags:
- context
related:
- action
- persistent-memory
- evaluation-design
- security
sources:
- rag
- context-engineering
- browsecomp
---

# Retrieval and grounding

Retrieval brings external evidence into a task; grounding ties a claim or action to that evidence. They are related but distinct: finding a relevant document does not establish that it supports the answer. The original RAG paper demonstrates combining a learned generator with retrieved non-parametric information in specific NLP tasks. Modern retrieval designs need not reproduce that architecture. [rag](https://arxiv.org/abs/2005.11401)

## Selecting a retrieval strategy {#retrieval-strategy}

An indexed retriever provides repeatable access to a curated corpus, with index maintenance and access filtering obligations. Iterative tool-driven search lets the agent revise queries based on what it finds, adding latency and opportunities to pursue irrelevant leads. Anthropic describes selective runtime loading and hybrid approaches. [context-engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

As an engineering choice, use exact lookup for known identifiers, lexical search for distinctive strings, and semantic retrieval where paraphrase matters. Compare strategies on representative missing-evidence and ambiguous-query cases rather than assuming one retrieval mechanism is universally sufficient.

## Evidence handling {#evidence-handling}

Preserve source identity, retrieval time and the passage or artifact supporting a material claim. Distinguish an original source from another page repeating it. Apply access controls before exposing results to the model, and treat retrieved content as untrusted data.

For example, a policy answer requires the applicable version and jurisdiction or business scope; a highly similar obsolete policy is still the wrong evidence. When sources disagree, narrow the claim, expose the uncertainty, or obtain additional evidence. Do not resolve contradictions solely from retrieval rank.

## Evaluate retrieval and answer quality separately {#evaluation}

Check whether needed evidence was found, whether it was available to the model, and whether the final claim follows from it. A citation's presence is not proof of entailment. BrowseComp measures persistent search for difficult but verifiable answers while explicitly leaving out parts of realistic user-query handling. Its results cannot alone establish the quality of a research report. [browsecomp](https://arxiv.org/abs/2504.12516)

The established principle is external evidence access with attribution. The best mix of indexing and agentic exploration remains task- and corpus-dependent.

## References {#references}

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — `rag`.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — `context-engineering`.
- [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516) — `browsecomp`.
