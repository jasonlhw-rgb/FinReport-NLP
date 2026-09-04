"""PDF / text preprocessing utilities."""

from __future__ import annotations

from pathlib import Path

from .utils import ensure_dir


def pdf_to_text(pdf_path: str | Path, txt_path: str | Path | None = None) -> str:
    """Extract text from a PDF using pdfplumber.

    Parameters
    ----------
    pdf_path:
        Source PDF file.
    txt_path:
        Optional destination .txt path. If omitted, text is only returned.
    """
    import pdfplumber

    pdf_path = Path(pdf_path)
    text_parts: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_parts.append(page_text)

    text = "\n".join(text_parts)
    if txt_path is not None:
        txt_path = Path(txt_path)
        ensure_dir(txt_path.parent)
        txt_path.write_text(text, encoding="utf-8")
    return text


def convert_pdf_folder(folder: str | Path, skip_existing: bool = True) -> list[tuple[str, bool]]:
    """Convert all PDFs in a folder to sibling .txt files.

    Returns a list of (filename, success) results.
    """
    folder = Path(folder)
    results: list[tuple[str, bool]] = []
    for pdf_path in sorted(folder.glob("*.pdf")):
        txt_path = pdf_path.with_suffix(".txt")
        if skip_existing and txt_path.exists():
            results.append((pdf_path.name, True))
            continue
        try:
            pdf_to_text(pdf_path, txt_path)
            results.append((pdf_path.name, True))
        except Exception:
            results.append((pdf_path.name, False))
    return results
