# Missing Feature List

This list is the canonical next-feature queue for the two-prompt loop.

Each row is intended to be one branch and one PR. Keep the scope narrow enough that the build prompt can finish it, and the QA prompt can verify it without extra context.

| Rank | Status | Feature | Merge Unit | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | open | Corpus index | Render the validated corpus as a browsable starting point | Browser smoke test and screenshot | First user-facing slice should make the repo contents visible before deeper interactions. |
| 2 | open | Profile detail view | Show one technology profile with metadata, citations, and references | Browser deep-link test and screenshot | Keep the detail page read-only until the corpus view is stable. |
| 3 | open | Search and filter | Filter profiles by domain, confidence, status, or tag | Browser interaction test and screenshot | This should be a thin query layer over the corpus, not a new data model. |
| 4 | open | Validation status panel | Surface compiler and repo validation state to users | Explicit non-UI verification plus browser check if rendered | Useful as a bridge between repo truth and the visible surface. |
| 5 | open | Diffusion view | Visualize T10-T75 progress and completion state | Browser chart test and screenshot | Only after the data slice is stable enough to render. |
| 6 | open | Dependency view | Make substrate dependencies easier to inspect | Browser graph test or explicit export check | Keep the first version simple; do not build a full graph platform too early. |
| 7 | open | Export/download | Provide a way to export the current corpus slice | Explicit non-UI verification | This is the safest non-UI feature if the browser surface stalls. |

## Selection Rule

Always pick the first open item that can be completed without widening the branch beyond one feature. If a feature needs additional scaffolding, split the scaffolding into a separate PR and keep this list updated.
