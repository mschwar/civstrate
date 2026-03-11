```yaml
id: immune_system/public_health_surveillance
domain: Immune_System
subdomain: Surveillance
technology: Public Health Surveillance
substrate_type: Soft
status: qa_passed
phase: 1
primary_dependencies: nervous_system/telegraph;nervous_system/telephone
invention_year: 1878
invention_year_defense: 1878 is the strongest practical invention boundary because Congress authorized federal collection and publication of morbidity reports, creating the first precursor of recurring U.S. disease surveillance.
us_commercial_launch_year: 1893
us_commercial_launch_defense: 1893 is the clearest U.S. public-deployment boundary because weekly collection from state and municipal authorities established a broader operating surveillance network rather than a narrower quarantine bulletin.
fundamental_scaling_metric: Cost per capita covered or per reportable event processed.
recommended_us_adoption_metric: Share of the U.S. population covered by nationally notifiable disease surveillance and reporting systems.
denominator: Population
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Core coordination substrate for outbreak detection, immunization targeting, public-health response, and routine epidemiological monitoring.
confidence: medium
notes: Centers recurring surveillance infrastructure rather than one publication title such as MMWR; 1925 remains the milestone when all states were reporting regularly. Tier 1 diffusion attempt deferred because no single national population-coverage series runs cleanly from the 1878-1893 launch era through the mature notifiable-disease system.
```

# Public Health Surveillance

## Identity

- `Domain`: Immune_System
- `Subdomain`: Surveillance
- `Technology`: Public Health Surveillance
- `Substrate Type`: Soft

## Scope And Inclusion Note

- This profile covers recurring institutional systems for collecting, aggregating, and disseminating population health surveillance data, not one disease registry and not one publication brand.
- It is in scope because it became a durable coordination layer for outbreak detection, vaccination strategy, and public-health decision-making across jurisdictions [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Public-health agencies and reporting authority at federal, state, and municipal levels [1].
- Vital-statistics and case-reporting practices able to turn local observations into comparable surveillance records [2].
- Communications networks and publication channels for rapid distribution of surveillance information.

## Phase 1 Claims

- `Invention Year`: 1878  
  Defense: 1878 is the best current invention boundary because CDC identifies that year as the first precursor of MMWR and the beginning of federal surveillance-statistics publishing in the United States [1].

- `U.S. Commercial Launch (T0)`: 1893  
  Defense: 1893 is the stronger operating launch year because CDC records that Congress then authorized weekly collection from state and municipal authorities nationwide, creating a broader recurring surveillance network [2].

- `Fundamental Scaling Metric`: Cost per capita covered or per reportable event processed.

- `Recommended U.S. Adoption Metric`: Share of the U.S. population covered by nationally notifiable disease surveillance and reporting systems.

- `Denominator`: Population

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Core coordination substrate for outbreak detection, immunization targeting, public-health response, and routine epidemiological monitoring.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Centers for Disease Control and Prevention. "A History of MMWR." https://www.cdc.gov/mmwr/preview/mmwrhtml/su6004a3.htm
- [2] Centers for Disease Control and Prevention. "History of Morbidity Reporting and Surveillance in the United States." https://stacks.cdc.gov/view/cdc/35267/cdc_35267_DS1.pdf
- [3] Centers for Disease Control and Prevention. *Highlights in Public Health: Notifiable Disease Surveillance and Notifiable Disease Statistics.* https://www.cdc.gov/mmwr/pdf/other/highlite.pdf

## Open Questions

- Whether the canonical T0 should remain 1893 or move later to a point when all states reported regularly.
- Whether population coverage is sufficient or whether timeliness/completeness metrics should eventually be attached for this soft substrate.

## QA Notes

- PASS
- Dependency check: The profile depends on institutional and reporting infrastructure rather than on later digital systems.
- T0 check: 1893 is defensible for recurring multi-jurisdiction collection, while 1878 remains the precursor invention milestone and 1925 the full-state-coverage milestone.
- Metric check: Coverage is the simplest first-pass metric, though later analysis may need quality and latency measures.
