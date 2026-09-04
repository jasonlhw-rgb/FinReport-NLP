#!/usr/bin/env python3
"""Validate that a training JSON file is well-formed."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from finreport_nlp.dataset import load_training_data


REQUIRED = ("file_name", "input_text", "target_content")


def main() -> None:
    p = argparse.ArgumentParser(description="Validate training dataset JSON")
    p.add_argument(
        "--data",
        default=str(ROOT / "data" / "sample" / "sample_training_data.json"),
    )
    args = p.parse_args()

    items = load_training_data(args.data)
    print(f"Loaded {len(items)} records from {args.data}")

    errors = 0
    for i, item in enumerate(items):
        for key in REQUIRED:
            if key not in item:
                print(f"[{i}] missing key: {key}")
                errors += 1
                continue
        target = item.get("target_content", "")
        text = item.get("input_text", "")
        if target and target not in text:
            print(f"[{i}] target_content not found in input_text: {item.get('file_name')}")
            errors += 1

    if errors:
        print(f"Validation finished with {errors} issue(s).")
        sys.exit(1)
    print("Validation OK.")


if __name__ == "__main__":
    main()
