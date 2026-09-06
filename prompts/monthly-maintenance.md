# Monthly Knowledge Maintenance

## Goal

Improve the internal quality of the current knowledge base. This is primarily
an internal consistency, freshness, and structural review, not simply a larger
weekly news scan.

## Mandatory context

Read:

- AGENTS.md;
- every file under _meta/;
- the complete knowledge/ tree;
- references/sources.jsonl;
- recent references/seen.jsonl;
- all active watchlist entries;
- the previous month's changelogs;
- the previous month's weekly reports.

## Step 1 — Audit freshness

Identify important pages not recently verified, high-confidence claims resting
on weak or old evidence, changed practical meanings, terminology drift, and
references that no longer support current wording. Re-research important
claims. Do not update last_verified merely because a file was opened.

## Step 2 — Audit consistency

Search for contradictions, inconsistent terminology, duplicate explanations,
mismatched maturity/confidence labels, stale cross-links, orphan concepts, and
sources referenced by pages but missing from the registry.

## Step 3 — Audit structure

Critically review taxonomy and page boundaries. Ask whether concepts should
merge or split, whether a category is historical terminology, whether a durable
domain is missing, whether the hierarchy is awkward or too deep, and whether
vendor vocabulary leaked into the canonical structure.

Refactor only when a material improvement is justified.

## Step 4 — Audit obsolescence

Identify claims, sections, and pages to rewrite, merge, deprecate, or remove
from current prose. Do not preserve outdated explanations solely for history.

## Step 5 — Audit the watchlist

For each active item, choose keep watching, promote to emerging, merge into an
existing concept, promote directly to core only with unusually strong evidence,
or remove because the signal did not develop. Record the reason.

## Step 6 — Audit provenance

Review important pages for primary-source coverage, dead or superseded
evidence, unsupported broad claims, overreliance on one vendor, and source
metadata quality.

## Step 7 — Refactor

Perform the minimum coherent set of changes needed to restore a clean current
knowledge model. Moving, merging, splitting, rewriting, renaming, and removing
pages are allowed when justified. Preserve stable page IDs when semantically
correct.

## Step 8 — Update governance metadata

Update taxonomy, glossary, frontmatter, references, watchlist, and changelog as
required by the refactor. Do not change the charter or editorial principles
unless explicitly requested by the owner.

## Step 9 — Validate

Run repository checks and the Docusaurus production build:

    npm --prefix website ci
    npm --prefix website run build

Fix broken links, metadata, version assumptions, and rendering regressions.

## Step 10 — Release readiness

Determine whether the post-maintenance state is suitable for a monthly release.
Recommend a YYYY.MM name, but do not publish or create a frozen version before
the maintenance changes are reviewed and merged unless explicitly instructed.

Weekly reports are historical publications, not canonical knowledge or
evidence. Do not rewrite old reports merely because canonical understanding
has changed. Use canonical pages and the source registry for maintenance
decisions.

## Final output

Report stale content reviewed, revised/merged/split/deprecated/removed pages,
taxonomy changes, watchlist decisions, provenance improvements, unresolved
uncertainty, validation status, and recommended release name.

Do not merge directly to main.
