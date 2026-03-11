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

- Create a repeatable workflow for researching and validating technology profiles
- Establish a canonical schema for the master dataset
- Produce a small but rigorous MVP dataset for the first seed technologies
- Preserve methodological discipline around dates, dependencies, and adoption metrics
- Make the next 1 to 3 implementation moves obvious to future agents

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

- Milestone 1: Apply the documented inclusion rules, profile format, and citation conventions consistently
- Milestone 2: Create 12 to 16 validated technology profiles across all four domains
- Milestone 3: Compile the first canonical `data/processed/substrates_master.csv`
- Milestone 4: Add diffusion milestone methodology and fill it for the highest-confidence technologies
- Milestone 5: Produce the first comparative analysis on stacking, acceleration, and hard-vs-soft diffusion
