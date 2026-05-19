# Diffusion Backfill Swarm Plan

This plan describes how to use subagents or agent swarms to finish the T10/T25/T50/T75 backfills without losing methodological control.

## Goal

Keep a repeatable protocol for diffusion backfill decisions by dividing research across parallel agents, then routing every proposed edit through a single integration and QA path. The initial 15-profile backfill queue has been adjudicated; use this plan for future new profiles or revised milestone series.

The expected output for each assigned profile is one of two outcomes:

- filled milestone fields with sourced, defensible `t10_years`, `t25_years`, `t50_years`, and `t75_years`
- an explicit documented deferral explaining why no stable single series supports the thresholds yet

## Non-Negotiable Rules

- Use `STANDARDS_MEMO.md` section 7 as the diffusion methodology.
- Use one canonical time series for all thresholds unless the sources explicitly reconcile the series.
- Use first observed threshold crossing; do not interpolate sparse data.
- Store `t*_years` as years since `us_commercial_launch_year`, not calendar years.
- Add or update numbered references in the affected profile.
- Edit source profiles first, then regenerate `data/processed/substrates_master.csv` with `python scripts/compile_profiles.py`.
- Do not hand-edit the generated CSV.

## Recommended Swarm Shape

Use a coordinator plus four research agents and one QA/adjudication agent.

| Role | Assignment | Output |
| --- | --- | --- |
| Coordinator | Owns branch strategy, conflict control, integration, CSV regeneration, and final validation | One merged branch per feature row or one integration branch after independent research patches |
| Agent A: Public/household infrastructure | `modern_hospital_systems`, `public_health_surveillance`, `water_filtration_and_chlorination`, `radio` | Proposed profile edits or documented deferrals |
| Agent B: Materials and fuels | `bessemer_steel`, `oil_refining`, `portland_cement_concrete` | Proposed profile edits or documented deferrals |
| Agent C: Power and transport work | `internal_combustion_engine`, `nuclear_power`, `freight_trucking`, `pipelines` | Proposed profile edits or documented deferrals |
| Agent D: Compute and networks | `fiber_optics`, `microprocessors`, `semiconductors` | Proposed profile edits or documented deferrals |
| QA Agent | Reviews all proposed backfills for source quality, denominator stability, arithmetic, and schema validity | Accept/reject notes before integration |

## Parallel Work Protocol

1. Coordinator creates one feature branch from the first open backfill row in `missing-features.md`.
2. Coordinator assigns disjoint profile sets to agents. No two agents edit the same profile.
3. Each research agent returns:
   - profile path
   - selected canonical series
   - source citation details
   - threshold calendar years
   - computed years since launch
   - exact metadata and note changes
   - any deferral rationale
4. QA agent checks methodology before integration.
5. Coordinator applies accepted edits, runs:
   - `python scripts/compile_profiles.py`
   - `python scripts/validate_repo.py`
   - `python scripts/compile_profiles.py --check`
6. Coordinator updates `missing-features.md`, `BACKLOG.md`, and `CURRENT_STATE.md` if coverage counts changed.

## Suggested Prompt For Research Agents

> You are assigned only these profiles: `<profile-list>`. Read `STANDARDS_MEMO.md` section 7, `SCHEMA.md`, and the assigned profile files. For each profile, find one defensible U.S. national time series for T10/T25/T50/T75 diffusion thresholds, or recommend an explicit deferral if the series is unstable. Return the selected series, references, threshold calendar years, computed years since launch, and exact proposed profile metadata/notes changes. Do not edit generated CSV output.

## Suggested Prompt For QA Agent

> Review the proposed diffusion backfills against `STANDARDS_MEMO.md` section 7. Check that each profile uses a stable single series, a denominator aligned with the metadata, first observed threshold crossings, correct arithmetic from `us_commercial_launch_year`, and numbered references. Flag any row that should remain blank rather than forcing a weak proxy.

## Integration Strategy

Prefer one PR per feature row in `missing-features.md`. If running a larger swarm, collect research outputs in notes first, then integrate only one cohort per branch to keep review small.

Do not start UI features until at least one of these is true:

- all 24 profiles have complete or explicitly deferred milestone decisions
- the repo has a diffusion coverage report that makes the incomplete state visible and intentional
