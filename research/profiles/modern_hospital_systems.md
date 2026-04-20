```yaml
id: immune_system/modern_hospital_systems
domain: Immune_System
subdomain: Care_Delivery
technology: Modern Hospital Systems
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: immune_system/municipal_sanitation;immune_system/water_filtration_and_chlorination;metabolism/electricity
invention_year: 1946
invention_year_defense: 1946 is the strongest practical invention boundary for the modern U.S. hospital-system substrate because Hill-Burton created a coordinated federal-state program to survey, finance, and build a nationwide acute-care hospital network.
us_commercial_launch_year: 1946
us_commercial_launch_defense: 1946 is also the clearest U.S. public-deployment boundary because Hill-Burton immediately authorized grants to states for hospital and public health center construction rather than merely studying the problem.
fundamental_scaling_metric: Cost per adjusted patient day or staffed bed-day delivered.
recommended_us_adoption_metric: Share of U.S. population with access to community hospital beds (per 1,000 population), with staffed acute-care hospital admissions or discharges as supporting series.
denominator: Population
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Core care-delivery substrate for inpatient acute medicine, trauma, surgery, and advanced diagnostics, though bed intensity and organizational form have shifted over time.
confidence: medium
notes: This row is intentionally scoped to the post-1946 modern hospital network and not to earlier almshouses, charitable hospitals, or one-off specialty institutions. Tier 1 diffusion attempt deferred because hospital-capacity series shift across bed definitions, community-hospital scope, and system consolidation, making one clean national threshold run unstable.
```

# Modern Hospital Systems

## Identity

- `Domain`: Immune_System
- `Subdomain`: Care_Delivery
- `Technology`: Modern Hospital Systems
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers the postwar U.S. acute-care hospital network as an organized care-delivery substrate, not the pre-1800 hospital tradition and not any single hospital brand.
- It is in scope because hospitals became a nationwide high-capacity infrastructure for surgery, trauma, diagnostics, intensive care, and medical coordination, with measurable bed capacity and strong dependency depth across the rest of the health system [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Urban sanitation and treated water systems that made large inpatient facilities viable [3].
- Electricity and modern building services for lighting, sterilization, imaging, ventilation, and around-the-clock operations.
- Public-health and financing institutions able to support a geographically distributed care network at national scale [1, 2].

## Phase 1 Claims

- `Invention Year`: 1946  
  Defense: 1946 is the strongest practical boundary because the Hill-Burton Act created a coordinated federal-state system for surveying needs and building the hospital infrastructure of the modern U.S. inpatient network [1, 2].

- `U.S. Commercial Launch (T0)`: 1946  
  Defense: 1946 is the clearest launch year because the same act authorized grants for hospital and public-health-center construction immediately, turning planning into deployable infrastructure rather than keeping hospitals as a patchwork of local institutions [2, 3].

- `Fundamental Scaling Metric`: Cost per adjusted patient day or staffed bed-day delivered.

- `Recommended U.S. Adoption Metric`: Community-hospital beds per 1,000 population, with staffed acute-care hospital admissions or discharges as supporting series.

- `Denominator`: Population

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Core care-delivery substrate for inpatient acute medicine, trauma, surgery, and advanced diagnostics, though bed intensity and organizational form have shifted over time.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] American Hospital Association. "AHA 125th Anniversary, 1898-2023." https://www.aha.org/125
- [2] U.S. Department of Health and Human Services, HRSA Maternal & Child Health Bureau. "1946: Hill-Burton Act." https://mchb.hrsa.gov/about-us/timeline/text
- [3] National Institutes of Health. "Legislative Chronology." https://www.nih.gov/about-nih/nih-almanac/legislative-chronology
- [4] PubMed. "An Architectural History of US Community Hospitals." https://pubmed.ncbi.nlm.nih.gov/30893044/

## Open Questions

- Whether the row should remain `modern_hospital_systems` or later split between the postwar hospital buildout and later integrated health-system governance.
- Whether beds per capita alone is sufficient or whether admissions, staffed beds, and ICU-capacity measures should be paired for later phases.

## QA Notes

- PASS
- Dependency check: The listed dependencies predate 1946 and reflect facility prerequisites rather than later reimbursement or IT layers.
- T0 check: 1946 is acceptable because Hill-Burton authorized actual hospital-system buildout, not only advisory planning.
- Metric check: Beds per capita is an appropriate first-pass infrastructure measure for a hospital-system substrate.
