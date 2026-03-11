# Dependency Slug QA Round 2 Resolution

This note records the cleanup that followed `dependency_slug_qa_round1.md`.

## Outcome

The dependency slug contract is now normalized:

- `primary_dependencies` contains only canonical profile IDs
- unresolved placeholder slugs have been removed from profile metadata
- conceptual prerequisites remain in prose and notes instead of pretending to be resolvable graph nodes
- the `vascular/cold_chain_logistics` alias has been normalized to `vascular/refrigerated_logistics_cold_chain`

## Current State

- Compiled rows reviewed after cleanup: `24`
- Dependency edges after cleanup: `25`
- Invalid dependency slug shapes: `0`
- Unresolved dependency slugs in compiled CSV: `0`

## Enforcement Added

The compiler now enforces that:

- every dependency slug resolves to another compiled profile ID
- no row depends on itself
- no dependency is invented later than the row that depends on it

## Schema Decision

The repo now treats `primary_dependencies` as a closed canonical graph field.

If a prerequisite does not yet have its own canonical profile row, it should:

- stay in the prose dependency discussion
- stay in notes if it matters for later research
- not be inserted as a placeholder slug in profile metadata
