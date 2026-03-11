```yaml
id: nervous_system/microprocessors
domain: Nervous_System
subdomain: Compute
technology: Microprocessors
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: nervous_system/semiconductors
invention_year: 1971
invention_year_defense: 1971 is the cleanest practical invention boundary because Intel completed and released the 4004, the first programmable microprocessor, as a working general-purpose logic device on a chip.
us_commercial_launch_year: 1971
us_commercial_launch_defense: 1971 is also the strongest U.S. commercial launch year because Intel introduced the 4004 into the market that year for commercial use rather than as a lab-only prototype.
fundamental_scaling_metric: Cost per unit of compute delivered.
recommended_us_adoption_metric: U.S. shipments or installed base of microprocessor-powered computing devices, with semiconductor compute capacity as a supporting exposure series.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Foundational compute substrate embedded in PCs, servers, industrial control, vehicles, phones, and many later digital systems.
confidence: high
notes: Narrower than semiconductors and intended to capture the CPU-on-a-chip architectural break; the long-run adoption series may later need an exposure metric instead of pure device counts. Tier 1 diffusion attempt deferred because device counts understate embedded diffusion while compute-exposure metrics are not yet normalized.
```

# Microprocessors

## Identity

- `Domain`: Nervous_System
- `Subdomain`: Compute
- `Technology`: Microprocessors
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers the general-purpose CPU on a chip as a substrate for programmable digital systems, not semiconductors as a whole and not a single PC era product.
- It is in scope because it created a distinct bridge from semiconductors to personal computing, embedded control, servers, networking gear, and later cloud and AI stacks [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Semiconductor device fabrication and integrated-circuit manufacturing [1, 2].
- Precision materials, lithography, and packaging sufficient to place programmable logic on a single chip.
- Computer architecture and software toolchains that made the chip a reusable programmable platform rather than a fixed-function component.

## Phase 1 Claims

- `Invention Year`: 1971  
  Defense: 1971 is the cleanest practical invention boundary because Intel identifies the 4004 as the first programmable microprocessor and a completed working product [1, 2].

- `U.S. Commercial Launch (T0)`: 1971  
  Defense: 1971 is the strongest U.S. launch year because Intel introduced the 4004 commercially that year, making microprocessors purchasable devices rather than internal research artifacts [1, 3].

- `Fundamental Scaling Metric`: Cost per unit of compute delivered.

- `Recommended U.S. Adoption Metric`: U.S. shipments or installed base of microprocessor-powered computing devices, with semiconductor compute capacity as a supporting exposure series.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Foundational compute substrate embedded in PCs, servers, industrial control, vehicles, phones, and many later digital systems.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Intel. "Announcing a New Era of Integrated Electronics: The Intel 4004." https://www.intel.com/content/www/us/en/history/virtual-vault/articles/the-intel-4004.html
- [2] Intel. "The Intel 8008." https://www.intel.com/content/www/us/en/history/virtual-vault/articles/the-8008.html
- [3] Intel. "Intel Marks 30th Anniversary of the Microprocessor." https://www.intel.com/pressroom/archive/releases/2001/20011115corp_a.htm

## Open Questions

- Whether the canonical adoption metric should center on PC/server shipments, broader embedded-device penetration, or an exposure metric tied to U.S. compute capacity.
- Whether the launch year should remain at 1971 with the 4004 or shift to 1972-1974 when broader non-calculator use became clearer.

## QA Notes

- PASS
- Dependency check: The profile correctly sits downstream of semiconductors rather than replacing them.
- T0 check: 1971 is acceptable because the 4004 was an introduced commercial product, even if its first use case was narrow.
- Metric check: Device counts alone may understate embedded diffusion, so a paired exposure series may be useful later.
