```yaml
id: nervous_system/fiber_optics
domain: Nervous_System
subdomain: Networks
technology: Fiber Optics
substrate_type: Hard
status: qa_passed
phase: 1
primary_dependencies: nervous_system/telephone;nervous_system/semiconductors
invention_year: 1970
invention_year_defense: 1970 is the strongest practical invention boundary because Corning produced the first low-loss optical fiber capable of carrying telecommunications signals over useful distances.
us_commercial_launch_year: 1977
us_commercial_launch_defense: 1977 is the clearest U.S. commercial launch year because Bell Labs records that commercial traffic began on the Chicago lightwave system on April 1, 1977.
fundamental_scaling_metric: Cost per transmitted bit-kilometer or per Mbps-mile.
recommended_us_adoption_metric: Fiber route-miles in operation in the U.S., with share of U.S. telecom backbone traffic carried on fiber as a supporting metric.
denominator: Volume
t10_years:
t25_years:
t50_years:
t75_years:
peak_adoption_or_current_status: Core physical bandwidth substrate for telecom backbones, broadband access, data centers, and long-haul internet transport.
confidence: medium
notes: Uses 1977 because Bell System commercial traffic began in Chicago that year; the 1976 Atlanta experiment remains a precursor rather than canonical T0. Tier 1 diffusion attempt deferred because route-mile and traffic-share series do not yet form one continuous national threshold series that captures both buildout and bandwidth scaling.
```

# Fiber Optics

## Identity

- `Domain`: Nervous_System
- `Subdomain`: Networks
- `Technology`: Fiber Optics
- `Substrate Type`: Hard

## Scope And Inclusion Note

- This profile covers optical fiber as the physical transmission substrate for modern high-bandwidth communications networks, not lasers in general and not every optical component.
- It is in scope because it became the core bandwidth layer underneath long-haul telecom, broadband, undersea cables, data centers, and the modern Internet [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Telephone and telecom switching systems that created demand for higher-capacity transmission [2, 3].
- Precision glass and manufacturing methods capable of low-loss fiber [1].
- Semiconductor lasers, detectors, and network electronics to turn glass fiber into a working communications system [3].

## Phase 1 Claims

- `Invention Year`: 1970  
  Defense: 1970 is the cleanest practical boundary because Corning records that year as the invention of the first low-loss optical fiber suitable for telecommunications [1, 2].

- `U.S. Commercial Launch (T0)`: 1977  
  Defense: 1977 is the strongest current U.S. launch year because Corning identifies AT&T's Chicago installation as the first optical telephone communication system in operating service [2].

- `Fundamental Scaling Metric`: Cost per transmitted bit-kilometer or per Mbps-mile.

- `Recommended U.S. Adoption Metric`: Fiber route-miles or share of U.S. telecom backbone traffic carried on fiber.

- `Denominator`: Volume

## Diffusion Milestones

- `T10`:
- `T25`:
- `T50`:
- `T75`:
- `Peak Adoption / Current Status`: Core physical bandwidth substrate for telecom backbones, broadband access, data centers, and long-haul internet transport.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Corning. "Our History of Optical Fiber Innovation." https://www.corning.com/optical-communications/emea/en/home/products/fiber/optical-fiber-innovation.html
- [2] Corning. "Fiber Gets Real with Single-Mode Fiber Development." https://www.corning.com/in/en/markets/Optical-Communications-Market/streamlined-connectivity/timeline-1978.html
- [3] Nokia Bell Labs. "Atlanta Fiber System Experiment: Overview." https://www.nokia.com/bell-labs/publications-and-media/publications/atlanta-fiber-system-experiment-overview/

## Open Questions

- Whether the canonical U.S. T0 should be 1977 Chicago service, 1978 broader first commercial uses, or another Bell System deployment with cleaner evidence.
- Whether route-miles or carried traffic is the better long-run adoption measure for a backbone substrate.

## QA Notes

- PASS
- Dependency check: Fiber optics correctly follows telecom and materials prerequisites.
- T0 check: 1977 is supported by Bell Labs as the first commercial traffic on the Chicago system and is acceptable as canonical T0.
- Metric check: Route-miles are simple but may understate upgrades in bandwidth per strand.
