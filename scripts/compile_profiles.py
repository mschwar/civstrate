#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import difflib
import io
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / "research" / "profiles"
TEMPLATE_CSV = ROOT / "data" / "templates" / "substrates_master.template.csv"
OUTPUT_CSV = ROOT / "data" / "processed" / "substrates_master.csv"

DOMAIN_VALUES = {"Metabolism", "Vascular", "Nervous_System", "Immune_System"}
SUBSTRATE_TYPE_VALUES = {"Hard", "Soft"}
DENOMINATOR_VALUES = {"Households", "Population", "Firms", "GDP", "Volume"}
STATUS_VALUES = {"draft", "qa_passed"}

METADATA_FIELDS = [
    "id",
    "domain",
    "subdomain",
    "technology",
    "substrate_type",
    "status",
    "phase",
    "primary_dependencies",
    "invention_year",
    "invention_year_defense",
    "us_commercial_launch_year",
    "us_commercial_launch_defense",
    "fundamental_scaling_metric",
    "recommended_us_adoption_metric",
    "denominator",
    "t10_years",
    "t25_years",
    "t50_years",
    "t75_years",
    "peak_adoption_or_current_status",
    "confidence",
    "notes",
]

REQUIRED_NONEMPTY_FIELDS = [
    "id",
    "domain",
    "subdomain",
    "technology",
    "substrate_type",
    "status",
    "phase",
    "invention_year",
    "invention_year_defense",
    "us_commercial_launch_year",
    "us_commercial_launch_defense",
    "fundamental_scaling_metric",
    "recommended_us_adoption_metric",
    "denominator",
    "peak_adoption_or_current_status",
    "confidence",
]

INTEGER_FIELDS = [
    "phase",
    "invention_year",
    "us_commercial_launch_year",
    "t10_years",
    "t25_years",
    "t50_years",
    "t75_years",
]

SLUG_PATTERN = re.compile(r"^[a-z_]+/[a-z0-9_]+$")


class CompileError(Exception):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compile QA-passed profile metadata into the master substrate CSV."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the generated CSV would differ from data/processed/substrates_master.csv.",
    )
    return parser.parse_args()


def parse_metadata_block(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    start = None
    for index, line in enumerate(lines):
        if line.strip() == "```yaml":
            start = index + 1
            break

    if start is None:
        raise CompileError(f"{path.name}: missing top fenced yaml block")

    end = None
    for index in range(start, len(lines)):
        if lines[index].strip() == "```":
            end = index
            break

    if end is None:
        raise CompileError(f"{path.name}: unterminated yaml block")

    metadata: dict[str, str] = {}
    for raw_line in lines[start:end]:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in raw_line:
            raise CompileError(f"{path.name}: invalid metadata line: {raw_line}")
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = strip_wrapping_quotes(value.strip())
        if key in metadata:
            raise CompileError(f"{path.name}: duplicate metadata key '{key}'")
        metadata[key] = value

    return metadata, text


def strip_wrapping_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def count_references(path: Path, text: str) -> int:
    lines = text.splitlines()
    in_references = False
    count = 0

    for line in lines:
        stripped = line.strip()
        if stripped == "## References":
            in_references = True
            continue
        if in_references and stripped.startswith("## "):
            break
        if in_references and stripped.startswith("- [") and "]" in stripped:
            count += 1

    if count == 0:
        raise CompileError(f"{path.name}: ## References section has no numbered references")

    return count


def normalize_dependencies(value: str) -> str:
    if not value.strip():
        return ""
    parts = [part.strip() for part in value.split(";") if part.strip()]
    return ";".join(parts)


def validate_and_build_row(path: Path, metadata: dict[str, str], source_count: int) -> dict[str, str] | None:
    missing = [field for field in METADATA_FIELDS if field not in metadata]
    if missing:
        raise CompileError(f"{path.name}: missing metadata fields: {', '.join(missing)}")

    status = metadata["status"]
    if status not in STATUS_VALUES:
        raise CompileError(f"{path.name}: invalid status '{status}'")
    if status != "qa_passed":
        return None

    blank_required = [field for field in REQUIRED_NONEMPTY_FIELDS if not metadata[field].strip()]
    if blank_required:
        raise CompileError(f"{path.name}: blank required metadata fields: {', '.join(blank_required)}")

    if metadata["domain"] not in DOMAIN_VALUES:
        raise CompileError(f"{path.name}: invalid domain '{metadata['domain']}'")
    if metadata["substrate_type"] not in SUBSTRATE_TYPE_VALUES:
        raise CompileError(f"{path.name}: invalid substrate_type '{metadata['substrate_type']}'")
    if metadata["denominator"] not in DENOMINATOR_VALUES:
        raise CompileError(f"{path.name}: invalid denominator '{metadata['denominator']}'")

    normalized: dict[str, str] = {}
    for field in INTEGER_FIELDS:
        value = metadata[field].strip()
        if not value:
            normalized[field] = ""
            continue
        try:
            normalized[field] = str(int(value))
        except ValueError as exc:
            raise CompileError(f"{path.name}: field '{field}' must be an integer, got '{value}'") from exc

    invention_year = int(normalized["invention_year"])
    launch_year = int(normalized["us_commercial_launch_year"])
    delta_years = launch_year - invention_year
    if delta_years < 0:
        raise CompileError(
            f"{path.name}: us_commercial_launch_year ({launch_year}) precedes invention_year ({invention_year})"
        )

    return {
        "id": metadata["id"].strip(),
        "domain": metadata["domain"].strip(),
        "subdomain": metadata["subdomain"].strip(),
        "technology": metadata["technology"].strip(),
        "substrate_type": metadata["substrate_type"].strip(),
        "primary_dependencies": normalize_dependencies(metadata["primary_dependencies"]),
        "invention_year": normalized["invention_year"],
        "invention_year_defense": metadata["invention_year_defense"].strip(),
        "us_commercial_launch_year": normalized["us_commercial_launch_year"],
        "us_commercial_launch_defense": metadata["us_commercial_launch_defense"].strip(),
        "delta_years": str(delta_years),
        "fundamental_scaling_metric": metadata["fundamental_scaling_metric"].strip(),
        "recommended_us_adoption_metric": metadata["recommended_us_adoption_metric"].strip(),
        "denominator": metadata["denominator"].strip(),
        "t10_years": normalized["t10_years"],
        "t25_years": normalized["t25_years"],
        "t50_years": normalized["t50_years"],
        "t75_years": normalized["t75_years"],
        "peak_adoption_or_current_status": metadata["peak_adoption_or_current_status"].strip(),
        "source_count": str(source_count),
        "confidence": metadata["confidence"].strip(),
        "notes": metadata["notes"].strip(),
    }


def validate_dependency_graph(rows: list[dict[str, str]]) -> None:
    ids = {row["id"] for row in rows}
    rows_by_id = {row["id"]: row for row in rows}
    errors: list[str] = []

    for row in rows:
        deps = [dep for dep in row["primary_dependencies"].split(";") if dep]
        for dep in deps:
            if not SLUG_PATTERN.match(dep):
                errors.append(f"{row['id']}: invalid dependency slug '{dep}'")
                continue
            if dep == row["id"]:
                errors.append(f"{row['id']}: self-dependency is not allowed")
                continue
            if dep not in ids:
                errors.append(
                    f"{row['id']}: dependency '{dep}' does not resolve to a compiled profile id"
                )
                continue
            dep_invention_year = int(rows_by_id[dep]["invention_year"])
            row_invention_year = int(row["invention_year"])
            if dep_invention_year > row_invention_year:
                errors.append(
                    f"{row['id']}: dependency '{dep}' was invented in {dep_invention_year}, "
                    f"which is later than this row's invention_year {row_invention_year}"
                )

    if errors:
        raise CompileError("\n".join(errors))


def load_header() -> tuple[str, list[str]]:
    header_line = TEMPLATE_CSV.read_text(encoding="utf-8").splitlines()[0]
    columns = next(csv.reader([header_line]))
    return header_line, columns


def compile_rows() -> list[dict[str, str]]:
    errors: list[str] = []
    rows: list[tuple[Path, dict[str, str]]] = []
    seen_ids: dict[str, Path] = {}

    for path in sorted(PROFILE_DIR.glob("*.md")):
        if path.name == "PROFILE_TEMPLATE.md":
            continue
        try:
            metadata, text = parse_metadata_block(path)
            source_count = count_references(path, text)
            row = validate_and_build_row(path, metadata, source_count)
            if row is None:
                continue
            if row["id"] in seen_ids:
                first_path = seen_ids[row["id"]]
                raise CompileError(
                    f"{path.name}: duplicate id '{row['id']}' already used by {first_path.name}"
                )
            seen_ids[row["id"]] = path
            rows.append((path, row))
        except CompileError as exc:
            errors.append(str(exc))

    if errors:
        raise CompileError("\n".join(errors))

    compiled_rows = [row for _, row in sorted(rows, key=lambda item: item[1]["id"])]
    validate_dependency_graph(compiled_rows)
    return compiled_rows


def render_csv(rows: list[dict[str, str]], header_line: str, header_columns: list[str]) -> str:
    buffer = io.StringIO()
    buffer.write(header_line)
    buffer.write("\n")
    writer = csv.writer(buffer, quoting=csv.QUOTE_ALL, lineterminator="\n")
    for row in rows:
        writer.writerow([row.get(column, "") for column in header_columns])
    return buffer.getvalue()


def check_output(content: str) -> int:
    current = OUTPUT_CSV.read_text(encoding="utf-8") if OUTPUT_CSV.exists() else ""
    if current == content:
        return 0

    diff = difflib.unified_diff(
        current.splitlines(),
        content.splitlines(),
        fromfile=str(OUTPUT_CSV),
        tofile="generated",
        lineterm="",
    )
    sys.stderr.write("\n".join(diff) + "\n")
    return 1


def main() -> int:
    args = parse_args()
    header_line, header_columns = load_header()
    rows = compile_rows()
    content = render_csv(rows, header_line, header_columns)

    if args.check:
        return check_output(content)

    OUTPUT_CSV.write_text(content, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
