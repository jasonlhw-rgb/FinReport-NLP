#!/usr/bin/env python3
"""Train the FinReport-NLP spaCy NER model."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from finreport_nlp.training import train_ner_model


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Train TARGET_SECTION NER model")
    p.add_argument(
        "--data",
        default=str(ROOT / "data" / "sample" / "sample_training_data.json"),
        help="Path to training JSON",
    )
    p.add_argument(
        "--output",
        default=str(ROOT / "models" / "target_section_ner"),
        help="Directory to save the trained spaCy model",
    )
    p.add_argument("--epochs", type=int, default=20)
    p.add_argument("--batch-size", type=int, default=4)
    p.add_argument("--dropout", type=float, default=0.2)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    train_ner_model(
        args.data,
        args.output,
        n_epochs=args.epochs,
        batch_size=args.batch_size,
        dropout=args.dropout,
    )


if __name__ == "__main__":
    main()
