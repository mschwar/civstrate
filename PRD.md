# Product Requirements Document

## Problem

There is no structured, source-disciplined working repository for analyzing how foundational U.S. technologies become civilizational dependencies. Existing notes define a compelling thesis, but they do not yet provide a buildable workflow, artifact contract, or prioritized execution path.

## Users

- Lead researcher defining scope, claims, and final narrative
- Research agents generating technology profiles and source packs
- QA/adjudication agents verifying dates, dependencies, and metrics
- Data and analysis agents assembling the master dataset and later outputs
- Future readers or collaborators consuming the resulting dataset, memos, and visualizations

## Jobs To Be Done

- Decide which technologies count as civilizational substrates
- Capture the best defensible invention year and U.S. commercial launch year for each technology
- Model substrate dependencies so stacked-system analysis is possible
- Record how each technology should be measured for U.S. adoption or exposure
- Build a canonical dataset that can support later charts, essays, and comparative analysis

## Goals

- **Maintain a repeatable workflow** for research, validation, and automated compilation.
- **Produce a rigorous dataset** of at least 24 foundational technologies.
- **Quantify diffusion speed** using standardized milestones (T10-T75).
- **Model dependency chains** for civilizational infrastructure (Stacked-System Analysis).
- **Make the methodology defensible** through numbered citations and one-sentence defenses for every date claim.

## Non-Goals

- Building a polished end-user application in the bootstrap phase
- Covering every country or all pre-industrial history
- Producing exhaustive global technology histories
- Automating web scraping or large-scale ingestion before the methodology is stable
- Creating forecasts or causal claims that the underlying data cannot yet support

## Assumptions

- U.S. scope is the right initial constraint because it improves data availability and comparability
- Post-1800 is the correct historical cutoff for this project
- The first durable product is a dataset plus research corpus, not a web experience
- Per-technology markdown profiles are good enough for the first round of collection and adjudication
- Phase 1 should cover all four domains
- Citations should follow the newest Google DeepMind white-paper convention: numbered inline citations plus a numbered reference list

## Open Questions

- Which output matters first after the dataset: analysis memo, charts, notebook, or app?
- How should GDP exposure be estimated for enabling components that are not directly owned?
- What confidence model should be attached to disputed historical claims?

## Initial Milestones

- **Milestone 1: (COMPLETED)** Stabilize inclusion rules, profile format, and citation conventions.
- **Milestone 2: (COMPLETED)** Create 24 validated technology profiles across all four domains.
- **Milestone 3: (COMPLETED)** Compile the first canonical `data/processed/substrates_master.csv` via automation.
- **Milestone 4: (ACTIVE)** [x] Define diffusion milestone methodology. [ ] Populate T10-T75 fields for all validated rows (9/24 profiles completed).
- **Milestone 5: (PLANNED)** Produce the first comparative analysis on stacking and acceleration.
