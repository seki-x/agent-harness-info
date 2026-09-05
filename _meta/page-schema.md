# Knowledge Page Schema

Every canonical page under knowledge/ must begin with YAML frontmatter.

## Required fields

    ---
    id: stable-kebab-case-id
    title: Human-readable title
    status: core
    last_verified: "YYYY-MM-DD"
    confidence: high
    tags: []
    related: []
    sources: []
    ---

## Field rules

- id: stable, unique, lowercase kebab-case identifier.
- title: human-readable canonical page title.
- status: one of core, emerging, or deprecated.
- last_verified: ISO date; update only after material claims are reviewed.
- confidence: one of high, medium, or low; it describes confidence in the
  synthesis, not popularity.
- tags: required array, possibly empty.
- related: required array of canonical page IDs, possibly empty.
- sources: required array of IDs present in references/sources.jsonl.

Optional Docusaurus-compatible fields include description, slug, and
sidebar_position.

## Recommended body shape

Use sections appropriate to the concept. A useful default is:

    # Title

    Brief current synthesis.

    ## Why it matters {#why-it-matters}

    ...

    ## Current understanding {#current-understanding}

    ...

    ## Design space {#design-space}

    ...

    ## Trade-offs {#trade-offs}

    ...

    ## Related concepts {#related-concepts}

    ...

    ## References {#references}

    ...

Use explicit heading IDs for durable cross-page and translated links. Do not
turn pages into chronological update logs.
