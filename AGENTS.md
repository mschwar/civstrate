# Agent Operating Guide

## Mission

Build a defensible, source-backed research corpus and dataset for U.S. civilizational substrates after 1800, with explicit treatment of invention, commercialization, diffusion, scaling, and dependency chains.

## Read First

Future agents should read these files in order before making structural changes:

1. `README.md`
2. `AGENTS.md`
3. `PRD.md`
4. `ARCHITECTURE.md`
5. `SCHEMA.md`
6. `STANDARDS_MEMO.md`
7. `BACKLOG.md`
8. `ROADMAP.md`

## Operating Rules

- Treat this repository as an early-stage research system, not a finished software product.
- Preserve the current scope unless a doc is explicitly updated: U.S.-only, post-1800, foundational substrates only.
- Separate `known`, `assumed`, and `open question` content explicitly in docs and research notes.
- Do not present disputed history as settled fact. Record why a chosen date was selected.
- Use the workflow `profile -> QA/adjudication -> master dataset`, not direct unreviewed edits into the final dataset.
- Keep file and field naming stable once a canonical name lands in `SCHEMA.md`.
- Prefer small, source-backed additions over broad speculative framework work.
- Do not invent an application stack or data platform until the concept and artifact flow are stable.
- Preserve the distinction between direct adoption metrics and indirect economic exposure metrics for component technologies.

## What Is Real

- The project thesis and constraints in `README.md`
- The research standards in `STANDARDS_MEMO.md`
- The initial artifact model in `SCHEMA.md`
- **24 validated technology profiles** in `research/profiles/`
- **The research compiler** (`scripts/compile_profiles.py`) for automated CSV generation
- Starter prompts for all four domain agents plus QA in `research/prompts/`
- A CSV template for the master dataset in `data/templates/`

## What Is Assumed

- The project should begin as a documentation and data repo rather than a UI or product repo
- Markdown is an acceptable authoring format for individual technology profiles
- The first concrete build step is a small seed set of validated profiles
- Phase 1 covers all four domains
- Citation formatting should follow the newest Google DeepMind white-paper convention: numbered citations in the text and a numbered references section at the end

## What Is Undecided

- Whether a notebook, CLI, or app should become the first implementation surface
- The best method for measuring indirect exposure for deep components like semiconductors and cloud infrastructure
- Confidence thresholds for disputed historical claims near the inclusion boundary

## Definition Of Done For Early-Stage Work

For Phase 0 and early Phase 1 tasks, work is done when:

- the affected docs remain internally consistent
- assumptions are marked instead of hidden
- new profiles include sources and date justifications
- QA/adjudication can review the work without extra verbal context
- changes make the next implementation move more obvious, not less

Work is not done if it only adds volume, new abstractions, or speculative code without improving clarity or execution readiness.
