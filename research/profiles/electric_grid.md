```yaml
id: metabolism/electric_grid
domain: Metabolism
subdomain: Power
technology: Electric Grid
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: metabolism/electricity
invention_year: 1882
invention_year_defense: Pearl Street Station is the most defensible invention boundary for the electric grid because it combined central generation, local distribution, meters, and paying end users in one practical urban system.
us_commercial_launch_year: 1882
us_commercial_launch_defense: The same Pearl Street deployment also marks the first clear U.S. commercial launch of the grid as a purchasable service network.
fundamental_scaling_metric: Cost per delivered kWh over networked transmission and distribution.
recommended_us_adoption_metric: Share of U.S. households or customers connected to central-station electric service.
denominator: Households
t10_years: 28
t25_years: 38
t50_years: 43
t75_years: 58
peak_adoption_or_current_status: Near-universal infrastructure dependency; most other modern substrates assume reliable grid access.
confidence: high
notes: Uses Pearl Street for both invention and T0 because practical grid and commercial service coincide. Diffusion milestones use the percentage of U.S. dwelling units with electric service from Historical Statistics of the United States (Series S 108-119).
```

# Electric Grid

## Identity

- `Domain`: Metabolism
- `Subdomain`: Power
- `Technology`: Electric Grid
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers the networked architecture that transmits and distributes centrally generated electricity, not electricity as a physical phenomenon.
- It qualifies because it is measurable in customer connections, line miles, and delivered power; later infrastructures overwhelmingly depend on it; and it is clearly a durable enabling layer [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Electricity generation
- Conductors, insulation, switchgear, and metering
- Prime movers and station equipment able to support central-station service [1, 2]

## Phase 1 Claims

- `Invention Year`: 1882  
  Defense: Pearl Street Station is the most defensible invention boundary for the electric grid because it combined central generation, local distribution, meters, and paying end users in one practical urban system [1].

- `U.S. Commercial Launch (T0)`: 1882  
  Defense: The same Pearl Street deployment also marks the first clear U.S. commercial launch of the grid as a purchasable service network [1, 2].

- `Fundamental Scaling Metric`: Cost per delivered kWh over networked transmission and distribution.

- `Recommended U.S. Adoption Metric`: Share of U.S. households or customers connected to central-station electric service.

- `Denominator`: Households

## Diffusion Milestones

- Canonical Tier 1 candidate series: percentage of dwelling units with electric service from Historical Statistics / Census sources [3].
- `T10`: 28 years (1910). First observed year in Historical Statistics above 10% (15% in 1910) [3].
- `T25`: 38 years (1920). Historical Statistics records 35% in 1920 [3].
- `T50`: 43 years (1925). Historical Statistics records 53% in 1925 [3].
- `T75`: 58 years (1940). Historical Statistics records 79% in 1940 [3].
- `Peak Adoption / Current Status`: Near-universal infrastructure dependency; most other modern substrates assume reliable grid access.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] IEEE Engineering and Technology History Wiki. "Milestones: Pearl Street Station, 1882." https://ethw.org/Milestones:Pearl_Street_Station,_1882
- [2] Hughes, Thomas P. *Networks of Power: Electrification in Western Society, 1880-1930*. Johns Hopkins University Press, 1983.
- [3] U.S. Bureau of the Census. *Historical Statistics of the United States, Colonial Times to 1957*, Chapter S, series on percentage of dwelling units with electric service, 1960. https://www2.census.gov/library/publications/1960/compendia/hist_stats_colonial-1957/hist_stats_colonial-1957-chS.pdf

## Open Questions

- Whether a later AC-network milestone such as the Niagara-to-Buffalo system should be tracked separately for grid maturation.
- Whether the recommended adoption metric should be household connections, customer counts, or generated load served.

## QA Notes

- Dependency check: Grid follows electricity generation and associated hardware.
- T0 check: 1882 reflects paid utility service, not a prototype.
- Metric check: Household or customer connection is the correct diffusion lens.
