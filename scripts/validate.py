#!/usr/bin/env python3
"""Check every source file. Exit code 1 if anything is wrong.

    python3 scripts/validate.py                  # normal check
    python3 scripts/validate.py --require-complete
        # also fail while any theory subject in the catalog has no reviewed content
        # (use before an app release, since the app ships only when all content is done)
"""

import argparse
import sys

from content_lib import Report, coverage, validate_all


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--require-complete", action="store_true", help="fail unless every theory subject has reviewed content")
    parser.add_argument("--list-missing", action="store_true", help="print every theory subject that has no content yet")
    args = parser.parse_args()

    report = Report()
    validated = validate_all(report)

    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")

    if validated:
        cov = coverage(validated)
        counts = cov["counts"]
        print(
            f"\nCoverage: {counts['with content']} of {counts['theory subjects']} theory subjects have content, "
            f"{counts['reviewed']} reviewed."
        )
        if args.list_missing:
            for sid in cov["missing"]:
                print(f"  no content: {sid}")
        if args.require_complete and (counts["reviewed"] < counts["theory subjects"]):
            print("ERROR: --require-complete: not every theory subject has reviewed content yet.")
            return 1

    if report.errors:
        print(f"\n{len(report.errors)} error(s). Nothing was published.")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
