#!/usr/bin/env python3
"""Check the sources, then write public/v1/ (what gets hosted and what the app reads).

    python3 scripts/build.py

Output (all JSON is UTF-8, keys sorted, no extra spaces, so the same input
always gives byte-identical files and the same hashes):

    public/v1/manifest.json          versions + sha256 of everything below
    public/v1/catalog.json           streams > programmes > schemes > terms > subjects
    public/v1/exams/<body>.json      date sheets
    public/v1/packs/<subjectId>.json one subject: notes, questions, MCQs, mock tests, practicals
    public/v1/media/<subjectId>/...  images
"""

import sys

from content_lib import OUTPUT, Report, build_output, coverage, rel, validate_all


def main() -> int:
    report = Report()
    validated = validate_all(report)
    for warning in report.warnings:
        print(f"warning: {warning}")
    if report.errors or validated is None:
        for error in report.errors:
            print(f"ERROR: {error}")
        print(f"\n{len(report.errors)} error(s). Nothing was built.")
        return 1

    manifest = build_output(validated)
    counts = coverage(validated)["counts"]
    print(f"Built {rel(OUTPUT)}:")
    print(f"  catalog      {manifest['catalog']['version']}  ({manifest['catalog']['bytes']} bytes)")
    for exam in manifest["exams"]:
        print(f"  exams/{exam['bodyId']:<7} {exam['version']}  ({exam['bytes']} bytes)")
    for pack in manifest["packs"]:
        flag = "reviewed" if pack["reviewed"] else "NOT reviewed"
        print(f"  pack {pack['id']}  {pack['version']}  ({pack['bytes']} bytes, {len(pack['media'])} images, {flag})")
    print(
        f"Coverage: {counts['with content']} of {counts['theory subjects']} theory subjects have content, "
        f"{counts['reviewed']} reviewed."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
