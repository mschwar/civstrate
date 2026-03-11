```yaml
id: metabolism/internal_combustion_engine
domain: Metabolism
subdomain: Engines
technology: Internal Combustion Engine
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: metabolism/oil_refining
invention_year: 1876
invention_year_defense: Nikolaus Otto's 1876 four-stroke engine is the cleanest practical invention boundary because it was the first reliable internal-combustion engine that became an immediate commercial alternative to steam power.
us_commercial_launch_year: 1885
us_commercial_launch_defense: 1885 is the strongest current U.S. commercial launch year because Otto-licensed engines were being built and sold in the United States by then, establishing a real American market for practical internal-combustion prime movers before the later auto boom.
fundamental_scaling_metric: Cost per horsepower-hour delivered.
recommended_us_adoption_metric: Share of U.S. freight ton-miles or vehicle-miles powered by internal-combustion engines, with engine shipments as a supporting early series.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Still a foundational power plant for road freight, aviation, construction equipment, and backup power despite electrification pressure.
confidence: medium
notes: Uses the early U.S. stationary-engine market rather than vehicle commercialization as canonical T0; later automotive and diesel milestones remain downstream expansions of the substrate. Tier 1 diffusion attempt deferred because no single national direct-adoption series spans stationary engines, road vehicles, farm machinery, aviation, and other internal-combustion uses without a disputed proxy choice.
```

# Internal Combustion Engine

## Identity

- `Domain`: Metabolism
- `Subdomain`: Engines
- `Technology`: Internal Combustion Engine
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers practical internal-combustion prime movers as a substrate for transport, mobile machinery, and distributed mechanical power, not any single branded vehicle platform.
- It is in scope because it became a durable cross-sector power layer linking refined fuels to automobiles, trucks, tractors, ships, aviation, and industrial equipment [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- `metabolism/oil_refining`: Practical internal-combustion deployment depended on refined liquid fuels, especially gasoline and later diesel, as a portable high-energy input [1, 2].
- Practical engines also required metallurgy, precision machining, and machine tools capable of producing repeatable cylinders, valves, bearings, and ignition systems.
- Later U.S. scale-up also depended on road networks, fueling distribution, and mass manufacturing systems, but those are treated as downstream complements rather than core invention-stage prerequisites [2, 3].

## Phase 1 Claims

- `Invention Year`: 1876  
  Defense: Otto's 1876 four-stroke engine is the clearest practical boundary because Britannica identifies it as the first practical internal-combustion engine and an immediate alternative to steam power [1, 2].

- `U.S. Commercial Launch (T0)`: 1885  
  Defense: 1885 is the better U.S. launch year because ASME records an Otto-licensed engine built in the United States in that year, showing that practical internal-combustion engines were already entering an American commercial market as stationary prime movers before the later vehicle wave [2, 3].

- `Fundamental Scaling Metric`: Cost per horsepower-hour delivered.

- `Recommended U.S. Adoption Metric`: Share of U.S. freight ton-miles or vehicle-miles powered by internal-combustion engines, with engine shipments as a supporting early series.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Still a foundational power plant for road freight, aviation, construction equipment, and backup power despite electrification pressure.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Encyclopaedia Britannica. "Nikolaus Otto." https://www.britannica.com/biography/Nikolaus-Otto
- [2] Encyclopaedia Britannica. "Internal-combustion engines" in *Energy conversion*. https://www.britannica.com/technology/energy-conversion/Internal-combustion-engines
- [3] American Society of Mechanical Engineers. "Coolspring Power Museum." https://www.asme.org/about-asme/engineering-history/landmarks/215-coolspring-power-museum

## Open Questions

- Whether the canonical row should continue to center the stationary-engine market or later split out diesel and mobile transport engine branches as separate substrate rows.
- Whether the recommended adoption metric should resolve to freight activity, engine shipments, or fuel consumption by internal-combustion applications.

## QA Notes

- PASS
- Dependency check: No chosen dependency postdates the 1876 practical engine boundary.
- T0 check: 1885 is acceptable because it anchors the row to a clearly defined U.S. commercial engine market rather than to early vehicle prototypes.
- Metric check: Direct household ownership is too narrow; the substrate matters through transport and machinery work performed.
