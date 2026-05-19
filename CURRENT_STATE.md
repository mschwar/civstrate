# Current State

Audit date: 2026-05-19

This repository is the working research and data scaffold for a source-disciplined program that maps the invention, commercialization, diffusion, and dependency structure of foundational U.S. civilizational substrates after 1800. It now has a validated profile corpus, a compiled master dataset, and a small validation/compile toolchain; the main remaining work is coverage reporting, comparative analysis, and dependency depth rather than repo bootstrapping.

## Confirmed Working

- The repo scaffold is stable and validated by `python scripts/validate_repo.py`.
- `scripts/compile_profiles.py` successfully regenerates `data/processed/substrates_master.csv` from QA-passed profiles.
- `python scripts/compile_profiles.py --check` confirms the checked-in CSV is current.
- `research/profiles/` contains **24** technology profiles, all marked `status: qa_passed`.
- `data/processed/substrates_master.csv` contains **24** compiled rows and matches the compiler output.
- Diffusion milestone coverage is now **10/24 complete**, with **13/24 explicitly deferred** and **1/24 partially backfilled** because some higher thresholds are not reached in the chosen series.
- Starter prompts for the four domain agents plus QA are present in `research/prompts/`.
- The canonical schema, standards memo, runbook, and profile template are all in place.
- A minimal GitHub Actions validation workflow exists and mirrors the local validation command.

## Commands And Results

- `python scripts/validate_repo.py` passed.
- `python scripts/compile_profiles.py` passed.
- `python scripts/compile_profiles.py --check` passed.
- `bash scripts/validate_repo.sh` is a legacy wrapper; it was not executable in this Windows sandbox because `bash` is unavailable here.

## Important Files And Directories

- `README.md`, `AGENTS.md`, `CURRENT_STATE.md`, `docs/agentic-overhaul/2026-05-audit.md`, and `docs/agentic-loop/README.md`
- `docs/agentic-loop/missing-features.md`
- `PRD.md`, `ARCHITECTURE.md`, `ROADMAP.md`, `BACKLOG.md`, `RUNBOOK.md`
- `SCHEMA.md` and `STANDARDS_MEMO.md`
- `research/prompts/`, `research/profiles/`, `research/evidence/`, and `research/notes/`
- `data/templates/` and `data/processed/`
- `scripts/compile_profiles.py` and `scripts/validate_repo.py`

## Stale Or Conflicting Docs Or Metadata

- The main repo docs have been reconciled to the current state in this overhaul.
- The remaining legacy artifact is `scripts/validate_repo.sh`, which now delegates to the Python validator for compatibility.
- `BACKLOG.md` now treats initial diffusion backfill adjudication as complete and keeps the coverage report as the next diffusion-system work item.

## Known Risks

- No QA-passed profiles remain unadjudicated for diffusion milestones, but 13 profiles intentionally keep blank milestones because the available series do not provide stable single-denominator threshold crossings.
- The corpus still needs a coverage report so complete, partial, and intentionally deferred diffusion states are discoverable without manually inspecting profile notes or the CSV.
- Dependency chains still need periodic historical review as new profiles are added.
- The repo has a strong validation spine but no broader automated test suite yet.
- Hard and soft substrate adoption metrics remain methodologically different and should not be collapsed casually.

## Immediate Next Moves

- Add the diffusion coverage report from `docs/agentic-loop/missing-features.md` so milestone completeness and deferrals are visible as a generated or documented artifact.
- Keep dependency QA tight as new profiles are added.
- Add evidence packs only when profile references become noisy or disputed.
- Produce the first comparative analysis artifact only after the existing dataset slice stays stable under validation.
