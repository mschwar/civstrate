```yaml
id: immune_system/water_filtration_and_chlorination
domain: Immune_System
subdomain: Water
technology: Water Filtration and Chlorination
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: immune_system/municipal_sanitation
invention_year: 1908
invention_year_defense: 1908 is the strongest practical invention boundary for the modern U.S. treated-water substrate because routine chlorination completed a scalable filtration-plus-disinfection regime rather than a filtration-only precursor.
us_commercial_launch_year: 1908
us_commercial_launch_defense: 1908 is the clearest U.S. public-deployment boundary because Jersey City began routine community-water chlorination that year and the model rapidly spread across municipal systems.
fundamental_scaling_metric: Cost per million gallons treated.
recommended_us_adoption_metric: Share of the U.S. population served by filtered and disinfected community water systems.
denominator: Population
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Core public-health substrate and baseline expectation for municipal drinking water in the modern United States.
confidence: medium
notes: Earlier filtration-only milestones remain important precursors, but 1908 is used to represent the modern U.S. treated-water regime centered on routine disinfection. Tier 1 diffusion attempt deferred because the strongest national series mix filtration, chlorination, and community-water coverage without one continuous treated-population threshold series.
```

# Water Filtration and Chlorination

## Identity

- `Domain`: Immune_System
- `Subdomain`: Water
- `Technology`: Water Filtration and Chlorination
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers municipal drinking-water treatment based on filtration plus chlorination, not raw water supply or sewerage alone.
- It is in scope because it became a durable population-scale disease-control substrate with measurable coverage, strong mortality effects, and deep links to urban growth and public-health capacity [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Piped municipal water systems and utility governance able to deliver treated water at city scale [1].
- Chemical production and dosing systems for chlorine and related disinfectants [2].
- Filtration plant, pumping, and distribution infrastructure that let treatment persist as an operating service rather than a one-time intervention.

## Phase 1 Claims

- `Invention Year`: 1908  
  Defense: 1908 is the best current practical boundary because routine chlorination completed the modern treated-water stack, turning earlier filtration work into a robust municipal disease-control substrate [1, 2].

- `U.S. Commercial Launch (T0)`: 1908  
  Defense: 1908 is the clearest U.S. launch year because CDC and EPA identify Jersey City as the first U.S. city to begin routine community-water chlorination, after which the practice spread rapidly [1, 2].

- `Fundamental Scaling Metric`: Cost per million gallons treated.

- `Recommended U.S. Adoption Metric`: Share of the U.S. population served by filtered and disinfected community water systems.

- `Denominator`: Population

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Core public-health substrate and baseline expectation for municipal drinking water in the modern United States.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Centers for Disease Control and Prevention. "History of Drinking Water Treatment." https://archive.cdc.gov/www_cdc_gov/healthywater/drinking/history.html
- [2] U.S. Environmental Protection Agency. *An Overview of the Safe Drinking Water Act*. https://www.epa.gov/system/files/documents/2026-02/sdwa.pdf
- [3] U.S. Environmental Protection Agency. "The History of Drinking Water Treatment." https://archive.epa.gov/water/archive/web/pdf/2001_11_15_consumer_hist.pdf

## Open Questions

- Whether the profile should stay combined as `water_filtration_and_chlorination` or split into separate filtration and disinfection substrates.
- Whether the best adoption series is treated-population coverage, treatment-plant capacity, or compliance-based community water system coverage.

## QA Notes

- PASS
- Dependency check: The profile appropriately follows water-network and sanitation buildout.
- T0 check: 1908 is well sourced for routine chlorination and is acceptable because the row explicitly covers the mature filtration-plus-disinfection stack.
- Metric check: Population served is more defensible than plant counts.
