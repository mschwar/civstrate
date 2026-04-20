# Backlog

## P0: Diffusion Milestones

- [x] Define the standardized methodology for the 10%, 25%, 50%, and 75% adoption thresholds.
- [ ] Backfill `t10_years` through `t75_years` for all 24 validated profiles. (9/24 completed: Electric Grid, Telephone, Internet, Railroads, Municipal Sanitation, Vaccination Infrastructure, Electricity, Telegraph, Containerization).
- Adjudicate cases where direct adoption metrics (e.g., household percentage) are missing and indirect proxies are required.

## P1: Structural Cleanup

- [x] Define a confidence scoring model for disputed historical claims (numerical or tiered).
- [x] Resolve any remaining dependency-slug inconsistencies found during the first compilation pass.
- [x] Standardize the `recommended_us_adoption_metric` across technologies within the same domain.

## P2: Analysis and Visualization

- Build charting or notebook outputs for comparative analysis (e.g., diffusion latency by substrate type).
- Add source-evidence sidecars in `research/evidence/` if profile references become too noisy.
- Evaluate a lightweight dashboard for visualizing the dependency graph.

## Completed Tasks

- [x] Apply inclusion cutoff rules to initial substrate set.
- [x] Create seed profiles for 24 foundational technologies.
- [x] Implement citation and reference standards.
- [x] Build and verify the `compile_profiles.py` script.
- [x] Generate the first `data/processed/substrates_master.csv`.

## Tasks That Should Wait

- Global expansion (keep U.S. focus)
- Full automation of research collection
- Dashboard/UI development
- Predictive modeling
