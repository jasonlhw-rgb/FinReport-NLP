#!/usr/bin/env python3
"""Extract target sections from financial-report text files."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from finreport_nlp.dataset import load_training_data
from finreport_nlp.inference import process_files
from finreport_nlp.utils import ensure_dir


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Batch extract target sections")
    p.add_argument("--input", required=True, help="Folder of .txt reports")
    p.add_argument("--output", default=str(ROOT / "outputs"), help="Output folder")
    p.add_argument(
        "--model",
        default=str(ROOT / "models" / "target_section_ner"),
        help="Path to trained spaCy model directory",
    )
    p.add_argument(
        "--rules-data",
        default=None,
        help="Optional training JSON providing start/end markers for rule extraction",
    )
    p.add_argument(
        "--use-rules",
        action="store_true",
        help="Prefer rule-based extraction when markers are available",
    )
    p.add_argument(
        "--log",
        default=None,
        help="Optional CSV path for extraction status log",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    training_data = load_training_data(args.rules_data) if args.rules_data else None
    logs = process_files(
        args.input,
        args.output,
        model_path=args.model,
        use_rules=args.use_rules,
        training_data=training_data,
    )
    if args.log:
        log_path = Path(args.log)
        ensure_dir(log_path.parent)
        with open(log_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["file_name", "status"])
            writer.writeheader()
            writer.writerows(logs)
        print(f"Log saved to {log_path}")


if __name__ == "__main__":
    main()
