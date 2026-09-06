# Research Run Metadata

This directory stores non-canonical, machine-readable metadata for completed
research runs. It is an automation control surface, not knowledge, evidence,
or a reader-facing publication.

Each successful weekly run creates `runs/weekly/YYYY-Www.json`. The record
links the weekly report to candidate Issues evaluated by that run. A
post-merge workflow uses the trusted record on `main` to move those Issues from
`candidate:pending` to `candidate:processed`.

Run records must not contain credentials, raw fetched documents, or private
data beyond the referenced repository Issue numbers.
