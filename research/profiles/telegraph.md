```yaml
id: nervous_system/telegraph
domain: Nervous_System
subdomain: Communications
technology: Telegraph
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies:
invention_year: 1840
invention_year_defense: Morse's U.S. telegraph patent in 1840 is the cleanest practical invention boundary because it marks a working system rather than a speculative concept.
us_commercial_launch_year: 1845
us_commercial_launch_defense: 1845 is the stronger U.S. commercial launch year because telegraph service moved beyond government demonstration into paid public and company operation, including the creation of the Magnetic Telegraph Company and commercial service on the Washington-Baltimore line.
fundamental_scaling_metric: Cost per message-mile.
recommended_us_adoption_metric: Miles of telegraph line in operation in the United States.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Superseded as a standalone mass service, but foundational to later wired communications.
confidence: high
notes: 1844 is preserved in the profile as the operational demonstration milestone; 1845 is canonical T0. Tier 1 diffusion attempt deferred because line-mile and message-volume series do not yet provide one settled saturation denominator for threshold calculations.
```

# Telegraph

## Identity

- `Domain`: Nervous_System
- `Subdomain`: Communications
- `Technology`: Telegraph
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers electrical telegraphy as the first scalable long-distance signaling substrate for near-instant message transmission in the U.S.
- It qualifies because it is measurable in line miles and message traffic, clearly changed coordination across sectors, and underlies later communication systems [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Batteries and electrical signaling apparatus
- Wire, poles, and rights-of-way
- In practice, rail corridors greatly accelerated rollout [1, 2]

## Phase 1 Claims

- `Invention Year`: 1840  
  Defense: Morse's U.S. telegraph patent in 1840 is the cleanest practical invention boundary because it marks a working system rather than a speculative concept [1].

- `U.S. Commercial Launch (T0)`: 1845  
  Defense: 1845 is the stronger U.S. commercial launch year because telegraph service moved beyond government demonstration into paid public and company operation, including the creation of the Magnetic Telegraph Company and commercial service on the Washington-Baltimore line [1, 2].

- `Fundamental Scaling Metric`: Cost per message-mile.

- `Recommended U.S. Adoption Metric`: Miles of telegraph line in operation in the United States.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Superseded as a standalone mass service, but foundational to later wired communications.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Library of Congress. "1840 to 1872 | Samuel F. B. Morse Papers." https://www.loc.gov/collections/samuel-morse-papers/articles-and-essays/timeline/1840-1872/
- [2] Library of Congress. "Reason Gallery C: World's First Telecommunications Company." https://www.loc.gov/exhibits/treasures/tr22c.html
- [3] Standage, Tom. *The Victorian Internet*. Walker & Company, 1998.

## Open Questions

- Whether the dataset should preserve 1844 as an operational demonstration milestone while keeping 1845 as the commercial launch boundary.
- Whether line miles or message volume is the better eventual diffusion series.

## QA Notes

- Dependency check: No listed dependency postdates the telegraph.
- T0 check: 1845 reflects paid public and company service, not only the 1844 demonstration line.
- Metric check: Network extent is the right early diffusion measure.
