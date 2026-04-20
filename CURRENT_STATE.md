# Current State (March 11, 2026)

This document provides an objective snapshot of the repository's current state, distinguishing confirmed facts from inferred intent or stale documentation.

## Confirmed Working

- **Repository Scaffold:** The folder structure is stable and passes `scripts/validate_repo.sh`.
- **Core Methodology:** Inclusion rules and research standards are documented in `STANDARDS_MEMO.md` and applied across the profile set.
- **Profile Corpus:** 25 technology profiles exist in `research/profiles/`.
- **Validation Status:** 24 of these profiles have the status `qa_passed` in their metadata.
- **Compiler Script:** `scripts/compile_profiles.py` is fully functional. It correctly parses markdown metadata, enforces dependency ordering, and regenerates the master CSV.
- **Master Dataset:** `data/processed/substrates_master.csv` contains 24 validated rows, in sync with the profile metadata.
- **Agent Prompts:** Starter prompts for all four domains plus a QA adjudicator are available in `research/prompts/`.

## Unverified or Partially Complete

- **Diffusion Milestones:** The `t10_years` through `t75_years` fields are mostly empty across the profile set. The methodology for these is documented but not yet fully operationalized for most technologies.
- **Dependency Slugs:** While the compiler checks for slug existence, some dependency relationships may still need refined historical review.
- **Source Depth:** While every `qa_passed` profile includes at least 2-4 sources, a deeper "evidence pack" in `research/evidence/` has not yet been used for any technology.
- **Status Field:** Several profiles are still marked as `status: draft` and are intentionally excluded from the master dataset.

## Stale or Conflicting Areas

- **README.md / PRD.md:** Still describe the repo as "greenfield / pre-implementation" and list "creating the first seed profiles" as a future task. In reality, 24 seed profiles are complete and compiled.
- **BACKLOG.md / ROADMAP.md:** Phase 0 and Phase 1 tasks are largely finished but still listed as active P0 priorities.
- **ARCHITECTURE.md:** Discusses "implementation surface options" but does not fully reflect that a "CLI-first research compiler" is already the operating reality.

## Immediate Repo Risks

- **Historical Date Drift:** Date claims (invention vs. T0) are highly sensitive to interpretation. While defenses are included, a secondary QA pass is recommended as the dataset grows.
- **Metric Inconsistency:** Adoption metrics (denominators) vary by technology type. Ensuring comparability across "Hard" (physical) and "Soft" (institutional) substrates remains a challenge.
- **Scaling Complexity:** The `fundamental_scaling_metric` is often a single value (e.g., "Cost per kWh"). Capturing the multi-dimensional nature of scaling in a single field may be reductive.

## Operating Status Summary

The project has successfully moved from "Concept" to "Initial Data Generation." The infrastructure for compiling and validating data is solid. The primary bottleneck is now the research required to populate diffusion milestones (T10-T75) and the adjudication of more complex dependency chains.
