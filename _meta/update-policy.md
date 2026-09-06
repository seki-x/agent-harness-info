# Update and Maintenance Policy

## Lifecycle

The knowledge system has four operational modes:

1. Bootstrap — one-time initialization.
2. Weekly update — external change detection.
3. Monthly maintenance — internal consistency and refactoring.
4. Release — publication of a stable knowledge snapshot.

Bootstrap, weekly update, and monthly maintenance have separate prompts under
prompts/.

## Weekly update

Recommended cadence: once per week, Saturday morning, Asia/Tokyo.

The weekly process asks:

    What new evidence since the previous successful scan is sufficient to change
    the current knowledge state?

It is not a weekly-news-writing task.

Each successful weekly cycle also publishes a concise reader-facing report,
including quiet weeks with no canonical change. A report explains what was
examined and what is worth knowing; it is not canonical knowledge, evidence,
or a substitute for the semantic changelog.

Each meaningful candidate is classified as one of:

- NO_OP
- REFERENCE_ONLY
- WATCH
- ADD
- UPDATE
- DEPRECATE
- RESTRUCTURE

NO_OP means duplicate, irrelevant, weak, or not materially useful.
REFERENCE_ONLY means useful evidence without a prose change.
WATCH means potentially important but not yet canonical.
ADD means a distinct durable concept enters canonical knowledge.
UPDATE means existing understanding changes.
DEPRECATE means existing understanding is materially obsolete.
RESTRUCTURE means taxonomy or page boundaries no longer represent the field.

## Monthly maintenance

Recommended cadence: once per month, after at least one weekly cycle.

Monthly maintenance audits stale claims, contradictions, duplicated concepts,
weak provenance, orphaned pages, taxonomy drift, over-fragmentation, obsolete
terminology, watchlist decisions, unjustified confidence, outdated references,
and vendor-specific framing.

It may perform larger refactors than a weekly update.

## Pull request policy

- bootstrap: PR required;
- weekly content changes: PR required;
- monthly maintenance: PR required;
- taxonomy changes: PR required;
- deprecation/deletion: PR required;
- releases: human-triggered after maintenance is accepted;
- translations: PR required.

Do not allow autonomous direct pushes to main.

The candidate-intake workflow is not a content update. It may only validate,
label, comment on, and close GitHub Issues; it has no repository write
permission. Processing results, weekly reports, and run metadata remain part
of the reviewed weekly PR.

## Release policy

Git commits preserve exact engineering history. Knowledge releases preserve
human-meaningful snapshots. The recommended release cadence is monthly after
maintenance is merged, using a YYYY.MM label such as 2026.09.

A YYYY.MM Git tag identifies the authoritative stable release. A release may
also include an optional GitHub Release and a derived Docusaurus documentation
snapshot. The website should default to the latest stable snapshot while
keeping the accepted, unreleased current state available when practical. Do
not create a Docusaurus version for every commit or weekly update.

Weekly reports are published independently of monthly knowledge releases.
They should identify the stable release used as their baseline and clearly
distinguish released knowledge from accepted but unreleased changes.

## Translation policy

Translations are derived only after canonical changes are accepted into main.
They must preserve frontmatter keys, IDs, URLs, code blocks, explicit heading
IDs, and canonical terms from glossary.yaml. Translation must never silently
change canonical knowledge.
