# Weekly Knowledge Update

## Goal

Determine whether new external evidence since the previous successful update
materially changes the current knowledge state. This is not a weekly news
summary. A successful run may make no canonical changes.

## Mandatory context

Read:

- AGENTS.md;
- every file under _meta/;
- relevant knowledge/ pages;
- references/README.md;
- recent references/seen.jsonl;
- references/sources.jsonl;
- relevant watchlist/ entries;
- the latest changelog.

Follow all repository policies.

## Step 1 — Establish the research window

Find the latest successful weekly update from repository history or changelog.
Research developments after that point, while allowing older sources when they
are newly relevant.

## Step 2 — Discover candidate evidence

Search broadly enough to detect meaningful changes in architecture, agent
runtimes, context handling, tools, state and memory, orchestration,
long-running execution, environments, permissions, security, evaluation,
observability, human interaction, existing taxonomy domains, and genuinely new
domains.

Prefer primary evidence.

## Step 3 — Deduplicate

Compare candidates against references/seen.jsonl, references/sources.jsonl,
existing canonical knowledge, and watchlist entries. Do not repeatedly
rediscover the same source as new.

## Step 4 — Classify every meaningful candidate

Classify each candidate as exactly one of:

- NO_OP
- REFERENCE_ONLY
- WATCH
- ADD
- UPDATE
- DEPRECATE
- RESTRUCTURE

Ask whether it materially alters engineering understanding, whether evidence is
strong and independent, whether it is vendor-specific, and whether an existing
page is the right conceptual home.

## Step 5 — Update research memory

Record every meaningful examined source in references/seen.jsonl, including
important NO_OP decisions. Add accepted evidence to references/sources.jsonl.
Do not duplicate stable source IDs.

## Step 6 — Update the watchlist

For WATCH candidates, create or update an entry explaining why it may matter,
the current evidence, what would justify promotion, and what would justify
removal. Review existing watchlist items affected by this week's evidence.

## Step 7 — Modify canonical knowledge only when justified

For ADD, UPDATE, DEPRECATE, or RESTRUCTURE, edit the current knowledge
coherently. Prefer rewriting over appending a dated news paragraph. Remove
obsolete language and update related pages, metadata, taxonomy, and sources as
needed.

For REFERENCE_ONLY, avoid prose changes unless provenance materially improves.

## Step 8 — Check cross-page consequences

Search for related claims after every semantic change. Resolve contradictions,
old terminology, broken relationships, and stale duplicate explanations.

## Step 9 — Write the weekly changelog

Create changelog/YYYY-Www.md or update the appropriate current weekly file.
Record meaningful canonical changes, watchlist changes, structural changes,
strongest evidence, and important investigations that intentionally caused no
canonical change. Keep it concise.

## Step 10 — Validate

Validate JSONL, local links, and metadata as far as repository tooling permits.
Run:

    npm --prefix website ci
    npm --prefix website run build

If no lockfile exists, use npm install instead of npm ci. Fix failures caused
by the update.

## Step 11 — Review the diff

Check for novelty bias, overreaction to one source, vendor bias, accidental
taxonomy churn, unsupported confidence, duplicated prose, and incidental
website changes.

## Final output

Produce a PR-ready summary containing research window, source count,
classification counts, changed pages, watchlist changes, structural changes,
major evidence, uncertainty, and validation results.

If no semantic update is justified, say so clearly. Do not invent changes.
Do not merge directly to main.
