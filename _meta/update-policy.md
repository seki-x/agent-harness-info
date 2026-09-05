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

## Release policy

Git commits preserve exact engineering history. Knowledge releases preserve
human-meaningful snapshots. The recommended release cadence is monthly after
maintenance is merged, using a YYYY.MM label such as 2026.09.

A release may include a Git tag, optional GitHub Release, and Docusaurus
documentation snapshot. Do not create a Docusaurus version for every commit or
weekly update.

## Translation policy

Translations are derived only after canonical changes are accepted into main.
They must preserve frontmatter keys, IDs, URLs, code blocks, explicit heading
IDs, and canonical terms from glossary.yaml. Translation must never silently
change canonical knowledge.
