# Living Agent Knowledge

A Git-versioned, AI-maintained knowledge base for AI Agent and Agent Harness
engineering.

The system maintains a current knowledge state rather than a chronological
news archive.

## Architecture

    External evidence
          ↓
    Codex research / reasoning
          ↓
    Governance policies
          ↓
    knowledge/               ← canonical current state
          │
          ├── references/    ← provenance and research memory
          ├── watchlist/     ← not-yet-canonical ideas
          ├── changelog/     ← semantic history
          ├── reports/       ← reader-facing weekly briefs
          ├── runs/          ← weekly automation metadata
          │
          └── Docusaurus
                 ↓
            Cloudflare Pages

## Source of truth

knowledge/ is canonical. The website is a projection, translations are
derived, and Docusaurus release snapshots are frozen publication states. Git
remains the exact historical record.

Research exports in the repository root are input material only; they are not
canonical knowledge or evidence registry entries.

GitHub Issues labeled `candidate:pending` are the unreviewed research inbox.
They are evaluated during the next weekly cycle and become processed only after
the corresponding weekly pull request is merged.

## Repository governance

Agents must follow:

    AGENTS.md
    _meta/charter.md
    _meta/editorial-policy.md
    _meta/update-policy.md
    _meta/page-schema.md

Task-specific runbooks live under prompts/.

## Lifecycle

### Bootstrap

Run manually once:

    prompts/bootstrap.md

Bootstrap researches the field before defining taxonomy, builds and critiques
the initial knowledge state, initializes provenance/watchlist/glossary, and
produces a reviewable pull request.

### Weekly update

Recommended cadence: Saturday at 09:00 Asia/Tokyo.

Configure a Codex scheduled task with:

    Read and execute prompts/weekly-update.md in this repository.

The weekly process asks whether new evidence materially changes the current
knowledge state. It also publishes a concise report under `reports/weekly/`. A
no-change run is valid and still produces a report.

### Monthly maintenance

Recommended cadence: the first day of each month at 10:00 Asia/Tokyo.

Configure a Codex scheduled task with:

    Read and execute prompts/monthly-maintenance.md in this repository.

Monthly work audits freshness, consistency, redundancy, taxonomy, watchlist
state, and provenance.

## Pull request policy

Semantic changes follow:

    AI change → pull request → review → merge

Never push semantic knowledge changes directly to main. Translation starts
PR-only as well.

## Local website

Before bootstrap, knowledge/ contains only the structural landing page and no
initialized domain taxonomy. The site can still be built and previewed:

    npm --prefix website install
    npm --prefix website run start

Production check:

    npm --prefix website run build

After website/package-lock.json exists, prefer npm --prefix website ci.

## Translation

Translation is disabled by default. The canonical source is knowledge/;
derived localized content belongs under:

    website/i18n/<locale>/docusaurus-plugin-content-docs/current/

Before enabling translation, implement scripts/translate.mjs, configure
DEEPL_AUTH_KEY, set ENABLE_TRANSLATION=true, enable target locales, and verify
a localized production build.

## Deployment

The intended presentation flow is:

    Docusaurus → Cloudflare Pages

See website/CLOUDFLARE.md for setup.

## Initial setup checklist

1. Commit this skeleton.
2. Configure GitHub branch/ruleset protection for main when the repository plan
   supports it.
3. Run bootstrap with local Codex and the Node.js version in .nvmrc.
4. Enable the internet access needed for research.
5. Verify local `gh` authentication before enabling candidate processing.
6. Review and merge the bootstrap pull request.
7. Connect Cloudflare Pages.
8. Create weekly and monthly Codex scheduled tasks.
9. Review the first several automated runs closely.

## Design principle

The presentation layer may adapt to the knowledge system. The knowledge system
must not adapt merely to presentation constraints.
