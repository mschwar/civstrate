```yaml
id: nervous_system/telephone
domain: Nervous_System
subdomain: Communications
technology: Telephone
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: nervous_system/telegraph
invention_year: 1876
invention_year_defense: Bell's 1876 patent and successful first call are the most defensible practical invention boundary for the telephone as a working voice-transmission system.
us_commercial_launch_year: 1878
us_commercial_launch_defense: 1878 is the stronger commercial launch year because the first commercial exchange transformed the telephone from an invention into a purchasable network service.
fundamental_scaling_metric: Cost per subscriber connection or call carried over distance.
recommended_us_adoption_metric: Household telephone penetration.
denominator: Population
t10_years: 42
t25_years: 42
t50_years: 72
t75_years: 82
peak_adoption_or_current_status: Legacy fixed-line telephony has declined, but the telephone network model remained foundational for later communications.
confidence: medium
notes: 1877 company formation is treated as precursor; 1878 exchange service is canonical T0. Tier 1 diffusion series uses FCC household telephone-penetration estimates; because the standardized national household series begins in 1920 at 35.0 percent, T10 and T25 are first-observed threshold years rather than exact first crossings.
```

# Telephone

## Identity

- `Domain`: Nervous_System
- `Subdomain`: Communications
- `Technology`: Telephone
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers switched voice telephony as a networked coordination substrate, not merely the handset as a consumer device.
- It is in scope because it diffused across homes, firms, and institutions; it is measurable in subscriber lines and penetration; and it became an enduring coordination layer for the U.S. economy [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Telegraph-era wiring and pole infrastructure
- Acoustic-electrical transduction equipment and switchboards
- Large-scale rollout later depended on grid power and improved long-distance transmission [1, 2]

## Phase 1 Claims

- `Invention Year`: 1876  
  Defense: Bell's 1876 patent and successful first call are the most defensible practical invention boundary for the telephone as a working voice-transmission system [1].

- `U.S. Commercial Launch (T0)`: 1878  
  Defense: 1878 is the stronger commercial launch year because the first commercial exchange transformed the telephone from an invention into a purchasable network service [2].

- `Fundamental Scaling Metric`: Cost per subscriber connection or call carried over distance.

- `Recommended U.S. Adoption Metric`: Telephones per 100 U.S. residents or household telephone penetration.

- `Denominator`: Population

## Diffusion Milestones

- Canonical Tier 1 series: FCC historical household telephone-penetration estimates, which the FCC traces to *Historical Statistics of the United States* for 1920-1970 [3].
- `T10`: 42 years. The first standardized national household series point is already 35.0 percent in 1920, so the profile records 1920 as the first observed threshold year after the 1878 launch [3].
- `T25`: 42 years. The same 1920 observation is also the first observed point above 25 percent [3].
- `T50`: 72 years. FCC historical estimates put household penetration at 61.8 percent in 1950 [3].
- `T75`: 82 years. FCC historical estimates put household penetration at 78.3 percent in 1960 [3].
- `Peak Adoption / Current Status`: Legacy fixed-line telephony has declined, but the telephone network model remained foundational for later communications.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Library of Congress. "Invention of the Telephone: Topics in Chronicling America." https://guides.loc.gov/chronicling-america-telephone-invention
- [2] Fischer, Claude S. *America Calling: A Social History of the Telephone to 1940*. University of California Press, 1992.
- [3] Federal Communications Commission. *Trends in Telephone Service*, Table 17.3 "Historical Telephone Penetration Estimates," 2000. https://docs.fcc.gov/public/attachments/DOC-215526A1.pdf

## Open Questions

- Whether 1877 company formation or 1878 exchange service should be the final T0 boundary.
- Whether the adoption denominator should settle on population or households once a single historical series is selected.

## QA Notes

- Dependency check: Telephone follows telegraph-era infrastructure and basic electrical signaling.
- T0 check: 1878 represents exchange service, not patent paperwork alone.
- Metric check: Penetration and subscriber lines fit better than handset unit sales.
