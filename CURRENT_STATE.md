# Current State

Audit date: 2026-05-19

This repository is the working research and data scaffold for a source-disciplined program that maps the invention, commercialization, diffusion, and dependency structure of foundational U.S. civilizational substrates after 1800. It now has a validated profile corpus, a compiled master dataset, and a small validation/compile toolchain; the main remaining work is methodological depth rather than repo bootstrapping.

## Confirmed Working

- The repo scaffold is stable and validated by `python scripts/validate_repo.py`.
- `scripts/compile_profiles.py` successfully regenerates `data/processed/substrates_master.csv` from QA-passed profiles.
- `python scripts/compile_profiles.py --check` confirms the checked-in CSV is current.
- `research/profiles/` contains **24** technology profiles, all marked `status: qa_passed`.
- `data/processed/substrates_master.csv` contains **24** compiled rows and matches the compiler output.
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
- `BACKLOG.md` still correctly treats diffusion milestone backfilling as open work.

## Known Risks

- Diffusion milestone backfilling remains incomplete for most profiles.
- Dependency chains still need periodic historical review as new profiles are added.
- The repo has a strong validation spine but no broader automated test suite yet.
- Hard and soft substrate adoption metrics remain methodologically different and should not be collapsed casually.

## Immediate Next Moves

- Backfill the remaining T10-T75 diffusion milestones where the underlying series are defensible.
- Keep dependency QA tight as new profiles are added.
- Add evidence packs only when profile references become noisy or disputed.
- Produce the first comparative analysis artifact only after the existing dataset slice stays stable under validation.
