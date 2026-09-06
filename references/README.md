# References

This directory stores research provenance independently from canonical prose.

## seen.jsonl

Append one JSON object per source examined by a research run. A source may
appear here even when it does not enter canonical knowledge.

Suggested object:

    {"id":"seen-example","url":"https://example.invalid","title":"Example","publisher":"Example","published_at":null,"discovered_at":"YYYY-MM-DD","type":"unknown","topics":[],"decision":"NO_OP","reason":"Template only"}

For a source submitted through the candidate inbox, add the optional integer
field `candidate_issue` after the source was actually examined.

Allowed decision values:

- NO_OP
- REFERENCE_ONLY
- WATCH
- ADD
- UPDATE
- DEPRECATE
- RESTRUCTURE

## sources.jsonl

Contains evidence actually referenced by canonical knowledge.

Suggested object:

    {"id":"source-example","url":"https://example.invalid","title":"Example","publisher":"Example","published_at":null,"verified_at":"YYYY-MM-DD","type":"primary","topics":[],"used_by":[]}

used_by contains canonical knowledge page IDs.

## Rules

- One valid JSON object per non-empty line.
- IDs must be stable.
- Do not invent publication dates.
- Prefer canonical source URLs.
- Avoid duplicate entries for the same source.
- seen.jsonl is research memory.
- sources.jsonl is canonical provenance.

Submitting a candidate Issue does not create a `seen` or `sources` record. Add
it to `seen.jsonl` only after the linked source was actually retrieved and
evaluated. Add it to `sources.jsonl` only when it becomes usable canonical
evidence.
