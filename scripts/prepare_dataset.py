#!/usr/bin/env python3
"""Convert a folder of .txt files into JSON records for dataset building."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from finreport_nlp.dataset import txt_folder_to_json


def main() -> None:
    p = argparse.ArgumentParser(description="Convert txt folder to JSON files")
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    n = txt_folder_to_json(args.input, args.output)
    print(f"Converted {n} files -> {args.output}")


if __name__ == "__main__":
    main()
