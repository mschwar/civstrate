```yaml
id: vascular/containerization
domain: Vascular
subdomain: Logistics
technology: Containerization
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: vascular/railroads;vascular/freight_trucking
invention_year: 1956
invention_year_defense: The 1956 voyage of the Ideal X is the clearest practical invention boundary because it demonstrated modern containerized intermodal shipping in working service.
us_commercial_launch_year: 1956
us_commercial_launch_defense: The same Ideal X operation marks U.S. commercial launch because container shipping was used in revenue service rather than as a laboratory or military-only experiment.
fundamental_scaling_metric: Cost per ton handled or shipped in intermodal service.
recommended_us_adoption_metric: TEUs handled in U.S. ports, with container share of freight as a supporting metric.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Standard containerized handling is now the default backbone for large parts of maritime and intermodal freight.
confidence: high
notes: 1956 launch precedes the later ISO standardization milestone of the 1960s. Tier 1 diffusion attempt deferred because TEU series are strong later but do not yet provide one clean early national threshold baseline from launch onward.
```

# Containerization

## Identity

- `Domain`: Vascular
- `Subdomain`: Logistics
- `Technology`: Containerization
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers standardized intermodal freight containers and the associated handling system, not just a shipping box as an isolated artifact.
- It is in scope because it changed port operations, trucking, rail intermodal logistics, and global trade structure in a durable and measurable way [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Railroads and trucking
- Port infrastructure and cranes
- Standardized handling equipment and container specifications [1, 2]

## Phase 1 Claims

- `Invention Year`: 1956  
  Defense: The 1956 voyage of the *Ideal X* is the clearest practical invention boundary because it demonstrated modern containerized intermodal shipping in working service [1, 2].

- `U.S. Commercial Launch (T0)`: 1956  
  Defense: The same *Ideal X* operation marks U.S. commercial launch because container shipping was used in revenue service rather than as a laboratory or military-only experiment [1, 2].

- `Fundamental Scaling Metric`: Cost per ton handled or shipped in intermodal service.

- `Recommended U.S. Adoption Metric`: TEUs handled in U.S. ports, with container share of freight as a supporting metric.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Standard containerized handling is now the default backbone for large parts of maritime and intermodal freight.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] U.S. Maritime Administration. Historical materials and annual reports on containerization and the *Ideal X*. https://www.maritime.dot.gov/
- [2] Levinson, Marc. *The Box: How the Shipping Container Made the World Smaller and the World Economy Bigger*. Princeton University Press, 2006.

## Open Questions

- Whether ISO standardization in the 1960s should be treated as a later maturity milestone distinct from the 1956 launch.
- Whether TEUs or containerized share of freight should be the main adoption series.

## QA Notes

- Dependency check: Containerization depends on preexisting freight systems and port machinery.
- T0 check: 1956 is tied to revenue service.
- Metric check: Throughput is the correct diffusion lens, not box ownership.
