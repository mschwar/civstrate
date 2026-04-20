```yaml
id: vascular/pipelines
domain: Vascular
subdomain: Logistics
technology: Pipelines
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: metabolism/oil_refining
invention_year: 1879
invention_year_defense: 1879 is the strongest practical invention boundary because the Tidewater line demonstrated the first successful long-distance oil pipeline capable of displacing barrel-and-rail transport.
us_commercial_launch_year: 1879
us_commercial_launch_defense: The same 1879 Tidewater operation is the clearest U.S. commercial launch because shippers could use pipeline transport as an operating freight service rather than as an experimental line.
fundamental_scaling_metric: Cost per barrel-mile delivered.
recommended_us_adoption_metric: U.S. pipeline ton-miles moved, with total trunk pipeline mileage as a supporting diffusion series.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Core bulk-transport substrate for crude oil, refined products, natural gas, and many industrial feedstocks.
confidence: medium
notes: Centers the modern long-distance fuel-and-feedstock pipeline substrate rather than ancient or municipal pipe systems; later splitting crude/product and gas pipelines remains open. Tier 1 diffusion attempt deferred because mileage and throughput series diverge across crude, product, and gas networks without one canonical threshold denominator.
```

# Pipelines

## Identity

- `Domain`: Vascular
- `Subdomain`: Logistics
- `Technology`: Pipelines
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers long-distance industrial pipelines for moving fuels and feedstocks, not municipal water pipes or short on-site process piping.
- It is in scope because it became a durable bulk transport layer with major dependency depth across refining, gas distribution, petrochemicals, and power generation [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Steel pipe and joining methods strong enough for pressurized long-distance transport [1].
- Pumping power, valves, and flow-control equipment able to maintain continuous operation.
- Oil and gas production plus refining demand sufficient to justify dedicated trunk transport corridors [2].

## Phase 1 Claims

- `Invention Year`: 1879  
  Defense: 1879 is the cleanest practical boundary because Britannica identifies the Tidewater line as the world's first successful oil pipeline, proving long-distance pipeline transport as a working freight substrate [1].

- `U.S. Commercial Launch (T0)`: 1879  
  Defense: The same Tidewater line is the strongest U.S. commercial launch because crude oil was flowing for shipment as a live transport service rather than as a one-off engineering demonstration [1, 2].

- `Fundamental Scaling Metric`: Cost per barrel-mile delivered.

- `Recommended U.S. Adoption Metric`: U.S. pipeline barrel-miles or ton-miles moved, with total trunk pipeline mileage as a supporting diffusion series.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Core bulk-transport substrate for crude oil, refined products, natural gas, and many industrial feedstocks.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Encyclopaedia Britannica. "Pipeline." https://www.britannica.com/technology/pipeline-technology
- [2] Encyclopaedia Britannica. "How the world's first oil pipeline was built." https://www.britannica.com/video/180118/Overview-oil-pipeline-Standard-Oil-Company-and
- [3] U.S. Department of Energy. "How it Works: Refined Petroleum Product Pipelines." https://www.energy.gov/sites/default/files/2023-08/Pipeline%20Backgrounder_FINAL_508.pdf

## Open Questions

- Whether the row should remain a broad pipeline substrate or later split into crude/product pipelines and natural-gas pipelines.
- Whether the best long-run adoption measure is mileage, throughput, or an energy-delivery measure tied to U.S. fuel consumption.

## QA Notes

- PASS
- Dependency check: The current dependency list points to industrial materials and pumping prerequisites, not later logistics layers.
- T0 check: The Tidewater boundary is defensible for pipelines as a commercial transport substrate and aligns invention with live freight service.
- Metric check: Throughput-based measures are better than operator or asset counts.
