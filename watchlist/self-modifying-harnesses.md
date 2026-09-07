# Open-ended self-modifying harnesses

First seen: 2026-09-07
Last reviewed: 2026-09-07
Status: watching

## Why it may matter

A system that proposes changes to its own tools or control code could automate part of harness improvement. The relevant question is whether improvements transfer beyond the optimization benchmark while preserving enforceable constraints.

## Evidence

The [Darwin Godel Machine paper](https://arxiv.org/abs/2505.22954) describes generating modified coding agents, retaining an archive and evaluating changes on coding benchmarks. The reviewed abstract also reports sandboxing and human oversight. This is credible experimental evidence, not established production reliability. Research record: `seen-dgm` in [seen.jsonl](../references/seen.jsonl).

## What would justify promotion

Independent replications with held-out tasks, full compute accounting, regression analysis, and evidence that authority boundaries survive agent-generated modifications. A stable distinction from ordinary offline configuration search would help justify a standalone canonical treatment.

## What would justify removal

If gains are explained by benchmark-specific optimization, do not survive independent evaluation, or the idea is adequately covered as ordinary evaluated harness development, merge the useful evidence into [evaluation and operations](../knowledge/assurance/index.md) and retire this separate candidate.
