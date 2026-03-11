```yaml
id: metabolism/portland_cement_concrete
domain: Metabolism
subdomain: Materials
technology: Portland Cement Concrete
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies:
invention_year: 1824
invention_year_defense: Joseph Aspdin's 1824 patent is the conventional practical invention boundary for portland cement, the key binder that made modern concrete a scalable industrial substrate.
us_commercial_launch_year: 1875
us_commercial_launch_defense: 1875 is the strongest U.S. commercial launch year because USGS states that by then Saylor had overcome the early process problems and was making high-quality true portland cement commercially in Pennsylvania.
fundamental_scaling_metric: Cost per cubic yard of concrete placed or per ton of cement produced.
recommended_us_adoption_metric: U.S. portland cement consumption or concrete volume used in construction.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: One of the deepest physical substrates in the built environment, embedded in buildings, roads, utilities, dams, and industrial sites.
confidence: medium
notes: Uses 1875 because it is the stronger commercial-quality boundary; the row remains intentionally centered on the cement-plus-concrete material system rather than on cement chemistry in isolation. Tier 1 diffusion attempt deferred because consumption tracks cyclical construction demand and no clean saturation denominator is yet frozen.
```

# Portland Cement Concrete

## Identity

- `Domain`: Metabolism
- `Subdomain`: Materials
- `Technology`: Portland Cement Concrete
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers portland-cement-based concrete as a mass structural substrate, not decorative masonry or a single specialty concrete technique.
- It is in scope because it underlies roads, bridges, buildings, dams, utilities, and sanitation systems and is measurable through cement output and concrete use at national scale [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Limestone, clay, and aggregate supply at industrial scale [2].
- High-temperature kilns and fuel inputs capable of continuous cement manufacture [1, 2].
- Heavy transport and construction systems were required to move bulk cement, aggregate, and finished material into large infrastructure and building projects.

## Phase 1 Claims

- `Invention Year`: 1824  
  Defense: 1824 is the cleanest practical boundary because Britannica attributes the invention of portland cement to Aspdin's patent, which established the binder technology behind modern concrete [1].

- `U.S. Commercial Launch (T0)`: 1875  
  Defense: 1875 is the better U.S. launch year because USGS says Saylor had by then overcome the early process flaws and was making a high-quality true portland cement commercially, which is a stronger substrate T0 than the first still-troubled plant start in 1871 [2].

- `Fundamental Scaling Metric`: Cost per cubic yard of concrete placed or per ton of cement produced.

- `Recommended U.S. Adoption Metric`: U.S. portland cement consumption or concrete volume used in construction.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: One of the deepest physical substrates in the built environment, embedded in buildings, roads, utilities, dams, and industrial sites.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Encyclopaedia Britannica. "History of cement." https://www.britannica.com/technology/cement-building-material/History-of-cement
- [2] U.S. Geological Survey. *Background Facts and Issues Concerning Cement and Cement Data*. https://pubs.usgs.gov/of/2005/1152/2005-1152.pdf
- [3] American Cement Association. "How Cement Is Made." https://www.cement.org/cement-concrete/how-cement-is-made/

## Open Questions

- Whether this row should remain `portland_cement_concrete` or narrow to `portland_cement` for cleaner analytical separability from downstream structural systems.
- Whether U.S. adoption should be tracked through cement consumption, ready-mix concrete output, or specific infrastructure applications such as road lane-miles.

## QA Notes

- PASS
- Dependency check: Chosen dependencies precede industrial cement production.
- T0 check: 1875 is acceptable because it marks the first clearly commercial-quality U.S. production rather than an experimental plant start with unresolved process issues.
- Metric check: Volume consumed or produced is preferable to counting firms or projects.
