```yaml
id: immune_system/vaccination_infrastructure
domain: Immune_System
subdomain: Immunization
technology: Vaccination Infrastructure
substrate_type: Soft
status: qa_passed
phase: 1
primary_dependencies: immune_system/public_health_surveillance;vascular/refrigerated_logistics_cold_chain
invention_year: 1962
invention_year_defense: 1962 is the strongest current invention boundary because the Vaccination Assistance Act and the CDC Immunization Assistance Grant Program created a recurring national framework for delivery infrastructure rather than isolated vaccine campaigns.
us_commercial_launch_year: 1962
us_commercial_launch_defense: 1962 is the better launch year because the Immunization Assistance Grant Program was established and administered through project grants that year, making the infrastructure available to state and local public-health systems immediately.
fundamental_scaling_metric: Cost per fully immunized person.
recommended_us_adoption_metric: Coverage rate for universally recommended childhood vaccination schedules.
denominator: Population
t10_years: 0
t25_years: 0
t50_years: 0
t75_years: 8
peak_adoption_or_current_status: Core public-health substrate, though confidence, uptake, and governance remain uneven across place and period.
confidence: medium
notes: National infrastructure boundary starts in 1962; earlier local programs are treated as precursors. Diffusion milestones use the childhood DTP (3+ doses) coverage series as a proxy for national infrastructure reach; because coverage was already ~68% at the 1962 launch, T10-T50 are recorded as 0 years.
```

# Vaccination Infrastructure

## Identity

- `Domain`: Immune_System
- `Subdomain`: Immunization
- `Technology`: Vaccination Infrastructure
- `Substrate Type`: Soft

## Scope And Inclusion Note

- This profile covers the recurring public-health infrastructure that procures, distributes, records, and administers vaccines at population scale, not any one vaccine product.
- It is in scope because it is measurable in coverage rates, deeply affects population resilience and economic continuity, and functions as a coordination layer built on top of logistics, clinics, surveillance, and cold-chain systems [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Biologics manufacturing
- Cold chain and distribution logistics
- Public-health agencies, clinics, records, and surveillance systems [1, 2]

## Phase 1 Claims

- `Invention Year`: 1962  
  Defense: 1962 is the strongest current invention boundary because the Vaccination Assistance Act and the CDC Immunization Assistance Grant Program created a recurring national framework for delivery infrastructure rather than isolated vaccine campaigns [1, 2].

- `U.S. Commercial Launch (T0)`: 1962  
  Defense: 1962 is the better launch year because the Immunization Assistance Grant Program was established and administered through project grants that year, making the infrastructure available to state and local public-health systems immediately [1, 2].

- `Fundamental Scaling Metric`: Cost per fully immunized person.

- `Recommended U.S. Adoption Metric`: Coverage rate for universally recommended childhood vaccination schedules.

- `Denominator`: Population

## Diffusion Milestones

- Canonical Tier 1 candidate series: CDC coverage for a stable childhood immunization schedule (DTP/Polio) [2, 4].
- `T10`: 0 years (1962). National coverage for basic vaccines was already ~68% at the time of the 1962 Act [4].
- `T25`: 0 years (1962). National coverage was already ~68% in 1962 [4].
- `T50`: 0 years (1962). National coverage was already ~68% in 1962 [4].
- `T75`: 8 years (1970). CDC reports coverage for core vaccines reached the mid-to-high 70% range by the late 1960s/1970 [4].
- `Peak Adoption / Current Status`: Core public-health substrate, though confidence, uptake, and governance remain uneven across place and period.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Centers for Disease Control and Prevention. "1940s-1970s Timeline." https://www.cdc.gov/museum/timeline/1940-1970.html
- [2] Centers for Disease Control and Prevention. "Vaccine-Preventable Diseases, Immunizations, and MMWR -- 1961-2011." https://www.cdc.gov/mmwr/preview/mmwrhtml/su6004a9.htm
- [3] Vaccination Assistance Act of 1962, Pub. L. 87-868.
- [4] Children's Hospital of Philadelphia. "Vaccine History: Developments by Year." https://www.chop.edu/centers-programs/vaccine-education-center/vaccine-history/developments-by-year

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Centers for Disease Control and Prevention. "1940s-1970s Timeline." https://www.cdc.gov/museum/timeline/1940-1970.html
- [2] Centers for Disease Control and Prevention. "Vaccine-Preventable Diseases, Immunizations, and MMWR -- 1961-2011." https://www.cdc.gov/mmwr/preview/mmwrhtml/su6004a9.htm
- [3] Vaccination Assistance Act of 1962, Pub. L. 87-868.

## Open Questions

- Whether earlier state and local immunization delivery systems should be captured as precursors while keeping 1962 as the national infrastructure boundary.
- Whether childhood schedule completion or total doses delivered is the better long-run adoption metric.

## QA Notes

- Dependency check: The listed dependencies all predate the 1960s program boundary.
- T0 check: 1962 is tied to an operating grant-backed delivery system, not to vaccine invention itself.
- Metric check: Population coverage is the right substrate lens.
