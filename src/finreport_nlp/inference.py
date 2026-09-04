"""Hybrid rule + NER inference for target-section extraction."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import spacy

from .training import LABEL
from .utils import ensure_dir, list_txt_files


def extract_with_rules(
    file_content: str,
    start_marker: str,
    end_marker: str | None = None,
) -> str | None:
    """Extract text between markers using regular expressions.

    If ``end_marker`` is empty/None, extract from start_marker to EOF
    (behavior introduced in extract_agent7).
    """
    if not end_marker:
        pattern = re.compile(re.escape(start_marker) + r"(.*)", re.DOTALL)
    else:
        pattern = re.compile(
            re.escape(start_marker) + r"(.*?)" + re.escape(end_marker),
            re.DOTALL,
        )
    match = pattern.search(file_content)
    if match:
        return match.group(1).strip()
    return None


def extract_with_model(nlp, file_content: str) -> str:
    """Extract TARGET_SECTION entities using a loaded spaCy model."""
    # spaCy has practical length limits; truncate extremely long docs safely.
    max_length = getattr(nlp, "max_length", 1_000_000)
    if len(file_content) > max_length:
        file_content = file_content[:max_length]
    doc = nlp(file_content)
    sections = [ent.text for ent in doc.ents if ent.label_ == LABEL]
    return "\n".join(sections)


def load_model(model_path: str | Path):
    return spacy.load(str(model_path))


def process_files(
    input_folder: str | Path,
    output_folder: str | Path,
    model_path: str | Path | None = None,
    *,
    use_rules: bool = False,
    training_data: list[dict[str, Any]] | None = None,
    nlp=None,
) -> list[dict[str, str]]:
    """Batch-extract target sections from text files.

    Strategy (historical pipeline):
    1. If ``use_rules`` and matching markers exist, prefer rule extraction.
    2. Otherwise fall back to the spaCy NER model.
    """
    input_folder = Path(input_folder)
    output_folder = ensure_dir(output_folder)

    if nlp is None and model_path is not None:
        nlp = load_model(model_path)

    # Optional filename -> markers lookup for rule-based extraction
    marker_map: dict[str, dict[str, str]] = {}
    if training_data:
        for item in training_data:
            marker_map[item.get("file_name", "")] = item

    logs: list[dict[str, str]] = []
    for txt_path in list_txt_files(input_folder):
        content = txt_path.read_text(encoding="utf-8")
        extracted: str | None = None

        if use_rules and txt_path.name in marker_map:
            item = marker_map[txt_path.name]
            extracted = extract_with_rules(
                content,
                item.get("start_marker", ""),
                item.get("end_marker"),
            )

        if not extracted and nlp is not None:
            extracted = extract_with_model(nlp, content) or None

        out_path = output_folder / f"extracted_{txt_path.name}"
        out_path.write_text(extracted or "", encoding="utf-8")
        status = "Success" if extracted else "Failed"
        logs.append({"file_name": txt_path.name, "status": status})
        print(f"[{status}] {txt_path.name} -> {out_path.name}")

    return logs
