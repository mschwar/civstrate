```yaml
id: vascular/freight_trucking
domain: Vascular
subdomain: Freight
technology: Freight Trucking
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: metabolism/internal_combustion_engine;metabolism/oil_refining
invention_year: 1896
invention_year_defense: 1896 is the cleanest practical invention boundary because the first motor truck was built that year, establishing the dedicated freight-carrying truck as a distinct vehicle class.
us_commercial_launch_year: 1911
us_commercial_launch_defense: 1911 is the strongest current U.S. commercial launch year because FHWA identifies that year's transcontinental truck trip and motor truck show as the point when freight motor carriage had clearly grown to economic importance as a working freight service.
fundamental_scaling_metric: Cost per ton-mile.
recommended_us_adoption_metric: U.S. truck freight ton-miles.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Dominant U.S. door-to-door freight substrate and the key connective tissue between ports, warehouses, rail, and retail distribution.
confidence: medium
notes: Uses 1911 to represent trucking as a recognizably operating freight substrate rather than merely the first saleable truck vehicle. Tier 1 diffusion attempt deferred because truck ton-miles capture freight work well but do not yet have a frozen saturation denominator across modal substitution.
```

# Freight Trucking

## Identity

- `Domain`: Vascular
- `Subdomain`: Freight
- `Technology`: Freight Trucking
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers motor-truck freight service as a logistics substrate, not passenger automobiles or a single truck manufacturer.
- It is in scope because it became the dominant last-mile and short-to-medium-haul freight layer in the United States and later a major intercity freight system tightly coupled to roads, warehouses, ports, and retail supply chains [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Practical internal-combustion engines and refined liquid fuels for mobile freight service [1].
- Road and highway networks able to support recurring commercial vehicle traffic at scale [2].
- Warehousing, loading equipment, and later trailer/container interfaces that made trucking a system layer rather than a novelty vehicle [2, 3].

## Phase 1 Claims

- `Invention Year`: 1896  
  Defense: 1896 is the best current invention boundary because Britannica identifies that year as the first motor truck, which cleanly separates freight trucks from passenger automobiles and horse wagons [1].

- `U.S. Commercial Launch (T0)`: 1911  
  Defense: 1911 is the better U.S. launch year because FHWA identifies the first transcontinental motor-truck trip and the first Motor Truck Show as the point when the freight motor carrier had grown to real economic importance rather than remaining a niche vehicle novelty [2].

- `Fundamental Scaling Metric`: Cost per ton-mile.

- `Recommended U.S. Adoption Metric`: U.S. truck freight ton-miles.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Dominant U.S. door-to-door freight substrate and the key connective tissue between ports, warehouses, rail, and retail distribution.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Encyclopaedia Britannica. "Truck." https://www.britannica.com/technology/truck-vehicle
- [2] Federal Highway Administration. "Moving the Goods: As the Interstate Era Begins." https://www.fhwa.dot.gov/infrastructure/freight.cfm
- [3] Library of Congress. "Historical Background - The Trucking Industry: A Research Guide." https://guides.loc.gov/trucking-industry/historical-background

## Open Questions

- Whether the canonical T0 should remain 1911 or move slightly later to wartime and postwar freight-service expansion in the 1910s.
- Whether ton-miles alone is sufficient or whether a paired series with truck vehicle-miles is needed for early diffusion.

## QA Notes

- PASS
- Dependency check: Trucking follows the engine and roadway stack rather than preceding it.
- T0 check: 1911 is acceptable because it ties the row to a functioning freight-carrier market rather than only to vehicle saleability.
- Metric check: Ton-miles best preserve the freight substrate distinction from mere truck counts.
