```yaml
id: vascular/refrigerated_logistics_cold_chain
domain: Vascular
subdomain: Logistics
technology: Refrigerated Logistics Cold Chain
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: vascular/railroads
invention_year: 1877
invention_year_defense: 1877 is the strongest practical invention boundary because Swift's successful refrigerated rail shipment showed that perishable goods could move long distance in a controlled cold chain rather than only through local storage or seasonal ice.
us_commercial_launch_year: 1877
us_commercial_launch_defense: 1877 is the clearest U.S. commercial launch year because Swift used the refrigerator car in revenue meat distribution, proving a live logistics service rather than an isolated engineering trial.
fundamental_scaling_metric: Cost per ton-mile delivered under refrigerated conditions.
recommended_us_adoption_metric: Refrigerated warehouse cubic capacity, with refrigerated car and trailer capacity as supporting transport series.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Core perishables logistics substrate spanning food, pharmaceuticals, biologics, and temperature-sensitive retail distribution.
confidence: medium
notes: Uses the first successful refrigerated meat-shipping system as the canonical origin, while later mechanical refrigeration and highway reefer networks are treated as major scaling phases. Tier 1 diffusion attempt deferred because refrigerated warehouse, railcar, and trailer-capacity series do not yet combine into one clean chain-wide national threshold series.
```

# Refrigerated Logistics Cold Chain

## Identity

- `Domain`: Vascular
- `Subdomain`: Logistics
- `Technology`: Refrigerated Logistics Cold Chain
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers the integrated logistics substrate for storing and moving temperature-sensitive goods under controlled cold conditions, not domestic refrigerators and not food freezing as a consumer appliance story.
- It is in scope because it changed national food distribution, widened perishables markets, and later became essential for pharmaceuticals, vaccines, and biologics [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Rail transport and later road freight systems able to carry temperature-controlled cargo at scale [1].
- Ice production and then mechanical refrigeration technologies that made consistent cold conditions possible [2, 3].
- Warehousing and handling systems for transfer, staging, and storage of perishable goods throughout the chain.

## Phase 1 Claims

- `Invention Year`: 1877  
  Defense: 1877 is the strongest practical boundary because Britannica identifies Swift's first successful refrigerator-car shipment of fresh meat to the East as the breakthrough that made long-distance refrigerated distribution workable [1].

- `U.S. Commercial Launch (T0)`: 1877  
  Defense: 1877 is also the clearest U.S. launch year because the same Swift shipment operated within a live commercial meat-distribution business rather than a laboratory or exhibition setting [1].

- `Fundamental Scaling Metric`: Cost per ton-mile delivered under refrigerated conditions.

- `Recommended U.S. Adoption Metric`: Refrigerated warehouse cubic capacity, with refrigerated car and trailer capacity as supporting transport series.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Core perishables logistics substrate spanning food, pharmaceuticals, biologics, and temperature-sensitive retail distribution.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Encyclopaedia Britannica. "Gustavus Swift." https://www.britannica.com/money/Gustavus-Swift
- [2] U.S. Department of Agriculture, NASS. "Directory of Refrigerated Warehouses." https://esmis.nal.usda.gov/concern/publications/db78tc02w
- [3] U.S. Department of Agriculture, NASS. "Trends in U.S. Agriculture: Cold Storage." https://www.nass.usda.gov/Publications/Trends_in_U.S._Agriculture/Cold_Storage/index.php
- [4] U.S. National Park Service. "Moving Goods by Rail." https://www.nps.gov/articles/000/moving-goods-by-rail-article.htm

## Open Questions

- Whether the row should remain broad as `refrigerated_logistics_cold_chain` or later split between food cold chain and biologics/pharmaceutical cold chain.
- Whether refrigerated warehouse capacity is sufficient as the canonical adoption series or whether a transport-capacity series should lead instead.

## QA Notes

- PASS
- Dependency check: The listed dependencies predate the 1877 refrigerated-shipping breakthrough and align with cold-chain logistics rather than later retail appliances.
- T0 check: 1877 is acceptable because the refrigerator car was already being used in revenue distribution.
- Metric check: Capacity and refrigerated ton-mile style measures are preferable to counts of consumer refrigerators.
