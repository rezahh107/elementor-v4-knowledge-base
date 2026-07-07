#!/usr/bin/env python3
"""Render a deterministic Work Package plan."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.wp_decision import load, plan


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-state",
        required=True,
        type=Path,
    )
    parser.add_argument(
        "--output",
        type=Path,
    )
    args = parser.parse_args()

    result = plan(load(args.repo_state))
    output_text = (
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    if args.output:
        args.output.write_text(
            output_text,
            encoding="utf-8",
        )
    print(output_text, end="")
    return 1 if result.get("action") == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
