#!/usr/bin/env python3
"""Validate research registries and weekly automation metadata."""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECISIONS = {
    "NO_OP",
    "REFERENCE_ONLY",
    "WATCH",
    "ADD",
    "UPDATE",
    "DEPRECATE",
    "RESTRUCTURE",
}
WEEK_PATTERN = re.compile(r"[0-9]{4}-W[0-9]{2}")


def validate_jsonl(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing {path.relative_to(ROOT)}"]

    for line_number, raw in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: {exc}")
            continue
        if not isinstance(value, dict):
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: "
                "each line must be a JSON object"
            )
    return errors


def validate_weekly_run(path: Path) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(ROOT)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: {exc}"]

    if not isinstance(value, dict):
        return [f"{relative}: root must be a JSON object"]

    week = value.get("week")
    expected_week = path.stem
    if week != expected_week or not WEEK_PATTERN.fullmatch(expected_week):
        errors.append(f"{relative}: week must match filename {expected_week!r}")

    completed_at = value.get("completed_at")
    try:
        if not isinstance(completed_at, str):
            raise ValueError
        dt.date.fromisoformat(completed_at)
    except ValueError:
        errors.append(f"{relative}: completed_at must be an ISO date")

    expected_report = f"reports/weekly/{expected_week}.md"
    report = value.get("report")
    if report != expected_report:
        errors.append(f"{relative}: report must be {expected_report!r}")
    elif not (ROOT / report).is_file():
        errors.append(f"{relative}: referenced report does not exist")

    candidates = value.get("candidate_issues")
    if not isinstance(candidates, list):
        errors.append(f"{relative}: candidate_issues must be an array")
        return errors

    issue_numbers: set[int] = set()
    for index, candidate in enumerate(candidates):
        prefix = f"{relative}: candidate_issues[{index}]"
        if not isinstance(candidate, dict):
            errors.append(f"{prefix} must be an object")
            continue
        number = candidate.get("number")
        decision = candidate.get("decision")
        if (
            not isinstance(number, int)
            or isinstance(number, bool)
            or number <= 0
        ):
            errors.append(f"{prefix}.number must be a positive integer")
        elif number in issue_numbers:
            errors.append(f"{prefix}.number is duplicated")
        else:
            issue_numbers.add(number)
        if decision not in DECISIONS:
            errors.append(f"{prefix}.decision is invalid")

    return errors


def main() -> int:
    errors: list[str] = []
    for relative in ("references/seen.jsonl", "references/sources.jsonl"):
        errors.extend(validate_jsonl(ROOT / relative))
    for path in sorted((ROOT / "runs/weekly").glob("*.json")):
        errors.extend(validate_weekly_run(path))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Research data validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
