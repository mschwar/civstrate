```yaml
id: metabolism/oil_refining
domain: Metabolism
subdomain: Fuels
technology: Oil Refining
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies:
invention_year: 1854
invention_year_defense: Samuel Kier's mid-1850s distillation of petroleum into lamp oil is a practical U.S. refining boundary because it turned crude petroleum into a marketable product rather than a curiosity.
us_commercial_launch_year: 1859
us_commercial_launch_defense: 1859 is the better commercial launch year because the Drake well and ensuing refinery buildout created a repeatable petroleum supply chain that customers and firms could actually purchase from at scale.
fundamental_scaling_metric: Cost per barrel refined.
recommended_us_adoption_metric: U.S. refining capacity in barrels per day.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Still foundational to transport fuels, petrochemicals, and military logistics despite energy-transition pressures.
confidence: medium
notes: Kier-era invention boundary retained; the repo may later split kerosene-era and motor-fuel-era refining. Tier 1 diffusion attempt deferred because refining capacity is a strong industrial exposure series but does not yet have a stable adoption-threshold denominator for Round 1.
```

# Oil Refining

## Identity

- `Domain`: Metabolism
- `Subdomain`: Fuels
- `Technology`: Oil Refining
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers industrial refining of petroleum into usable fuels and feedstocks, not crude extraction.
- It is in scope because it became a measurable nationwide processing layer, underlies transport and petrochemicals, and clearly functions as durable industrial infrastructure [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Crude oil supply
- Distillation equipment, industrial heat, storage, and distribution infrastructure [1, 2]

## Phase 1 Claims

- `Invention Year`: 1854  
  Defense: Samuel Kier's mid-1850s distillation of petroleum into lamp oil is a practical U.S. refining boundary because it turned crude petroleum into a marketable product rather than a curiosity [1, 3].

- `U.S. Commercial Launch (T0)`: 1859  
  Defense: 1859 is the better commercial launch year because the Drake well and ensuing refinery buildout created a repeatable petroleum supply chain that customers and firms could actually purchase from at scale [1, 2].

- `Fundamental Scaling Metric`: Cost per barrel refined.

- `Recommended U.S. Adoption Metric`: U.S. refining capacity in barrels per day.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Still foundational to transport fuels, petrochemicals, and military logistics despite energy-transition pressures.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Yergin, Daniel. *The Prize: The Epic Quest for Oil, Money & Power*. Simon & Schuster, 1991.
- [2] U.S. Energy Information Administration. "Petroleum and the History of U.S. Refining" and related historical materials. https://www.eia.gov/
- [3] American Chemical Society. National Historic Chemical Landmarks materials on the birth of the U.S. petroleum industry. https://www.acs.org/education/whatischemistry/landmarks.html

## Open Questions

- Whether the invention boundary should stay with Kier's early refining work or move to a slightly later petroleum-specific industrial process milestone.
- Whether kerosene-era refining and motor-fuel-era refining should later be split analytically.

## QA Notes

- Dependency check: Refining depends on crude supply and industrial processing equipment, not on later transport substrates.
- T0 check: 1859 is tied to real market availability rather than a lab process.
- Metric check: Capacity and throughput are better than consumer ownership.
