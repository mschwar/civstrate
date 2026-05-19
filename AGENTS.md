# Agent Operating Guide

## Mission

Build a defensible, source-backed research corpus and dataset for U.S. civilizational substrates after 1800, with explicit treatment of invention, commercialization, diffusion, and dependency chains.

## Read First

Future agents should read these files in order before making structural changes:

1. `README.md`
2. `CURRENT_STATE.md`
3. `AGENTS.md`
4. `PRD.md`
5. `ARCHITECTURE.md`
6. `SCHEMA.md`
7. `STANDARDS_MEMO.md`
8. `docs/agentic-overhaul/2026-05-audit.md`
9. `BACKLOG.md`
10. `ROADMAP.md`

## Canonical Sources

- `SCHEMA.md` defines the canonical artifact shapes and field names.
- `STANDARDS_MEMO.md` defines inclusion rules, citation expectations, and diffusion methodology.
- `CURRENT_STATE.md` is the current truth snapshot for the repo.
- `docs/agentic-overhaul/2026-05-audit.md` is the detailed audit for this overhaul pass.
- `research/profiles/` is the source corpus for compiled dataset rows.
- `data/processed/substrates_master.csv` is generated output and should never be hand-edited.
- `scripts/compile_profiles.py` is the compiler that turns QA-passed profiles into CSV.
- `scripts/validate_repo.py` is the canonical local and CI validation command.

## Commands

Before and after structural edits:

- `python scripts/validate_repo.py`
- `python scripts/compile_profiles.py --check`

When changing profile metadata:

- `python scripts/compile_profiles.py`
- `python scripts/validate_repo.py`
- `python scripts/compile_profiles.py --check`

## Generated Vs Hand-Authored

- Generated: `data/processed/substrates_master.csv`
- Hand-authored: docs, profile markdown, prompts, template CSV, compiler, validator, and CI workflow
- The compiler is the source of truth for generated output; do not edit the CSV by hand.

## Data And Provenance Rules

- Keep `primary_dependencies` limited to canonical profile IDs.
- Never invent placeholder slugs for unresolved prerequisites.
- Every `qa_passed` profile must have inline numbered citations and a numbered `## References` section.
- Every date claim needs a one-sentence defense in the profile metadata.
- Treat direct ownership metrics and indirect exposure metrics as different measurement problems.
- Do not present disputed history as settled. Record the rationale for the chosen date.
- If a claim, license, roadmap item, or status is contradictory, document the contradiction and make the smallest safe correction.

## Safe-Change Rules

- Make small, reviewable patches.
- Do not rewrite major artifacts unless the current truth is clearly wrong.
- Update source profile files first when a generated artifact needs to change.
- Do not hand-edit generated outputs.
- Do not introduce new frameworks, storage layers, or product surfaces unless the workflow requires them.
- If docs conflict, reconcile them in place rather than layering new contradictions on top.

## Known Traps

- `bash scripts/validate_repo.sh` is only a compatibility wrapper; use `python scripts/validate_repo.py` as the canonical command.
- `scripts/compile_profiles.py` only compiles `status: qa_passed` profiles.
- Dependency validation fails if a `primary_dependencies` slug does not resolve to a compiled profile id or points forward in time.
- `confidence` accepts only `high`, `medium`, or `low`.
- The profile template and compiler expect `confidence`, not a separate `confidence_score` field.
- The repo is still research-first; do not confuse the existence of a compiler with a finished application product.
