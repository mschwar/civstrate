```yaml
id: metabolism/bessemer_steel
domain: Metabolism
subdomain: Materials
technology: Bessemer Steel
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies:
invention_year: 1856
invention_year_defense: Henry Bessemer's 1856 converter announcement is the standard practical invention boundary because it demonstrated a repeatable process for mass steelmaking.
us_commercial_launch_year: 1865
us_commercial_launch_defense: 1865 is the clearest U.S. commercial launch because the first successful U.S. Bessemer steel works began producing saleable steel in that period.
fundamental_scaling_metric: Cost per ton of steel.
recommended_us_adoption_metric: Tons of U.S. steel output produced with the Bessemer process or Bessemer-era steel rail output.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: The Bessemer process itself was superseded, but low-cost steel remained a permanent civilizational substrate.
confidence: medium
notes: 1864 versus 1865 remains a minor normalization question for U.S. launch. Tier 1 diffusion attempt deferred because the Bessemer process was later superseded, so any threshold series is unstable between process adoption and the broader steel substrate it enabled.
```

# Bessemer Steel

## Identity

- `Domain`: Metabolism
- `Subdomain`: Materials
- `Technology`: Bessemer Steel
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers bulk low-cost steel made with the Bessemer process as a foundational material substrate for rails, structures, machinery, and later industrial systems.
- It is in scope because it is measurable in tons, deeply enabling for later substrates, and clearly distinct from downstream finished products [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Ironmaking
- Coke or other high-heat furnace fuel
- Ore supply and heavy transport [1, 2]

## Phase 1 Claims

- `Invention Year`: 1856  
  Defense: Henry Bessemer's 1856 converter announcement is the standard practical invention boundary because it demonstrated a repeatable process for mass steelmaking [1].

- `U.S. Commercial Launch (T0)`: 1865  
  Defense: 1865 is the clearest U.S. commercial launch because the first successful U.S. Bessemer steel works began producing saleable steel in that period [2, 3].

- `Fundamental Scaling Metric`: Cost per ton of steel.

- `Recommended U.S. Adoption Metric`: Tons of U.S. steel output produced with the Bessemer process or Bessemer-era steel rail output.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: The Bessemer process itself was superseded, but low-cost steel remained a permanent civilizational substrate.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Encyclopaedia Britannica. "Bessemer process." https://www.britannica.com/technology/Bessemer-process
- [2] IEEE Engineering and Technology History Wiki. "Milestones: America's First Bessemer Steel Mill, Wyandotte, MI, 1864-1865." https://ethw.org/
- [3] World Steel Association. Historical materials on the Bessemer process and modern steelmaking. https://worldsteel.org/

## Open Questions

- Whether 1864 or 1865 should be the final U.S. commercial launch year after tighter source normalization.
- Whether later steelmaking processes should be separate rows or grouped as post-Bessemer successors.

## QA Notes

- Dependency check: The chosen dependencies all predate commercial Bessemer steel.
- T0 check: The date points to actual mill output, not a patent only.
- Metric check: Output tons are the right substrate measure.
