```yaml
id: nervous_system/internet
domain: Nervous_System
subdomain: Networks
technology: Internet
substrate_type: Soft
status: qa_passed
phase: 1
primary_dependencies: nervous_system/telephone;nervous_system/semiconductors
invention_year: 1969
invention_year_defense: ARPANET's first node-to-node operation in 1969 is the clearest practical invention boundary because it marks a working packet-switched network rather than a theoretical protocol proposal.
us_commercial_launch_year: 1991
us_commercial_launch_defense: 1991 is the stronger canonical U.S. commercial launch year because NSF explicitly identifies that year as the point when the Internet was opened to public and commercial use, even though precursor commercial ISPs appeared slightly earlier.
fundamental_scaling_metric: Cost per Mbps-month of bandwidth delivered.
recommended_us_adoption_metric: Share of U.S. households or adults with Internet access.
denominator: Population
t10_years: 6
t25_years: 7
t50_years: 10
t75_years: 24
peak_adoption_or_current_status: Near-ubiquitous dependence across communication, commerce, logistics, software, and state capacity.
confidence: medium
notes: 1989 commercial ISP availability is treated as a precursor milestone; 1991 is canonical T0. Tier 1 diffusion series uses NTIA/Census person-level Internet use from any location; thresholds are 22.2 percent in 1997, 32.7 percent in 1998, 53.9 percent in 2001, and 75 percent in 2015.
```

# Internet

## Identity

- `Domain`: Nervous_System
- `Subdomain`: Networks
- `Technology`: Internet
- `Substrate Type`: Soft

## Scope And Inclusion Note

- This profile treats the internet as the interoperable packet-switched network of networks, distinct from physical telecom lines and distinct from later cloud services or web applications.
- It is in scope because it became an economy-wide coordination layer, is measurable through user access and traffic, and clearly sits deep in the modern dependency stack [1, 2].
- Which inclusion tests from `STANDARDS_MEMO.md` it satisfies: cross-sector impact, dependency depth, durability, substrate character, analytical separability.

## Primary Dependencies

- Telegraph and telephone lineage
- Semiconductors and routers
- Long-haul telecom infrastructure and standardized protocols [1, 2]

## Phase 1 Claims

- `Invention Year`: 1969  
  Defense: ARPANET's first node-to-node operation in 1969 is the clearest practical invention boundary because it marks a working packet-switched network rather than a theoretical protocol proposal [1, 2].

- `U.S. Commercial Launch (T0)`: 1991  
  Defense: 1991 is the stronger canonical U.S. commercial launch year because NSF explicitly identifies that year as the point when the Internet was opened to public and commercial use, even though precursor commercial ISPs appeared slightly earlier [2, 3].

- `Fundamental Scaling Metric`: Cost per Mbps-month of bandwidth delivered.

- `Recommended U.S. Adoption Metric`: Share of U.S. households or adults with Internet access.

- `Denominator`: Population

## Diffusion Milestones

- Canonical Tier 1 series: NTIA/Census share of Americans ages 3 and older using the Internet from any location [5, 6, 7].
- `T10`: 6 years. The standardized NTIA/Census series is already at 22.2 percent in October 1997, so the first observed threshold crossing after the 1991 launch is 1997 [5].
- `T25`: 7 years. NTIA reports 32.7 percent Internet use in December 1998 [5].
- `T50`: 10 years. NTIA reports 53.9 percent Internet use in September 2001 [5].
- `T75`: 24 years. NTIA reports 75 percent of Americans ages 3 and older used the Internet in 2015 [6].
- `Peak Adoption / Current Status`: Near-ubiquitous dependence across communication, commerce, logistics, software, and state capacity.

Leave these blank when evidence is not yet strong enough.

## References

Use numbered citations inline in the sections above, for example `[1]` or `[2, 3]`.

- [1] Defense Advanced Research Projects Agency. "ARPANET." https://www.darpa.mil/about-us/timeline/arpanet
- [2] Internet Society. "A Brief History of the Internet." https://www.internetsociety.org/internet/history-internet/brief-history-internet/
- [3] U.S. National Science Foundation. "NSB 50th Anniversary: The 1990s." https://www.nsf.gov/nsb/documents/2000/nsb00215/nsb50/1990/index.html
- [4] U.S. National Science Foundation. *The Internet*. https://www.nsf.gov/about/history/nsf0050/pdf/internet.pdf
- [5] National Telecommunications and Information Administration. "Chapter 2: Computer and Internet Use" in *A Nation Online: How Americans Are Expanding Their Use of the Internet*, 2002. https://www.ntia.gov/sites/default/files/data/dn/html/Chapter2.htm
- [6] National Telecommunications and Information Administration. "First Look: Internet Use in 2015," 2016. https://www.ntia.gov/blog/2016/first-look-internet-use-2015
- [7] National Telecommunications and Information Administration. "New Data Show Substantial Gains and Evolution in Internet Use," 2018. https://www.ntia.gov/blog/2018/new-data-show-substantial-gains-and-evolution-internet-use

## Open Questions

- Whether the project should preserve 1989 as an early commercial-ISP milestone while keeping 1991 as the canonical public/commercial launch year.
- Whether household access or firm connectivity is the better long-run adoption metric for the dataset.

## QA Notes

- Dependency check: Internet follows earlier telecom and semiconductor substrates.
- T0 check: 1991 is tied to official opening for public and commercial use rather than research-network access only.
- Metric check: Direct access is reasonable here because the Internet has meaningful end-user penetration as well as industrial dependence.
