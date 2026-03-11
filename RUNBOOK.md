# Runbook

## How To Orient Inside The Repo

Start with:

1. `README.md` for the current project state
2. `AGENTS.md` for operating rules
3. `PRD.md` and `ARCHITECTURE.md` for scope and workflow
4. `SCHEMA.md` and `STANDARDS_MEMO.md` for research contracts

Then inspect:

- `research/prompts/` for the current agent prompts
- `research/profiles/` for per-technology work
- `data/templates/` for the canonical dataset header

## Commands That Exist

- `bash scripts/validate_repo.sh`
  Validates that the required scaffold files and directories exist and that the dataset template header is present.
- `python3 scripts/compile_profiles.py`
  Rebuilds `data/processed/substrates_master.csv` from the metadata blocks in `research/profiles/*.md`, counting references automatically and including only `status: qa_passed` profiles.
- `python3 scripts/compile_profiles.py --check`
  Verifies that the checked-in `data/processed/substrates_master.csv` matches what the compiler would generate.

There is intentionally no application runtime, package manager, or build system yet.

## How To Validate Progress

- Run `python3 scripts/compile_profiles.py` after changing profile metadata.
- Run `python3 scripts/compile_profiles.py --check` before finishing to confirm the compiled dataset is up to date.
- Run `bash scripts/validate_repo.sh` after structural changes.
- Re-read any docs you changed for consistency with `README.md`, `AGENTS.md`, and `SCHEMA.md`.
- When adding profiles, confirm that every date claim has a source and a one-sentence defense.
- Confirm that profile prose uses numbered citations and ends with a numbered `References` section.
- Confirm that dependency claims do not point to technologies invented later than the dependent technology.
- Keep `primary_dependencies` limited to canonical profile IDs; put unresolved conceptual prerequisites in prose or notes instead of inventing placeholder slugs.

## How To Add Structure Without Drifting From The Concept

- Add the smallest structure that removes ambiguity for the next agent.
- Prefer updating canonical docs over inventing new top-level concepts.
- If you introduce a new artifact type, add it to `SCHEMA.md` and reference it from `README.md` or `ARCHITECTURE.md`.
- Do not create app code, services, or frameworks until the research workflow requires them.
- If a choice is still unsettled, log it as an open question rather than forcing a premature architecture decision.

## Recommended Next Move

Edit the metadata block in a validated profile, rerun `python3 scripts/compile_profiles.py`, and treat the regenerated `data/processed/substrates_master.csv` as the canonical compiled output rather than editing the CSV by hand.
