"""Dataset loading and construction helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, save_json


def load_training_data(path: str | Path) -> list[dict[str, Any]]:
    """Load training data from JSON.

    Expected format::

        {"data": [{"file_name", "input_text", "target_content",
                   "start_marker", "end_marker"}, ...]}
    """
    raw = load_json(path)
    if isinstance(raw, dict) and "data" in raw:
        return list(raw["data"])
    if isinstance(raw, list):
        return raw
    raise ValueError(f"Unsupported training data format: {path}")


def save_training_data(items: list[dict[str, Any]], path: str | Path) -> None:
    save_json({"data": items}, path)


def txt_folder_to_json(input_folder: str | Path, output_folder: str | Path) -> int:
    """Convert each .txt file into a simple JSON record."""
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    count = 0
    for txt_path in sorted(input_folder.glob("*.txt")):
        content = txt_path.read_text(encoding="utf-8")
        save_json(
            {"file_name": txt_path.name, "content": content},
            output_folder / f"{txt_path.stem}.json",
        )
        count += 1
    return count


def filter_files_by_keyword(
    source_folder: str | Path,
    destination_folder: str | Path,
    keyword: str = "管理层讨论与分析",
) -> list[str]:
    """Copy text files that contain a keyword into a destination folder."""
    import shutil

    source_folder = Path(source_folder)
    destination_folder = Path(destination_folder)
    destination_folder.mkdir(parents=True, exist_ok=True)
    matched: list[str] = []
    for txt_path in sorted(source_folder.glob("*.txt")):
        content = txt_path.read_text(encoding="utf-8")
        if keyword in content:
            shutil.copy2(txt_path, destination_folder / txt_path.name)
            matched.append(txt_path.name)
    return matched
