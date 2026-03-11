```yaml
id: nervous_system/semiconductors
domain: Nervous_System
subdomain: Compute
technology: Semiconductors
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: metabolism/electricity
invention_year: 1947
invention_year_defense: The Bell Labs transistor announcement marks the practical invention boundary because it demonstrated a working solid-state alternative to vacuum tubes.
us_commercial_launch_year: 1951
us_commercial_launch_defense: 1951 is the best current launch year because commercially manufactured junction transistors were entering the market by then, allowing firms to buy semiconductor devices as industrial inputs.
fundamental_scaling_metric: Cost per transistor or compute delivered per dollar.
recommended_us_adoption_metric: U.S. GDP exposure to semiconductor-dependent sectors, with semiconductor industry output as a supporting series.
denominator: GDP
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Foundational dependency across computation, communications, industrial control, and consumer electronics.
confidence: medium
notes: 1951 is retained for T0, but 1954 remains a plausible alternative normalization candidate. Tier 1 diffusion attempt deferred because indirect GDP exposure remains the right lens, but the corresponding milestone method is not yet stable enough for reproducible thresholds.
```

# Semiconductors

## Identity

- `Domain`: Nervous_System
- `Subdomain`: Compute
- `Technology`: Semiconductors
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile treats semiconductors as the device layer beginning with the transistor and extending into the modern chip industry, not as consumer electronics.
- It is in scope because it underlies later compute and communications substrates, is measurable through output, capital stock, and GDP exposure, and functions as one of the deepest enabling layers in the modern economy [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Electricity
- Precision materials and manufacturing
- Vacuum-tube-era electronics knowledge and clean fabrication processes [1, 2]

## Phase 1 Claims

- `Invention Year`: 1947  
  Defense: The Bell Labs transistor announcement marks the practical invention boundary because it demonstrated a working solid-state alternative to vacuum tubes [1, 2].

- `U.S. Commercial Launch (T0)`: 1951  
  Defense: 1951 is the best current launch year because commercially manufactured junction transistors were entering the market by then, allowing firms to buy semiconductor devices as industrial inputs [1, 3].

- `Fundamental Scaling Metric`: Cost per transistor or compute delivered per dollar.

- `Recommended U.S. Adoption Metric`: U.S. GDP exposure to semiconductor-dependent sectors, with semiconductor industry output as a supporting series.

- `Denominator`: GDP

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Foundational dependency across computation, communications, industrial control, and consumer electronics.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Computer History Museum. "The Silicon Engine | 1947-1958: Invention of the Transistor / First Commercial Junction Transistor." https://www.computerhistory.org/siliconengine/
- [2] Nokia Bell Labs. "The Transistor." https://www.bell-labs.com/about/our-history/milestones/transistor/
- [3] Riordan, Michael, and Lillian Hoddeson. *Crystal Fire: The Invention of the Transistor and the Birth of the Information Age*. W. W. Norton, 1997.

## Open Questions

- Whether 1951 or 1954 is the best long-run T0 once a single shipment-based source is standardized.
- Whether GDP exposure should eventually be operationalized through BEA input-output tables or capital-stock measures first.

## QA Notes

- Dependency check: The dependencies all predate the transistor.
- T0 check: The current date points to commercial device availability rather than only the Bell Labs lab result.
- Metric check: Direct household ownership is incorrect; indirect exposure is the right lens.
