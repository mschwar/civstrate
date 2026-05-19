# Agentic Buildout Loop

This document defines the two-prompt loop used to deliver the repo one independently mergeable feature at a time.

## Operating Goal

Every feature should be:

- independently mergeable
- implemented on one branch with one PR
- testable in the browser or by explicit non-UI verification
- discoverable by the next agent without chat context

The loop is intentionally narrow. It favors small vertical slices over broad platform moves so each PR can be reviewed, verified, and merged without pulling in unrelated work.

## Canonical Inputs

Before starting a feature, read:

- `CURRENT_STATE.md`
- `AGENTS.md`
- `docs/agentic-loop/missing-features.md`
- `docs/agentic-loop/backfill-swarm-plan.md` when the selected feature touches diffusion milestones
- the feature-specific source files for the slice you are about to change

Do not rely on prior chat unless the required context is also written in the repo.

## Feature Contract

Each feature branch must have exactly one primary purpose.

- One branch
- One PR
- One feature
- One verification path

If a change set starts to span multiple features, split it before merge.

## Verification Rules

Use the smallest validation that proves the feature.

- For browser-visible work: run the app, verify the flow in the browser, and capture screenshots.
- For non-UI work: run an explicit command that proves the behavior, and record the command plus its result.
- If the feature touches both, the browser check is primary and the command check is supporting evidence.

Never mark a feature done without a reproducible verification path.

## Handoff Contract

When a build prompt finishes, leave enough context in the repo for the QA prompt to work without chat history.

- Update docs if the feature changed what the next agent should know.
- Ensure the missing-feature list still reflects the correct next item.
- Keep the branch summary, verification command, and any screenshot paths in the PR description or feature notes.

## Prompt A

Use this prompt for the build pass:

> Create a feature branch and develop the next feature from `docs/agentic-loop/missing-features.md`. Keep the change to one independently mergeable feature, update the relevant docs, run the explicit verification, then commit and push the branch.

For diffusion backfill features, add:

> Use `docs/agentic-loop/backfill-swarm-plan.md` and `STANDARDS_MEMO.md` section 7. Update source profiles first, regenerate the master CSV with `python scripts/compile_profiles.py`, and do not force weak milestone values where an explicit deferral is more defensible.

## Prompt B

Use this prompt for the QA pass:

> Check out the feature branch, verify it in the browser or with the explicit non-UI check, take screenshots if the feature has a UI, update the docs and review notes, then commit, push, and merge.

For diffusion backfill QA, add:

> Verify the selected series, denominator alignment, first observed threshold crossings, arithmetic from launch year, profile references, regenerated CSV, and the validation commands listed in the feature row.

## Done Criteria

A feature is done when:

- the code or content change is merged cleanly
- validation passes
- the QA path is reproducible
- the next feature can be discovered from `docs/agentic-loop/missing-features.md`
- the repo truth files still match the implemented state
