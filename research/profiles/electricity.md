```yaml
id: metabolism/electricity
domain: Metabolism
subdomain: Power
technology: Electricity
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies:
invention_year: 1831
invention_year_defense: Michael Faraday's demonstration of electromagnetic induction in 1831 created the first practical path to generating electricity mechanically rather than treating it only as a laboratory phenomenon.
us_commercial_launch_year: 1882
us_commercial_launch_defense: Pearl Street Station in lower Manhattan is the clearest defensible U.S. commercial launch because it sold centrally generated electricity to paying customers at city scale.
fundamental_scaling_metric: Cost per kWh delivered.
recommended_us_adoption_metric: Retail electricity sales per capita, with household electrification used as a diffusion proxy where needed.
denominator: Population
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Effectively universal dependency across U.S. households, firms, and public infrastructure.
confidence: medium
notes: Scope intentionally separated from electric_grid; invention boundary may tighten to a practical dynamo milestone. Tier 1 diffusion attempt deferred because the cleanest national household-adoption series belongs to electric_grid, while electricity sales-per-capita does not yet provide one stable threshold method distinct from grid connection.
```

# Electricity

## Identity

- `Domain`: Metabolism
- `Subdomain`: Power
- `Technology`: Electricity
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile treats electricity as controllable electric power generation and end use, distinct from the later network architecture of the electric grid.
- It satisfies the inclusion gates because it is post-1800 in practical form, measurable through U.S. generation and sales, and clearly operates as a system layer for industry, communications, health, and households [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- No earlier in-scope substrate is strictly required for the initial invention boundary chosen here.
- Commercial scale depended on dynamos, conductors, insulation, metering, and prime movers able to spin generators reliably [1, 3].

## Phase 1 Claims

- `Invention Year`: 1831  
  Defense: Michael Faraday's demonstration of electromagnetic induction in 1831 created the first practical path to generating electricity mechanically rather than treating it only as a laboratory phenomenon [1].

- `U.S. Commercial Launch (T0)`: 1882  
  Defense: Pearl Street Station in lower Manhattan is the clearest defensible U.S. commercial launch because it sold centrally generated electricity to paying customers at city scale [2, 3].

- `Fundamental Scaling Metric`: Cost per kWh delivered.

- `Recommended U.S. Adoption Metric`: Retail electricity sales per capita, with household electrification used as a diffusion proxy where needed.

- `Denominator`: Population

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Effectively universal dependency across U.S. households, firms, and public infrastructure.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Encyclopaedia Britannica. "Michael Faraday." https://www.britannica.com/biography/Michael-Faraday
- [2] IEEE Engineering and Technology History Wiki. "Milestones: Pearl Street Station, 1882." https://ethw.org/Milestones:Pearl_Street_Station,_1882
- [3] Hughes, Thomas P. *Networks of Power: Electrification in Western Society, 1880-1930*. Johns Hopkins University Press, 1983.

## Open Questions

- Whether a narrower boundary such as the practical dynamo should replace Faraday's 1831 induction result for the invention year.
- Whether electricity and grid commercialization should ultimately use the same T0 or remain distinct by scope.

## QA Notes

- Dependency check: No impossible dependency ordering in the current draft.
- T0 check: 1882 is a commercial service date, not a lab demonstration.
- Metric check: Direct ownership is not the key measure; sales and electrification are better substrate indicators.
