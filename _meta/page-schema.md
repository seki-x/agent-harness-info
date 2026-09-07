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
- related: required array of canonical page IDs, possibly empty. It represents
  non-hierarchical cross-links, not parent/child structure.
- sources: required array of IDs present in references/sources.jsonl.

Optional Docusaurus-compatible fields include description, slug, and
sidebar_position.

## Semantic hierarchy

Page structure must follow the structure of the concept rather than
mechanically flattening content into a standard template.

- Use H1 for the canonical page concept.
- Use H2 for major child concepts, mechanisms, dimensions, or design choices.
- Use H3 for meaningful subdivisions, approaches, or variants within an H2.
- Avoid H4 and deeper headings unless the subject genuinely requires them.

Heading depth must express real conceptual containment or decomposition, not
visual indentation. Conversely, do not represent genuine parent/child concepts
as peer headings merely to keep the outline shallow.

## Page boundaries

Not every knowledge node requires its own page. Create a standalone canonical
page when the concept can be understood and referenced independently, requires
substantial explanation, has its own meaningful design space or trade-offs, is
likely to evolve independently, or is meaningfully referenced from several
parts of the taxonomy.

Keep a concept as an H2/H3 section of its parent when it is mainly a component,
subtype, implementation approach, local trade-off, or small detail whose
separation would create a thin page. When a child becomes a standalone page,
retain a short synthesis and link in the parent instead of duplicating the full
explanation.

A substantive parent concept with independently useful child pages should be a
navigation group. Its `index.md` may be a full canonical synthesis rather than
a thin directory introduction; the child pages provide the deeper treatments.

Each standalone page has one primary home in the navigation hierarchy. Use
`related` links for cross-cutting relationships rather than duplicating the
page under multiple domains.

## Common editorial shape

Use sections appropriate to the concept. The following is a useful default,
not a required flat template. Combine, nest, rename, or omit sections when the
concept's natural structure requires it.

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
