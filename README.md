# Civilizational Substrate Project

This repository is a greenfield bootstrap for a research and data program that maps the invention, commercialization, diffusion, and dependency structure of foundational "civilizational substrates" in the United States from 1800 to the present.

The workspace is intentionally pre-implementation. It now has a coherent operating structure, but it does not yet have a complete dataset, a settled software stack, or a finished product surface.

## Project Overview

The core question is why some technologies become so foundational that large portions of GDP, logistics, coordination, or public capacity depend on them within a few decades. The initial framing treats civilization as a stacked system with:

- `Metabolism`: energy and materials
- `Vascular`: transport and logistics
- `Nervous_System`: communications and compute
- `Immune_System`: health and societal capacity

The project is not meant to catalog consumer fads. It is meant to build a defensible, source-backed corpus of general-purpose technologies, enabling infrastructures, and critical materials that changed the operating substrate of the U.S. economy.

## Current Status

- Greenfield / pre-implementation
- Canonical docs are now in place
- Research standards and starter prompts exist
- A machine-readable dataset template exists
- No ingestion pipeline, dashboard, notebook suite, or publication workflow has been built yet

## Intended Use Case

This repo is for a team of human and AI agents who need to:

- decide which technologies belong in scope
- create source-backed technology profiles
- adjudicate disputed dates and dependency claims
- assemble a canonical master dataset
- produce later analysis on diffusion speed, scaling laws, and stacked-system vulnerability

## Repo Structure

- `README.md`: entry point and orientation
- `AGENTS.md`: operating guide for future agents
- `PRD.md`: product and project definition for the research program
- `ARCHITECTURE.md`: target repo and workflow architecture
- `ROADMAP.md`: phased execution plan
- `BACKLOG.md`: prioritized next actions
- `RUNBOOK.md`: practical instructions for working in the repo
- `SCHEMA.md`: canonical artifact and dataset schema
- `STANDARDS_MEMO.md`: research adjudication rules carried forward from the original notes
- `research/prompts/`: starter prompts for the first research and QA agents
- `research/profiles/`: future per-technology profiles
- `research/evidence/`: optional later evidence packs for claims that need more than normal profile references
- `research/notes/`: preserved source notes from the loose-folder stage
- `data/templates/`: starter machine-readable artifacts
- `data/raw/`: future raw source extracts and evidence packs
- `data/processed/`: future compiled datasets
- `scripts/`: lightweight repo validation and utilities

## What Is Known, Assumed, and Undecided

Known from the original notes:

- Geography is U.S.-only for the initial version
- The timeline starts after 1800
- The focus is foundational technologies, infrastructures, and materials
- The first analytical lenses are invention year, U.S. commercial launch, dependencies, diffusion milestones, and scaling metrics
- Phase 1 covers all four domains: `Metabolism`, `Vascular`, `Nervous_System`, and `Immune_System`

Working assumptions:

- The first useful artifact is a canonical master dataset plus profile files, not a software product
- Markdown profiles plus CSV outputs are sufficient for Phase 0 and Phase 1
- Citation formatting should mirror the newest Google DeepMind white-paper pattern: numbered citations in the text with a numbered references section at the end

Still undecided:

- the eventual analysis/publishing surface
- whether later implementation should be Python-first, notebook-first, or app-first

## How To Continue From Here

1. Read `README.md`, `AGENTS.md`, `PRD.md`, `ARCHITECTURE.md`, `SCHEMA.md`, and `STANDARDS_MEMO.md`.
2. Use the documented inclusion cutoff in `STANDARDS_MEMO.md` before adding or rejecting borderline technologies.
3. Create a small set of source-backed profiles in `research/profiles/` for seed technologies across all four domains.
4. Run QA against those profiles using the adjudication prompt.
5. Compile the first `data/processed/substrates_master.csv` from validated profiles.
6. Choose an implementation surface from the options documented in `ARCHITECTURE.md` only after the first dataset slice exists.
