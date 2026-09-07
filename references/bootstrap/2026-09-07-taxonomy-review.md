# Independent taxonomy review

Reviewed the governing files, bootstrap prompt, and candidate tree. This is a structural critique, not independent validation of the candidate's source evidence.

**Verdict:** The five problem domains are coherent enough for a lean initial knowledge base. They are vendor-neutral and need no additional top-level domain. Accept only after clarifying the boundaries below; neither a target page count nor navigation symmetry should determine additions.

## Changes recommended before materialization

1. **Separate reusable instructions from learned memory.** “Persistent memory” includes procedural memory while “Reusable procedural context” covers skill packages, creating apparent sibling duplication. Define memory as retained experience/state with write, update, retrieval, and deletion policies; define reusable procedural context as deliberately authored, versioned task instructions and supporting resources. Explain that learned procedures can be promoted into authored packages without making the two identical. If evidence supports only a particular packaging format, keep reusable procedures as an H2 in the context overview rather than manufacturing a separate emerging page.

2. **Limit durable execution to persistence and resumption semantics.** “Deployment lifecycle” is too broad for that page. Keep checkpointing, replay, idempotency, external side effects, checkpoint compatibility, and recovery there. Put release gates, deployment/rollback, and production feedback in the evaluation-and-operations overview. Long-horizon handover belongs here only when it means persisted resumable state; delegation between agents belongs in coordination. Cancellation has a user-control policy in oversight and execution cleanup semantics in durable execution, joined by links rather than repeated explanation.

3. **Make the tool-contract design space substantive and discoverable.** The action overview currently bears most of its domain while its only child is interoperability. It must cover capability discovery, argument/output validation, execution errors versus task failure, side effects, and API/code/browser environment feedback as real sections. Protocol interoperability specializes external integration and can remain a child if it has substantial independent trade-offs. If it is merely MCP/A2A summaries, fold it into an interoperability H2 instead. Do not split pages just to give this directory more children.

4. **Do not imply that tool access and delegated tasks are the same protocol boundary.** In interoperability, tool/resource exposure and remote task delegation should be distinct subordinate sections; link delegated task lifecycle back to coordination. A common protocol cannot by itself imply portable authorization, semantics, state, or successful handoff. No additional vendor/protocol pages are warranted.

5. **Clarify state ownership across context and execution.** The context overview should explicitly distinguish model-visible working context, durable application/task state, and cross-task memory. Compaction belongs under working-context management; checkpoints under durable execution; retained knowledge under persistent memory. This prevents “memory” from becoming a catch-all and keeps genuine containment intact.

6. **Give failure handling an explicit home.** The proposal mentions errors, recovery, timeouts, and backoff in scattered locations. Put retry eligibility and transient/permanent failure handling in control flow; external side-effect safety in durable execution; protocol error contracts in action; retry budget ceilings in resource budgets. Explain the boundaries once and cross-link. Resource budgets should govern ceilings and allocation, not become a second reliability page.

## Missing coverage to add as sections, not domains

- **Task specification and success criteria:** inputs, constraints, allowed actions, ambiguous goals, output contracts, and completion evidence in the execution/control overview or control-flow page. Link to evaluation's independently defined success criteria and to oversight's clarification mechanism.
- **Environment and artifact lifecycle:** workspace initialization, artifact ownership, reproducibility and cleanup under execution; sandbox enforcement under isolation. This is particularly important for code/browser agents but does not justify modality-specific domains.
- **Security beyond isolation:** data/tool-output trust, exfiltration routes, output validation, and defense in depth in the security overview; authorization needs least privilege and scope, not merely an approval UI.
- **Evaluation validity and feedback:** contamination/leakage, grader validity, regression sets, nondeterminism, and online monitoring in evaluation design/operations. Observability is measurement infrastructure, not evidence of correctness on its own.

## Maturity and hierarchy cautions

- An entire coordination page marked emerging may confuse the established engineering problem with newer autonomous coordination designs. Likewise, interoperability is a durable problem even if particular agent protocols are evolving. Set page status from the actual synthesis and explicitly distinguish established mechanisms from unsettled approaches inside it; do not assign maturity solely from a fashionable label.
- Persistent-memory subtypes correctly remain sections. Plans and stopping correctly remain subordinate to control flow. No current relationship demands another directory layer.
- Retrieval spans working context and persistent memory; its independent page plus links is appropriate. Do not nest all retrieval under memory.
- Domain indexes must explain the parent design problem and child boundaries, not repeat each leaf's full treatment. The five substantive overviews are defensible; they are not a reason to generate five template pages with identical headings.
- There is no evident filesystem distortion yet. Preserve the conceptual tree when materializing it, and accept asymmetry. The preferred navigation depth must not flatten future meaningful specializations.

**Proposed version 0.1 shape:** Retain the five domains and existing leaves, conditionally retaining reusable procedural context and interoperability only if their evidence and independent substance justify pages. Apply the ownership changes above. Do not add pages solely for these findings. Record the distinction between established problems and emerging implementations in the bootstrap changelog.
