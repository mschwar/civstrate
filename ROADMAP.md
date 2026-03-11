# Roadmap

## Phase 0: Clarify And Stabilize The Concept

Purpose:
Turn the current thesis, schema sketch, and prompts into a stable research contract.

Work:

- apply and test the documented Phase 1 inclusion rules against edge cases
- finalize the per-technology profile format
- decide the canonical field names for the master dataset
- operationalize the citation and evidence capture approach
- seed all four domain prompts and starter technology lists

Exit criteria:

- docs are internally consistent
- the artifact flow `profile -> QA -> dataset` is stable
- seed technologies for the MVP are explicitly named
- no major naming conflicts remain across the docs
- the four-domain Phase 1 boundary is reflected consistently everywhere

## Phase 1: Minimum Viable Implementation

Purpose:
Produce the first credible dataset slice.

Work:

- write validated profiles for the initial seed technologies
- run QA adjudication on those profiles
- compile the first `data/processed/substrates_master.csv`
- backfill justifications and source links for every populated row
- document any unresolved disputes without hiding them

Exit criteria:

- at least 8 validated technologies exist
- the master dataset can be regenerated from the profile set
- the highest-confidence fields are populated consistently
- unresolved disputes are logged as open issues, not buried in prose

## Later Phases

### Phase 2: Diffusion And Comparative Analysis

Work:

- add T10, T25, T50, and T75 where defensible
- compare hard vs soft substrate adoption latency
- map dependency chains and stacked-vulnerability patterns
- produce first charts, memos, or notebooks

Exit criteria:

- diffusion methodology is documented
- at least one comparative analysis artifact exists
- dependency relationships are expressed consistently enough for graphing

### Phase 3: Publication Surface And Tooling

Work:

- decide whether the repo needs a notebook workflow, CLI, or app surface
- add only the tooling required by the proven research workflow
- package outputs for collaboration or publication

Exit criteria:

- the chosen implementation surface is justified by actual use
- the repo can onboard a new contributor without verbal handoff
- tooling supports the research system instead of replacing it
