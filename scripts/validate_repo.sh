#!/usr/bin/env bash

set -euo pipefail

required_files=(
  "README.md"
  "AGENTS.md"
  "PRD.md"
  "ARCHITECTURE.md"
  "ROADMAP.md"
  "BACKLOG.md"
  "RUNBOOK.md"
  "SCHEMA.md"
  "STANDARDS_MEMO.md"
  ".gitignore"
  "research/prompts/qa_adjudicator.md"
  "research/prompts/metabolism_agent.md"
  "research/prompts/nervous_system_agent.md"
  "research/prompts/vascular_agent.md"
  "research/prompts/immune_system_agent.md"
  "research/profiles/PROFILE_TEMPLATE.md"
  "research/evidence/README.md"
  "research/notes/source-agent-prompts.md"
  "data/templates/substrates_master.template.csv"
  "scripts/compile_profiles.py"
)

required_dirs=(
  "research"
  "research/prompts"
  "research/profiles"
  "research/evidence"
  "research/notes"
  "data"
  "data/templates"
  "data/raw"
  "data/processed"
  "scripts"
)

for path in "${required_files[@]}"; do
  if [[ ! -f "$path" ]]; then
    echo "Missing required file: $path" >&2
    exit 1
  fi
done

for path in "${required_dirs[@]}"; do
  if [[ ! -d "$path" ]]; then
    echo "Missing required directory: $path" >&2
    exit 1
  fi
done

expected_header="id,domain,subdomain,technology,substrate_type,primary_dependencies,invention_year,invention_year_defense,us_commercial_launch_year,us_commercial_launch_defense,delta_years,fundamental_scaling_metric,recommended_us_adoption_metric,denominator,t10_years,t25_years,t50_years,t75_years,peak_adoption_or_current_status,source_count,confidence,notes"
actual_header="$(head -n 1 data/templates/substrates_master.template.csv)"

if [[ "$actual_header" != "$expected_header" ]]; then
  echo "Dataset template header does not match the canonical schema." >&2
  exit 1
fi

echo "Repository scaffold validation passed."
