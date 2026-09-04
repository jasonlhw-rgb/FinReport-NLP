# Development History

This document preserves the evolution of FinReport-NLP from the original
experimental scripts (2024–2025) to the reorganized open-source layout (2026).

## Real-world deployment note

The pipeline was originally built to fulfill a **paid research data-processing
engagement** for a PhD researcher: extract target sections (especially
管理层讨论与分析) from a large filing corpus.

The final model (**mode7**) was used to run extraction over about **22,800**
plain-text reports. The delivered results met the client's needs; the
researcher was highly satisfied upon receiving the outputs. This is the
project's strongest real-world validation — not a lab demo only.

## Model iteration: mode1 → mode7

Training was **not** a single shot. Multiple model versions were trained and
compared as data and extraction logic improved:

| Round | Artifact / focus | Notes |
|-------|------------------|-------|
| early | mode1 … mode5 (intermediate) | Dataset / training experiments while iterating on `training_data*.json` |
| mode6 | paired with `extract_agent6` + `training_data6` | First packaged spaCy NER + hybrid rules pipeline |
| **mode7** | paired with `extract_agent7` + `training_data7` | **Final** model: stronger rule fallback (empty `end_marker`), best large-scale results |

**mode7** is the version published under [`models/mode7/`](../models/mode7/).

Training terminal evidence (20 epochs, loss drop, then batch extraction):

![mode7 training terminal](images/mode7_training_terminal.jpg)

## Timeline

### Version 0.1 — Rule / keyword filtering

- PDF → TXT conversion (`pdf_to_txt_pdfplumber_优化.py`)
- Keyword scan for `管理层讨论与分析` (`0_（按关键词）遍历txt文件内容.py`)
- Random sampling for annotation (`1_随机抽取样本文件.py`)

### Version 0.2 — Dataset construction

- TXT → JSON conversion (`2_将多行文本转换为一行JSON字符串*.py`)
- JSON validation (`3_验证修复后的json文件.py`)
- Iterative training corpora: `training_data.json` → `training_data7.json`

### Version 0.3 — spaCy NER training (`extract_agent6` / mode6)

- `spacy.blank("zh")` + NER pipe
- Entity label: `TARGET_SECTION`
- Span construction via `input_text.find(target_content)`
- Hybrid inference: rules first, model fallback
- Training: 20 epochs, minibatch size 4, dropout 0.2

### Version 0.4 — Final model (`extract_agent7` / **mode7**)

- Allow missing / empty `end_marker` (extract to EOF)
- Continued hybrid strategy
- Final artifact: `models/mode7/`

### Version 0.5 — Large-scale batch extraction (~22,800 files)

- Inference-only script (`extract_with_trained_model.py`)
- Full corpus-scale run on ~22,800 plain-text reports
- Excel extraction logs for success/failure tracking
- Post-processing helpers (rename `extracted_*`, folder matching)
- Delivered to the PhD client with strong positive feedback

### Version 0.6 — Open-source reorganization (2026)

- Package layout: `src/finreport_nlp` + `scripts/`
- Publish `models/mode7` + synthetic sample dataset
- External links for full corpora (caiwushi.net + Google Drive)
- MIT license, docs, and reproducibility scripts
- Download scraper **intentionally excluded** from the public tree

## Mapping: historical scripts → current modules

| Historical file | Current location |
|-----------------|------------------|
| `extract_agent6.py` / `extract_agent7.py` | `src/finreport_nlp/training.py`, `inference.py` |
| `extract_with_trained_model.py` | `scripts/extract_sections.py` |
| `pdf_to_txt_pdfplumber_优化.py` | `src/finreport_nlp/preprocessing.py`, `scripts/convert_pdfs.py` |
| `2_*.py` / `3_*.py` | `scripts/prepare_dataset.py`, `scripts/validate_dataset.py` |
| `pdf下载.py` | **Not published** (contained session cookies) |

## Design notes

The project is best understood as a **hybrid IE pipeline**:

```text
regex markers (when available)
        │
        ├─ success → extracted section
        │
        └─ fail → spaCy NER (TARGET_SECTION)
```

This combination was practical for heterogeneous Chinese financial-report
layouts where pure rules were brittle and pure NER needed better coverage.
