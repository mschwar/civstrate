```yaml
id: nervous_system/radio
domain: Nervous_System
subdomain: Communications
technology: Radio
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: metabolism/electricity;nervous_system/telegraph
invention_year: 1906
invention_year_defense: 1906 is the strongest practical invention boundary because Fessenden's Brant Rock transmission demonstrated long-distance voice-and-music broadcasting rather than point-to-point wireless telegraphy alone.
us_commercial_launch_year: 1920
us_commercial_launch_defense: 1920 is the clearest U.S. commercial launch year because KDKA's election-night broadcast is widely treated as the first commercial U.S. radio broadcast.
fundamental_scaling_metric: Cost per listener-hour delivered.
recommended_us_adoption_metric: Share of U.S. households with a radio receiver.
denominator: Households
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Radio remains a durable mass-audience and emergency-information substrate even after television, internet, and mobile media displaced its peak centrality.
confidence: medium
notes: This row is scoped to broadcast radio as a mass communication substrate, not to wireless telegraphy or later two-way mobile radio systems. Tier 1 diffusion attempt deferred pending normalization of one reproducible national household-radio-ownership table from Historical Statistics and Census sources into exact threshold years.
```

# Radio

## Identity

- `Domain`: Nervous_System
- `Subdomain`: Communications
- `Technology`: Radio
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers broadcast radio as a mass wireless communication substrate, not wireless telegraphy in general and not later cellular or satellite systems.
- It is in scope because it became a national coordination and culture layer, was measurable through household receiver ownership and station growth, and remained important for emergency and public communication long after its first mass-adoption wave [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Electricity and transmitting equipment able to sustain regular broadcasting [1].
- Telegraph-era signaling knowledge and wireless experimentation that preceded broadcast service.
- Precision instrumentation, antennas, and receiver manufacturing sufficient to turn broadcasting into a repeatable household medium [2, 3].

## Phase 1 Claims

- `Invention Year`: 1906  
  Defense: 1906 is the strongest practical boundary because NPS and Britannica both identify Fessenden's Brant Rock broadcast as the first long-distance voice-and-music radio broadcast [1, 2].

- `U.S. Commercial Launch (T0)`: 1920  
  Defense: 1920 is the clearest U.S. launch year because the FCC identifies KDKA's November 2, 1920 election-night transmission as the first commercial radio broadcast in the United States [3].

- `Fundamental Scaling Metric`: Cost per listener-hour delivered.

- `Recommended U.S. Adoption Metric`: Share of U.S. households with a radio receiver.

- `Denominator`: Households

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Radio remains a durable mass-audience and emergency-information substrate even after television, internet, and mobile media displaced its peak centrality.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] U.S. National Park Service. "Reginald Fessenden." https://www.nps.gov/people/reginaldfessenden.htm
- [2] Encyclopaedia Britannica. "Reginald Aubrey Fessenden." https://www.britannica.com/biography/Reginald-Aubrey-Fessenden
- [3] Federal Communications Commission. Statement of Chairman Ajit Pai, MB Docket No. 17-106. https://docs.fcc.gov/public/attachments/DOC-344947A2.pdf
- [4] U.S. Census Bureau. *Historical Statistics of the United States, Colonial Times to 1957*, chapter R. https://www2.census.gov/library/publications/1960/compendia/hist_stats_colonial-1957/hist_stats_colonial-1957-chR.pdf

## Open Questions

- Whether a later split between `broadcast_radio` and two-way mobile radio would improve analytical separability as the dataset grows.
- Whether household receiver ownership is sufficient on its own or should eventually be paired with station reach or audience-hour measures.

## QA Notes

- PASS
- Dependency check: The listed dependencies predate 1906 broadcast radio and avoid relying on later electronics stacks.
- T0 check: 1920 is acceptable because it marks a recognized commercial U.S. broadcasting launch rather than an experimental transmission.
- Metric check: Household receiver ownership is an appropriate denominator for a mass broadcast substrate.
