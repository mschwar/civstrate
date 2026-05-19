#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / "research" / "profiles"
TEMPLATE_CSV = ROOT / "data" / "templates" / "substrates_master.template.csv"
COMPILER = ROOT / "scripts" / "compile_profiles.py"

EXPECTED_TEMPLATE_HEADER = (
    "id,domain,subdomain,technology,substrate_type,primary_dependencies,"
    "invention_year,invention_year_defense,us_commercial_launch_year,"
    "us_commercial_launch_defense,delta_years,fundamental_scaling_metric,"
    "recommended_us_adoption_metric,denominator,t10_years,t25_years,t50_years,"
    "t75_years,peak_adoption_or_current_status,source_count,confidence,notes"
)

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "PRD.md",
    "ARCHITECTURE.md",
    "ROADMAP.md",
    "BACKLOG.md",
    "RUNBOOK.md",
    "CURRENT_STATE.md",
    "SCHEMA.md",
    "STANDARDS_MEMO.md",
    ".gitignore",
    "research/prompts/qa_adjudicator.md",
    "research/prompts/metabolism_agent.md",
    "research/prompts/nervous_system_agent.md",
    "research/prompts/vascular_agent.md",
    "research/prompts/immune_system_agent.md",
    "research/profiles/PROFILE_TEMPLATE.md",
    "research/evidence/README.md",
    "research/notes/README.md",
    "research/notes/source-agent-prompts.md",
    "data/templates/substrates_master.template.csv",
    "scripts/compile_profiles.py",
    "scripts/validate_repo.py",
    "docs/agentic-overhaul/2026-05-audit.md",
]

REQUIRED_DIRS = [
    "research",
    "research/prompts",
    "research/profiles",
    "research/evidence",
    "research/notes",
    "data",
    "data/templates",
    "data/raw",
    "data/processed",
    "scripts",
    "docs",
    "docs/agentic-overhaul",
]

INLINE_CITATION_RE = re.compile(r"\[\d+(?:,\s*\d+)*\]")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class ValidationError(Exception):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the repository scaffold and profile corpus.")
    return parser.parse_args()


def fail(message: str) -> None:
    raise ValidationError(message)


def check_required_paths() -> None:
    missing_files = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    missing_dirs = [path for path in REQUIRED_DIRS if not (ROOT / path).is_dir()]

    messages: list[str] = []
    if missing_files:
        messages.append("Missing required file(s): " + ", ".join(missing_files))
    if missing_dirs:
        messages.append("Missing required directory(ies): " + ", ".join(missing_dirs))

    if messages:
        fail("\n".join(messages))


def check_template_header() -> None:
    actual_header = TEMPLATE_CSV.read_text(encoding="utf-8").splitlines()[0]
    if actual_header != EXPECTED_TEMPLATE_HEADER:
        fail("Dataset template header does not match the canonical schema.")


def parse_top_yaml_block(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    start = None
    for index, line in enumerate(lines):
        if line.strip() == "```yaml":
            start = index + 1
            break

    if start is None:
        fail(f"{path.name}: missing top fenced yaml block")

    end = None
    for index in range(start, len(lines)):
        if lines[index].strip() == "```":
            end = index
            break

    if end is None:
        fail(f"{path.name}: unterminated yaml block")

    metadata: dict[str, str] = {}
    for raw_line in lines[start:end]:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in raw_line:
            fail(f"{path.name}: invalid metadata line: {raw_line}")
        key, value = raw_line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("'\"")

    return metadata, text


def strip_code_fences(text: str) -> str:
    visible_lines: list[str] = []
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            visible_lines.append(line)
    return "\n".join(visible_lines)


def check_profile_citations() -> None:
    errors: list[str] = []

    for path in sorted(PROFILE_DIR.glob("*.md")):
        if path.name == "PROFILE_TEMPLATE.md":
            continue

        metadata, text = parse_top_yaml_block(path)
        if metadata.get("status") != "qa_passed":
            continue

        visible_text = strip_code_fences(text)
        body, separator, references = visible_text.partition("## References")
        if not separator:
            errors.append(f"{path.name}: missing ## References section")
            continue
        if not INLINE_CITATION_RE.search(body):
            errors.append(f"{path.name}: missing inline numbered citation in profile body")
        if not any(line.strip().startswith("- [") for line in references.splitlines()):
            errors.append(f"{path.name}: ## References section has no numbered references")

    if errors:
        fail("\n".join(errors))


def check_markdown_links() -> None:
    errors: list[str] = []

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue

        visible_text = strip_code_fences(path.read_text(encoding="utf-8"))
        for match in MARKDOWN_LINK_RE.finditer(visible_text):
            raw_target = match.group(1).strip()
            if not raw_target:
                continue
            if raw_target.startswith("<") and ">" in raw_target:
                raw_target = raw_target[1 : raw_target.index(">")]
            else:
                raw_target = raw_target.split()[0]

            target = raw_target.split("#", 1)[0]
            if not target:
                continue
            if target.startswith(("http://", "https://", "mailto:", "app://", "plugin://", "file://", "#")):
                continue

            candidate = Path(target)
            if not candidate.is_absolute():
                candidate = (path.parent / candidate).resolve()

            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link target '{raw_target}'")

    if errors:
        fail("\n".join(errors))


def run_compiler_check() -> None:
    result = subprocess.run(
        [sys.executable, str(COMPILER), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        stdout = result.stdout.strip()
        detail = stderr or stdout or "compiler check failed"
        fail(detail)


def main() -> int:
    parse_args()
    check_required_paths()
    check_template_header()
    check_profile_citations()
    check_markdown_links()
    run_compiler_check()
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
