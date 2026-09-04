#!/usr/bin/env python3
"""Convert PDFs in a folder to plain-text files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from finreport_nlp.preprocessing import convert_pdf_folder


def main() -> None:
    p = argparse.ArgumentParser(description="PDF to TXT conversion")
    p.add_argument("--input", required=True, help="Folder containing PDF files")
    args = p.parse_args()
    results = convert_pdf_folder(args.input)
    ok = sum(1 for _, success in results if success)
    print(f"Done: {ok}/{len(results)} succeeded")


if __name__ == "__main__":
    main()
