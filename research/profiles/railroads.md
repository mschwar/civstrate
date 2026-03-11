```yaml
id: vascular/railroads
domain: Vascular
subdomain: Freight
technology: Railroads
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies:
invention_year: 1830
invention_year_defense: For a U.S.-scoped substrate, 1830 is the best practical invention boundary because common-carrier steam railroad service began operation in that year.
us_commercial_launch_year: 1830
us_commercial_launch_defense: The same 1830 operating milestone also marks commercial launch because freight and passenger rail service was being offered as a transport service rather than merely tested.
fundamental_scaling_metric: Cost per ton-mile.
recommended_us_adoption_metric: U.S. railroad freight ton-miles, with route miles as an early diffusion proxy.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Still critical for bulk freight, though no longer the dominant passenger substrate.
confidence: medium
notes: 1830 reflects U.S. common-carrier steam service rather than earlier prototypes or horse railways. Tier 1 diffusion attempt deferred because route miles are the clearest early national series, but Round 1 has not yet frozen whether thresholds should be normalized to peak route mileage, freight ton-miles, or another national exposure denominator.
```

# Railroads

## Identity

- `Domain`: Vascular
- `Subdomain`: Freight
- `Technology`: Railroads
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers steam-era common-carrier railroads as a transport substrate for moving freight, people, and industrial inputs across the U.S.
- It is in scope because it is measurable in route miles and ton-miles, transformed multiple sectors, and became a major dependency for later logistics and communications systems [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Steam power
- Iron and later steel rails
- Rights-of-way, bridges, signaling, and terminal infrastructure [1, 2]

## Phase 1 Claims

- `Invention Year`: 1830  
  Defense: For a U.S.-scoped substrate, 1830 is the best practical invention boundary because common-carrier steam railroad service began operation in that year [1].

- `U.S. Commercial Launch (T0)`: 1830  
  Defense: The same 1830 operating milestone also marks commercial launch because freight and passenger rail service was being offered as a transport service rather than merely tested [1].

- `Fundamental Scaling Metric`: Cost per ton-mile.

- `Recommended U.S. Adoption Metric`: U.S. railroad freight ton-miles, with route miles as an early diffusion proxy.

- `Denominator`: Volume

## Diffusion Milestones

- Canonical Tier 1 candidate series: national route miles first, freight ton-miles second.
- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Still critical for bulk freight, though no longer the dominant passenger substrate.

Tier 1 result: deferred. The national route-mile series is tractable, but the milestone denominator is not yet frozen tightly enough to produce reproducible threshold years that would survive adjudication.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Federal Transit Administration. "History of NTD and Transit in the United States." https://www.transit.dot.gov/ntd/history-ntd-and-transit-united-states
- [2] Chandler, Alfred D. *The Visible Hand: The Managerial Revolution in American Business*. Harvard University Press, 1977.

## Open Questions

- Whether an 1820s prototype or horse-railroad milestone should be captured in notes but excluded from the canonical row.
- Whether route miles or ton-miles should be the default adoption series in the first compiled dataset.

## QA Notes

- Dependency check: The chosen dependencies all predate the 1830 service boundary.
- T0 check: 1830 reflects operating rail service, not just chartering.
- Metric check: Ton-miles are the strongest long-run substrate measure.
