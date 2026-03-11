# Architecture Direction

## Current State

The repository began as a loose note folder with:

- a concept memo in `README.md`
- a schema sketch in `SCHEMA.md`
- a standards memo in `STANDARDS_MEMO.md`
- an untitled prompt note that has been preserved under `research/notes/`

There is no application runtime, data pipeline, or validated dataset yet.

## Proposed Target Architecture

The project should start as a research-and-data repository with four layers:

1. `Canonical docs`
   Purpose: define scope, workflow, architecture, milestones, and operating rules.

2. `Research artifacts`
   Purpose: store prompts, profile templates, source notes, and future technology profiles.

3. `Data artifacts`
   Purpose: hold machine-readable templates, raw evidence extracts, and compiled datasets.

4. `Lightweight validation`
   Purpose: verify that the repo scaffold and canonical artifacts remain intact as the project evolves.

## Candidate Components

- `research/prompts/`
  Seed prompts for domain researchers and QA agents.

- `research/profiles/`
  One file per technology, written against a stable profile template.

- `research/evidence/`
  Optional later home for source extracts or evidence packs when a claim needs more than a normal profile citation.

- `data/templates/substrates_master.template.csv`
  The canonical starter header for the master dataset.

- `data/raw/`
  Raw source extracts, notes, or evidence packs.

- `data/processed/`
  Compiled outputs such as `data/processed/substrates_master.csv`.

- `scripts/validate_repo.sh`
  A simple repo-level structural validation step.

## Workflow

```text
Source note or research question
-> per-technology profile draft
-> QA / adjudication review
-> validated profile
-> master dataset row(s)
-> later analysis, visualization, and publication
```

## Tradeoffs

- `Markdown profiles first` vs `database first`
  Markdown is slower for bulk operations, but it keeps early-stage claims readable and reviewable.

- `CSV master table` vs `SQL warehouse`
  CSV is limited, but it is sufficient until the schema and workflow stabilize.

- `Manual adjudication` vs `automated ingestion`
  Manual review is slower, but this project is currently bottlenecked by methodological clarity, not by throughput.

- `U.S.-only scope` vs `global scope`
  U.S.-only is less complete, but it reduces ambiguity and makes Phase 1 feasible.

## Implementation Surface Options

These are the top five implementation surfaces for the project, in descending order of current fit.

1. `CLI-first research compiler`
   Best fit for the current stage. Keeps the repo centered on profile authoring, QA, dataset compilation, and lightweight validation.

2. `Notebook-first analysis workspace`
   Good once the first dataset exists. Strong for exploratory charts, milestone analysis, and essay support, but weaker for disciplined data entry.

3. `Static publication site`
   Useful after the research corpus stabilizes. Good for publishing profiles, charts, and essays without building application complexity.

4. `Lightweight review web app`
   Useful if multiple agents or humans need a dedicated interface for adjudication and dataset edits. Premature before the schema and workflow settle.

5. `Dependency-graph explorer`
   Potentially strong for later stacked-vulnerability analysis, but only after dependencies are consistently modeled across many validated profiles.

The current recommendation is option 1: a CLI-first research compiler, with notebooks as the first likely companion surface once the initial dataset slice exists.

## What Should Not Be Built Yet

- No dashboard or public-facing app
- No generalized agent framework
- No complex ETL or scraping pipeline
- No vector database or retrieval system
- No predictive model or simulation layer
- No large taxonomy expansion before the inclusion rules are frozen
- No review web app before profile and QA workflows prove stable

The immediate need is not more software. It is a stable research contract that multiple agents can execute against without drifting.
