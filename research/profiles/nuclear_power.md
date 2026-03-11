```yaml
id: metabolism/nuclear_power
domain: Metabolism
subdomain: Power
technology: Nuclear Power
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: metabolism/electric_grid
invention_year: 1951
invention_year_defense: 1951 is the cleanest practical invention boundary because EBR-I produced the first usable electricity from nuclear fission, demonstrating nuclear power as a working electricity-generating technology rather than a weapons-only reactor program.
us_commercial_launch_year: 1957
us_commercial_launch_defense: 1957 is the strongest U.S. commercial launch year because Shippingport began operation as the first full-scale nuclear power plant serving utility customers rather than functioning only as an experimental reactor.
fundamental_scaling_metric: Cost per kWh delivered.
recommended_us_adoption_metric: Share of U.S. electricity generation produced by nuclear power, with installed nuclear generating capacity as a supporting series.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Major zero-carbon baseload substrate with enduring importance to the U.S. grid, though expansion has been slower and more contested than earlier expectations.
confidence: high
notes: Uses 1951 for first usable nuclear electricity and 1957 for commercial grid service; the 1954 Atomic Energy Act remains the key civilian-commercial precursor. Tier 1 diffusion attempt deferred because generation-share series are strong, but the practical saturation ceiling for nuclear power remains too policy-contingent for a clean threshold interpretation in Round 1.
```

# Nuclear Power

## Identity

- `Domain`: Metabolism
- `Subdomain`: Power
- `Technology`: Nuclear Power
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers civilian nuclear fission power as an electricity-generating substrate, not nuclear weapons production, naval propulsion, or the broader nuclear fuel cycle in isolation.
- It is in scope because it became a major utility-scale generation technology with measurable U.S. output, deep grid dependence, and persistent strategic importance for industrial and public-capacity resilience [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- A preexisting electric-grid and utility system able to absorb large central-station generation [2].
- Steam-turbine power conversion and associated thermal plant engineering.
- Precision materials, reactor engineering, and fuel handling systems capable of sustained high-energy operation [1, 3].

## Phase 1 Claims

- `Invention Year`: 1951  
  Defense: 1951 is the cleanest practical boundary because DOE identifies EBR-I as the first reactor to produce usable electricity through atomic fission [1].

- `U.S. Commercial Launch (T0)`: 1957  
  Defense: 1957 is the strongest U.S. launch year because DOE identifies Shippingport as the first full-scale nuclear power plant and notes that it provided power to Duquesne Light customers [2, 3].

- `Fundamental Scaling Metric`: Cost per kWh delivered.

- `Recommended U.S. Adoption Metric`: Share of U.S. electricity generation produced by nuclear power, with installed nuclear generating capacity as a supporting series.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Major zero-carbon baseload substrate with enduring importance to the U.S. grid, though expansion has been slower and more contested than earlier expectations.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] U.S. Department of Energy. "9 Notable Facts About the World's First Nuclear Power Plant - EBR-I." https://www.energy.gov/ne/articles/9-notable-facts-about-world-s-first-nuclear-power-plant-ebr-i
- [2] U.S. Department of Energy. "December 23, 1957: Shippingport." https://www.energy.gov/management/december-23-1957-shippingport
- [3] U.S. Department of Energy. *The United States Naval Nuclear Propulsion Program.* https://www.energy.gov/sites/prod/files/2017/08/f36/nuclear_propulsion_program_8-30-2016%5B1%5D.pdf
- [4] Nuclear Regulatory Commission. "History." https://ww2.nrc.gov/about-nrc/history

## Open Questions

- Whether later work should split `nuclear_power` into light-water-reactor commercialization and the broader civilian nuclear-power regime.
- Whether the best long-run adoption series is generation share, installed capacity, or reactor fleet counts weighted by output.

## QA Notes

- PASS
- Dependency check: The listed dependencies predate commercial nuclear generation and reflect grid-scale power prerequisites rather than later digital controls.
- T0 check: 1957 is acceptable because Shippingport was operating as a utility-serving power station, not only as a laboratory demonstration.
- Metric check: Generation share is stronger than plant counts for a central-station power substrate.
