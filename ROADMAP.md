# Roadmap

## Phase 0: Clarify And Stabilize The Concept (COMPLETED)

Exit criteria:
- [x] docs are internally consistent
- [x] the artifact flow `profile -> QA -> dataset` is stable
- [x] seed technologies for the MVP are explicitly named
- [x] the four-domain Phase 1 boundary is reflected consistently

## Phase 1: Minimum Viable Implementation (NEARLY COMPLETE)

Purpose:
Produce the first credible dataset slice.

Work:
- [x] write validated profiles for the initial seed technologies
- [x] run QA adjudication on those profiles
- [x] compile the first `data/processed/substrates_master.csv`
- [ ] complete backfilling of all diffusion milestones (T10-T75)

Exit criteria:
- at least 24 validated technologies exist
- the master dataset is regenerated automatically from profiles
- the highest-confidence fields are populated consistently

## Phase 2: Diffusion And Comparative Analysis (ACTIVE)

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
