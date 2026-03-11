# Next Profile Wave

## Objective

Expand the profile set beyond the first 12 without jumping into the most ambiguous edge cases too early.

The next wave should improve:

- continuity across the dependency stack
- coverage balance across all four domains
- the usefulness of later hard-vs-soft and stacked-dependency analysis

## Recommended Scope

Do `Wave 2A` first. It is the best tradeoff between analytical value and research tractability.

### Wave 2A: Recommended Now

- `internal_combustion_engine`
  Why now: directly connects `oil_refining` to `freight_trucking`, mechanized logistics, and later aviation.

- `portland_cement_concrete`
  Why now: complements `bessemer_steel`, `municipal_sanitation`, roads, and modern urban buildout.

- `microprocessors`
  Why now: creates the missing bridge from `semiconductors` to PCs, cloud, and AI-era compute.

- `fiber_optics`
  Why now: creates the missing physical-network bridge between `telephone`/telecom systems and modern `internet` bandwidth scaling.

- `freight_trucking`
  Why now: complements `railroads` and `containerization` and makes the U.S. logistics stack much more legible.

- `pipelines`
  Why now: creates a clearer fuel and materials transport layer adjacent to `oil_refining`.

- `water_filtration_and_chlorination`
  Why now: is the cleanest adjacent follow-on to `municipal_sanitation` and has a strong public-health impact trail.

- `public_health_surveillance`
  Why now: complements `vaccination_infrastructure` and introduces an explicit coordination layer within `Immune_System`.

### Wave 2B: After Wave 2A QA

- `nuclear_power`
- `radio`
- `refrigerated_logistics_cold_chain`
- `modern_hospital_systems`

These should wait until `Wave 2A` is through QA. They are valuable, but each carries more scope or boundary risk than the `Wave 2A` set.

## Recommended Order Inside Wave 2A

1. `internal_combustion_engine`
2. `freight_trucking`
3. `pipelines`
4. `portland_cement_concrete`
5. `water_filtration_and_chlorination`
6. `microprocessors`
7. `fiber_optics`
8. `public_health_surveillance`

This order is deliberate:

- it resolves obvious gaps next to the current seed profiles
- it builds strong dependency bridges before moving to more abstract coordination layers
- it keeps all four domains active without scattering into too many borderline cases

## Research Rules For This Wave

- Reuse the current profile template in `research/profiles/PROFILE_TEMPLATE.md`.
- Use numbered citations and a numbered `References` section.
- Do not mark a profile `qa_passed` until adjudication is complete.
- Prefer one canonical U.S. adoption or exposure metric per profile.
- If a candidate cannot cleanly pass the inclusion cutoff in `STANDARDS_MEMO.md`, log that and stop rather than forcing it into scope.

## Minimum Output For Each New Profile

- stable metadata block
- clear scope note
- primary dependencies
- invention year and defense
- U.S. commercial launch year and defense
- scaling metric
- recommended U.S. adoption metric and denominator
- references
- open questions
- QA notes

## Done Condition For Wave 2A

Wave 2A is done when:

- all 8 profiles exist in `research/profiles/`
- all 8 have passed QA or have explicit blocking questions logged
- any newly surfaced schema or denominator issues have been documented
- the compiler can include the passed subset without manual CSV edits
