```yaml
id: immune_system/municipal_sanitation
domain: Immune_System
subdomain: Sanitation
technology: Municipal Sanitation
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies:
invention_year: 1855
invention_year_defense: 1855 is the best current practical invention boundary because Chicago created its Board of Sewerage Commissioners and commissioned what contemporary city histories describe as the first comprehensive underground sewer plan in the United States.
us_commercial_launch_year: 1856
us_commercial_launch_defense: 1856 is the stronger U.S. public-deployment boundary because construction of Chicago's comprehensive sewer system had begun, meaning municipalities were utilizing the technology in operating public works rather than only planning it.
fundamental_scaling_metric: Cost per capita served or per million gallons collected and treated.
recommended_us_adoption_metric: Share of the U.S. urban population served by municipal sewerage and related sanitation systems.
denominator: Population
t10_years: 4
t25_years: 24
t50_years: 44
t75_years: 64
peak_adoption_or_current_status: Municipal sanitation is a persistent public-health substrate with near-universal expectation in dense urban areas.
confidence: medium
notes: This row currently centers sewerage; treated-water milestones may later split into a separate substrate. Diffusion milestones use the estimated percentage of the U.S. urban population served by sewers (Joel Tarr / National Research Council).
```

# Municipal Sanitation

## Identity

- `Domain`: Immune_System
- `Subdomain`: Sanitation
- `Technology`: Municipal Sanitation
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers city-scale sanitation infrastructure, especially sewerage and related public-health systems, as a substrate that preserves urban population health and labor capacity.
- It qualifies because it is measurable in population served and treatment capacity, changed disease exposure at system scale, and became an enduring prerequisite for dense modern urban life [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Civil engineering and municipal finance
- Piped water networks, pumping, and drainage works
- Construction materials and urban governance capacity [1, 2]

## Phase 1 Claims

- `Invention Year`: 1855  
  Defense: 1855 is the best current practical invention boundary because Chicago created its Board of Sewerage Commissioners and commissioned what contemporary city histories describe as the first comprehensive underground sewer plan in the United States [1, 2].

- `U.S. Commercial Launch (T0)`: 1856  
  Defense: 1856 is the stronger U.S. public-deployment boundary because construction of Chicago's comprehensive sewer system had begun, meaning municipalities were utilizing the technology in operating public works rather than only planning it [1, 2].

- `Fundamental Scaling Metric`: Cost per capita served or per million gallons collected and treated.

- `Recommended U.S. Adoption Metric`: Share of the U.S. urban population served by municipal sewerage and related sanitation systems.

- `Denominator`: Population

## Diffusion Milestones

- Canonical Tier 1 candidate series: share of U.S. urban population served by municipal sewerage [2, 5].
- `T10`: 4 years (1860). Estimated ~10% of urban population served by buried sewers [5].
- `T25`: 24 years (1880). Estimated ~30% of urban population served [5].
- `T50`: 44 years (1900). Estimated ~50% of urban population served [5].
- `T75`: 64 years (1920). Estimated ~75% of urban population served [5].
- `Peak Adoption / Current Status`: Municipal sanitation is a persistent public-health substrate with near-universal expectation in dense urban areas.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Chicago Public Library. "Chicago Sewers Digital Collection." https://www.chipublib.org/chicago-sewers-digital-collection/
- [2] Melosi, Martin V. *The Sanitary City: Urban Infrastructure in America from Colonial Times to the Present*. Johns Hopkins University Press, 2000.
- [3] Illinois State Archives. "Early Chicago, 1833-1871." https://www.ilsos.gov/departments/archives/teaching_packages/early_chicago/doc31.html
- [4] U.S. Census Bureau. "Historical Census of Housing Tables: Sewage Disposal." https://www2.census.gov/programs-surveys/decennial/tables/time-series/census-housing-tables/sewage.pdf
- [5] Tarr, Joel A. *The Search for the Ultimate Sink: Urban Pollution in Historical Perspective*. University of Akron Press, 1996.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Chicago Public Library. "Chicago Sewers Digital Collection." https://www.chipublib.org/chicago-sewers-digital-collection/
- [2] Melosi, Martin V. *The Sanitary City: Urban Infrastructure in America from Colonial Times to the Present*. Johns Hopkins University Press, 2000.
- [3] Illinois State Archives. "Early Chicago, 1833-1871." https://www.ilsos.gov/departments/archives/teaching_packages/early_chicago/doc31.html
- [4] U.S. Census Bureau. "Historical Census of Housing Tables: Sewage Disposal." https://www2.census.gov/programs-surveys/decennial/tables/time-series/census-housing-tables/sewage.pdf

## Open Questions

- Whether a later treated-water milestone should be split from sewerage rather than folded into the same sanitation row.
- Whether one row should eventually split into `sewerage` and `treated municipal water`.

## QA Notes

- Dependency check: The dependencies all predate the sanitation rollout boundary.
- T0 check: 1856 reflects municipal deployment and construction rather than sanitary theory alone.
- Metric check: Population served is the correct substrate measure.
