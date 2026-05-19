# Missing Feature List

This list is the canonical next-feature queue for the two-prompt loop.

Each row is intended to be one branch and one PR. Keep the scope narrow enough that the build prompt can finish it, and the QA prompt can verify it without extra context.

## Current Product Gap

The repo's working product is the source-backed corpus plus compiler, not a dashboard. The highest-priority missing feature is completing the diffusion milestone backfill so the corpus can support comparative analysis.

Current diffusion coverage:

- 24 QA-passed profiles compile into `data/processed/substrates_master.csv`.
- 10 profiles have complete T10/T25/T50/T75 milestone fields.
- 13 profiles have explicit documented deferrals.
- 1 profile has a partial milestone backfill with remaining thresholds explicitly deferred.
- 0 QA-passed profiles still need milestone adjudication or an explicit documented deferral.

The two-prompt loop should handle backfills as data features before UI features. Each backfill branch must update source profiles first, regenerate the CSV with `python scripts/compile_profiles.py`, and verify with `python scripts/validate_repo.py` plus `python scripts/compile_profiles.py --check`.

| Rank | Status | Feature | Merge Unit | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | done | Diffusion backfill: direct public/household infrastructure | Backfilled `radio`; explicitly deferred `modern_hospital_systems`, `public_health_surveillance`, and `water_filtration_and_chlorination` | `python scripts/compile_profiles.py`; `python scripts/validate_repo.py`; `python scripts/compile_profiles.py --check` | Radio now uses household receiver ownership; the three public-health infrastructure profiles document why one stable population-denominator threshold series is not available. |
| 2 | done | Diffusion backfill: industrial materials and fuels | Explicitly deferred `bessemer_steel`, `oil_refining`, and `portland_cement_concrete` | `python scripts/compile_profiles.py`; `python scripts/validate_repo.py`; `python scripts/compile_profiles.py --check` | These profiles remain blank by design: Bessemer is superseded, refining capacity lacks a stable saturation denominator, and cement/concrete volume tracks cyclical construction demand. |
| 3 | done | Diffusion backfill: industrial power and transport work | Backfilled nuclear-power T10; explicitly deferred higher nuclear thresholds plus `internal_combustion_engine`, `freight_trucking`, `pipelines`, and `refrigerated_logistics_cold_chain` | `python scripts/compile_profiles.py`; `python scripts/validate_repo.py`; `python scripts/compile_profiles.py --check` | Nuclear has a stable generation-share series for T10; the other rows remain blank by design because their volume/work metrics do not yet have stable threshold denominators. |
| 4 | done | Diffusion backfill: compute and network substrates | Explicitly deferred `fiber_optics`, `microprocessors`, and `semiconductors` | `python scripts/compile_profiles.py`; `python scripts/validate_repo.py`; `python scripts/compile_profiles.py --check` | Fiber route-mile, backbone-traffic, and last-mile connection series do not form one stable denominator; microprocessor PC/device series narrow the substrate too far; semiconductor GDP exposure needs a reproducible BEA input-output method before thresholds are safe. |
| 5 | open | Diffusion coverage report | Add a generated or documented report showing which profiles have complete, partial, blank, or intentionally deferred diffusion milestones | Explicit non-UI verification command and validator check | This should make the 10/24 complete, 13/24 deferred, and 1/24 partial state discoverable without manually inspecting the CSV. |
| 6 | open | First comparative analysis artifact | Produce a small chart, notebook, or memo using only profiles with defensible complete milestones | Re-run analysis from command line and validate repo | Keep claims scoped to complete rows. Do not compare blanks or deferred rows as zeroes. |
| 7 | open | Dependency edge export | Generate a machine-readable edge list from `primary_dependencies` | Explicit export check and validator check | This is the first graph-friendly data artifact; no graph UI yet. |
| 8 | open | Corpus index | Render the validated corpus as a browsable starting point | Browser smoke test and screenshot | First user-facing slice should make the repo contents visible before deeper interactions. |
| 9 | open | Profile detail view | Show one technology profile with metadata, citations, and references | Browser deep-link test and screenshot | Keep the detail page read-only until the corpus view is stable. |
| 10 | open | Search and filter | Filter profiles by domain, confidence, status, or tag | Browser interaction test and screenshot | This should be a thin query layer over the corpus, not a new data model. |
| 11 | open | Validation status panel | Surface compiler and repo validation state to users | Explicit non-UI verification plus browser check if rendered | Useful as a bridge between repo truth and the visible surface. |
| 12 | open | Diffusion view | Visualize T10-T75 progress and completion state | Browser chart test and screenshot | Only after the data slice is stable enough to render. |
| 13 | open | Dependency view | Make substrate dependencies easier to inspect | Browser graph test or explicit export check | Keep the first version simple; do not build a full graph platform too early. |
| 14 | open | Export/download | Provide a way to export the current corpus slice | Explicit non-UI verification | This is the safest non-UI feature if the browser surface stalls. |

## Selection Rule

Always pick the first open item that can be completed without widening the branch beyond one feature. If a feature needs additional scaffolding, split the scaffolding into a separate PR and keep this list updated.

## Backfill Done Criteria

A diffusion backfill feature is complete only when:

- each assigned profile either has defensible integer values for every reachable milestone or explicitly documents why milestones remain blank
- the profile's `Diffusion Milestones` section or `notes` field names the exact source series and caveat
- every new milestone claim is supported by a numbered reference in that profile
- `data/processed/substrates_master.csv` is regenerated by the compiler, not edited by hand
- validation passes locally
