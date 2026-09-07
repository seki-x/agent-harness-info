# Bootstrap the Living Knowledge Base

## Goal

Create the first high-quality canonical knowledge state for this repository.
This is a one-time initialization task. Do not assume the final taxonomy
before research and do not optimize for page count.

## Mandatory context

Read these files before doing anything else:

- AGENTS.md
- _meta/charter.md
- _meta/editorial-policy.md
- _meta/update-policy.md
- _meta/taxonomy.yaml
- _meta/glossary.yaml
- _meta/page-schema.md
- references/README.md
- watchlist/README.md
- changelog/README.md

Treat those files as governing instructions.

## Step 1 — Inspect the repository

Confirm that:

- knowledge/ contains at most the structural index page and no initialized
  domain taxonomy;
- _meta/taxonomy.yaml is uninitialized;
- no prior bootstrap changelog exists.

Do not overwrite an already initialized knowledge base unless explicitly
instructed to re-bootstrap it.

## Step 2 — Broad discovery

Research the current state of AI Agent and Agent Harness engineering. Map the
problem space, recurring engineering problems, major architectural decisions,
terminology conflicts, mature areas, emerging areas, and relationships.

Do not create the final taxonomy yet. Prefer primary sources and direct
technical evidence. Use social/discussion sources only to discover leads unless
stronger evidence is unavailable and uncertainty is recorded.

Record examined sources in references/seen.jsonl and evidence selected for
canonical use in references/sources.jsonl.

## Step 3 — Synthesize the problem space

Create an internal candidate map answering:

- What durable engineering problems does the field solve?
- Which concepts are genuinely distinct?
- Which terms are aliases or overlapping concepts?
- Which relationships are containment, specialization, dependency, or mere
  association?
- Which distinctions are vendor vocabulary rather than durable concepts?
- Which topics are mature enough for canonical knowledge?
- Which belong only in the watchlist?

Do not modify knowledge/ yet.

Do not represent containment or specialization merely as flat sibling topics.
Dependency and association normally become cross-links rather than ownership
in the primary hierarchy.

## Step 4 — Propose the taxonomy

Before deciding filesystem layout or page count, build a recursive conceptual
tree organized primarily by problem domain, not by vendor or framework.
Preserve genuine parent/child relationships. For each candidate node, decide
whether it should be represented as:

1. a navigation group, subdomain, or substantive parent concept with children;
2. a standalone leaf canonical page;
3. a section within a parent page; or
4. a cross-link only.

Check that categories have meaningful boundaries, survive vendor churn, and
support cross-links. Do not default every discovered concept to a peer page.
An excessively flat taxonomy is as undesirable as an unnecessarily deep one.
Treat the preferred navigation depth in _meta/taxonomy.yaml as guidance, not a
hard limit when the subject genuinely requires another level.

## Step 5 — Critique the taxonomy

Prefer assigning this critique to a fresh-context subagent when the execution
environment supports subagents. Give it the governing repository files and the
candidate taxonomy, but do not preload it with the main agent's rationale or
conclusions. Ask it to act as a critical reviewer and look for missing domains,
overlaps, duplicated concepts, artificial distinctions, current-trend bias,
vendor/framework bias, categories likely to age badly, and premature
formalization of unstable terminology. Ask specifically whether genuine
parent/child concepts have been flattened into peers, whether sibling pages
should be sections of a parent, whether any page is too thin or too broad, and
whether filesystem convenience has distorted the concept tree. Treat its
findings as review input, not as automatically authoritative decisions.

If a fresh-context subagent is unavailable, perform the same review explicitly
from an independent-reviewer perspective. Do not skip or weaken this step.

Revise until the structure is coherent enough to serve as version 0.1. Only
then update _meta/taxonomy.yaml, set status to initialized, and record the
initialization date.

## Step 6 — Build the initial knowledge state

Populate knowledge/ using _meta/page-schema.md. Use quality rather than page
count as the stopping criterion. A lean first version is preferred; roughly
15–30 substantive pages may be reasonable if research supports them.

Materialize the accepted primary navigation hierarchy under knowledge/. Use
directories for durable domains and subdomains, Markdown files for standalone
concepts, and H2/H3 headings for subordinate concepts that do not justify
independent pages. A group whose node is itself a substantive parent concept
should use `index.md` for its canonical synthesis, with child pages providing
deeper treatments. Each page must have one primary home; represent cross-domain
relationships with links rather than duplicate pages. Keep the filesystem close
enough to the conceptual navigation tree that Docusaurus autogenerated sidebars
expose a useful hierarchy without manually maintained sidebar rules.

For every page:

- synthesize the current state, not a chronological history;
- explain why the concept matters;
- explain the main design space and meaningful trade-offs;
- link related concepts;
- cite evidence;
- distinguish established from emerging understanding;
- use explicit heading IDs for stable anchors.

Do not create pages merely to mention individual products. Products and
frameworks may appear as implementation examples inside durable concept pages.

## Step 7 — Initialize emerging knowledge

Place potentially important but insufficiently established ideas in watchlist/.
Do not promote them merely to make the initial wiki appear comprehensive.

## Step 8 — Normalize terminology

Populate _meta/glossary.yaml with terminology that needs stable canonical
wording. Mark product names, protocol names, acronyms, and technical terms
that should not be machine-translated where appropriate.

## Step 9 — Verify the whole knowledge base

Prefer assigning verification to a fresh-context subagent when available. Give
it the governing repository files and the completed knowledge-base state, but
do not provide a narrative that presumes the implementation is correct. Ask it
to independently check taxonomy coherence, duplicated concepts, contradictory
claims, unsupported broad claims, missing provenance, broken local links,
frontmatter, source IDs, maturity labels, page IDs, relationships, excessive
flattening or depth, and incorrect page/section boundaries.

The main agent remains responsible for evaluating the findings and fixing
confirmed issues. If a fresh-context subagent is unavailable, run the same
checks from an independent-verifier perspective. Do not skip or weaken this
step.

## Step 10 — Create the bootstrap changelog

Create a changelog entry describing the initial problem-space model, chosen
taxonomy, major editorial boundaries, emerging/watchlist areas, and major
uncertainties. Do not turn it into a source dump.

## Step 11 — Validate presentation

Run repository validation and the Docusaurus production build. If no lockfile
exists, run:

    npm --prefix website install
    npm --prefix website run build

Commit website/package-lock.json. Fix rendering, frontmatter, and link errors.

## Step 12 — Final review

Review the entire diff and confirm that canonical knowledge is under
knowledge/, presentation concerns did not distort taxonomy, sources are real,
no credentials were committed, and the change is suitable for one bootstrap PR.

## Final output

Provide a concise PR-ready summary containing research scope, taxonomy summary,
canonical page count, core/emerging count, watchlist count, source count, major
uncertainties, and validation results.

Do not merge directly to main.
