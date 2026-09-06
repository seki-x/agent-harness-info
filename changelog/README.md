# Changelog

This directory records human-readable semantic evolution of the knowledge base.
Git is the exact file history; the changelog explains why the knowledge state
changed.

## Naming

Weekly:

    YYYY-Www.md

Monthly maintenance may append to a weekly file or create:

    YYYY-MM-maintenance.md

## Suggested format

    # YYYY-Www

    ## Summary

    Brief description of meaningful change.

    ## Canonical changes

    ### Updated

    - page-id: what changed and why.

    ### Added

    - page-id: why the concept now belongs in canonical knowledge.

    ### Deprecated or removed

    - page-id: why the previous understanding is no longer appropriate.

    ## Watchlist

    - Added:
    - Promoted:
    - Removed:

    ## Structural changes

    Taxonomy/page-boundary changes, if any.

    ## Evidence

    Most important new source IDs.

    ## No-change findings

    Important topics investigated that did not justify a knowledge change.

Do not copy weekly news into the changelog. Record semantic changes to the
knowledge model.

## Changelog versus weekly report

The changelog records semantic changes to the knowledge model. A weekly report
is a reader-facing summary of the research cycle and may discuss important
WATCH or NO_OP findings even when canonical knowledge did not change. Do not
expand the changelog into a general weekly briefing.
