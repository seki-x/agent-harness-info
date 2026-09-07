# Universal portable agent telemetry semantics

First seen: 2026-09-07
Last reviewed: 2026-09-07
Status: watching

## Why it may matter

A common meaning for agent, tool, task and usage events could reduce instrumentation adapters and make comparisons across harnesses more reliable. The watch item is universal semantic portability, not the value of ordinary tracing, which is already [canonical](../knowledge/assurance/observability.md).

## Evidence

The [OpenTelemetry migration notice](https://opentelemetry.io/docs/specs/semconv/gen-ai/) points to the [GenAI semantic-conventions repository](https://github.com/open-telemetry/semantic-conventions-genai). Its reviewed README covers GenAI clients, MCP and provider conventions; its schema-URL section is marked TODO. These observations motivate following concrete schema and compliance work, but do not prove cross-runtime portability. Research records: `seen-otel-genai-moved` and `seen-otel-genai-repo` in [seen.jsonl](../references/seen.jsonl).

## What would justify promotion

Versioned stability commitments for the relevant agent operations, usable migration guidance and multiple implementations demonstrating equivalent meanings for retries, delegation, usage and task outcomes. Promote the evidenced subset rather than claiming every field is stable together.

## What would justify removal

If the universal claim proves unnecessary or conventions remain implementation-specific, retain version-specific instrumentation advice in observability and remove this broader hypothesis.
