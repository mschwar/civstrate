# Canonical Schema

This project currently has three canonical artifact types:

1. per-technology profile files
2. a master compiled dataset
3. agent prompt files that drive collection and QA

The schema below is intentionally lightweight. It is meant to stabilize the early workflow, not to imply that the full data model is final.

## Artifact 1: Technology Profile

Path pattern:

- `research/profiles/<slug>.md`

Purpose:

- capture the source-backed research record for one technology
- keep adjudication-readable context near each claim
- serve as the source material for later compiled dataset rows

Recommended sections:

- identity
- scope and inclusion note
- primary dependencies
- invention year claim and defense
- U.S. commercial launch claim and defense
- scaling metric
- recommended adoption metric and denominator
- diffusion milestone notes
- references
- QA comments

The canonical starter format lives in `research/profiles/PROFILE_TEMPLATE.md`.

### Citation Convention For Profiles

Profiles should follow the citation pattern used in the newest Google DeepMind white papers:

- use numbered citations inline in prose, for example `[1]` or `[2, 3]`
- end each profile with a `## References` section
- number references in citation order
- include enough detail to recover the source without extra chat context: author, title, venue or publisher, year, and stable URL when available

This citation convention is modeled on recent official Google DeepMind white papers. The repo-specific choice to store those references directly in each profile is an implementation decision derived from that publication style.

## Artifact 2: Master Dataset

Canonical future output path:

- `data/processed/substrates_master.csv`

Starter template path:

- `data/templates/substrates_master.template.csv`

One row represents one technology.

### Column Definitions

- `id`
  Stable slug for the row, for example `nervous-system/semiconductors`.

- `domain`
  One of `Metabolism`, `Vascular`, `Nervous_System`, `Immune_System`.

- `subdomain`
  Specific grouping such as `Power`, `Materials`, `Wireless`, or `Compute`.

- `technology`
  Human-readable technology name.

- `substrate_type`
  One of `Hard` or `Soft`.

- `primary_dependencies`
  Semicolon-delimited list of prerequisite technology slugs that must resolve to other canonical profile IDs included in the compiled dataset. If a prerequisite is real but does not yet have its own canonical profile row, keep it in the profile prose or notes instead of putting a placeholder slug here.

- `invention_year`
  First workable or practical invention year after 1800.

- `invention_year_defense`
  One-sentence justification for why the chosen year is the defensible invention year.

- `us_commercial_launch_year`
  First meaningful U.S. commercial or public availability year.

- `us_commercial_launch_defense`
  One-sentence justification for the chosen U.S. launch year.

- `delta_years`
  Derived field: `us_commercial_launch_year - invention_year`.

- `fundamental_scaling_metric`
  The cost/performance metric that best captures long-run improvement.

- `recommended_us_adoption_metric`
  The preferred metric for measuring spread or exposure in the U.S.

- `denominator`
  One of `Households`, `Population`, `Firms`, `GDP`, `Volume`, or another explicitly documented choice.

- `t10_years`
  Years from U.S. commercial launch to 10 percent adoption or equivalent exposure.

- `t25_years`
  Years from U.S. commercial launch to 25 percent adoption or equivalent exposure.

- `t50_years`
  Years from U.S. commercial launch to 50 percent adoption or equivalent exposure.

- `t75_years`
  Years from U.S. commercial launch to 75 percent adoption or equivalent exposure.

- `peak_adoption_or_current_status`
  Best current summary of peak reach, saturation, or present role.

- `source_count`
  Integer count of sources cited in the profile.

- `confidence`
  Qualitative confidence such as `high`, `medium`, or `low`.

- `notes`
  Reserved for unresolved caveats that should survive compilation.

### Phase Guidance

- Phase 1 requires the identity, classification, dependency, timeline, and metric fields.
- Diffusion milestone fields may be blank during Phase 1 if they are not yet defensible.
- `delta_years` should be computed, not manually invented.

## Artifact 3: Agent Prompt Files

Path pattern:

- `research/prompts/*.md`

Purpose:

- preserve the research roles and instructions that future agents should execute against
- avoid hiding the project method in chat history only

Current prompt set:

- `qa_adjudicator.md`
- `metabolism_agent.md`
- `nervous_system_agent.md`
- `vascular_agent.md`
- `immune_system_agent.md`

## Naming Rules

- Use lowercase file slugs with underscores for filenames.
- Use stable domain names exactly as written above.
- Do not rename canonical columns casually once the first compiled dataset exists.
- If a new artifact type is introduced, document it here before relying on it operationally.
- Treat `primary_dependencies` as a closed graph field, not as a catch-all for abstract prerequisites.
