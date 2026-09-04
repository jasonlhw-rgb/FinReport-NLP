# FinReport-NLP

> Large-scale NLP-based information extraction from financial reports.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![spaCy](https://img.shields.io/badge/NLP-spaCy%20NER-orange.svg)](https://spacy.io/)

FinReport-NLP is an NLP-based document information extraction pipeline designed
to automatically identify and extract target sections from large-scale financial
reports.

The project was originally developed to process **more than 20,000** financial
report documents and extract specific semantic sections such as:

- Management's Discussion and Analysis (管理层讨论与分析 / MD&A)
- Risk Factors
- Business Overview
- Other target financial-report sections

It covers the complete workflow from document preprocessing and dataset
construction to **spaCy NER** model training, hybrid inference, validation, and
large-scale batch extraction.

Originally developed in 2024–2025. Reorganized and open-sourced in 2026.

---

## Features

- Batch processing of large collections of financial documents
- PDF / text preprocessing (`pdfplumber`)
- Training dataset construction & validation
- spaCy Chinese blank model + NER (`TARGET_SECTION`)
- Hybrid extraction: **rules first**, NER fallback
- Batch inference with extraction logs
- Structured text / JSON output

---

## Project Pipeline

```text
Financial Reports
        │
        ▼
PDF / Text Preprocessing
        │
        ▼
Text Cleaning & Keyword Filtering
        │
        ▼
Training Dataset Construction
        │
        ▼
spaCy NER Model Training
        │
        ▼
Hybrid Inference (Rules → NER)
        │
        ▼
Target Section Extraction
        │
        ▼
Validation & Post-processing
        │
        ▼
Structured Output
```

### Example

**Input (excerpt):**

```text
第三节 管理层讨论与分析
报告期内，公司实现营业收入110亿元……
第四节 公司治理
```

**Output:**

```json
{
  "section": "管理层讨论与分析",
  "text": "报告期内，公司实现营业收入110亿元……"
}
```

---

## Tech Stack (verified from original code)

| Component | Choice |
|-----------|--------|
| Framework | [spaCy](https://spacy.io/) `>=3.8,<3.9` |
| Model | `spacy.blank("zh")` + `ner` pipe |
| Label | `TARGET_SECTION` |
| Training | 20 epochs, minibatch=4, dropout=0.2 |
| Hybrid | regex start/end markers → NER fallback |
| PDF | `pdfplumber` |

---

## Installation

```bash
git clone https://github.com/jasonlhw-rgb/FinReport-NLP.git
cd FinReport-NLP
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
# source .venv/bin/activate

pip install -r requirements.txt
python -m spacy download zh_core_web_sm
```

> Note: training uses a **blank** Chinese model (`spacy.blank("zh")`), so the
> pretrained download is optional for the core pipeline. Install it if you want
> additional Chinese NLP utilities.

---

## Quick Start

1. Validate the sample dataset:

```bash
python scripts/validate_dataset.py
```

2. Train a demo NER model:

```bash
python scripts/train.py \
  --data data/sample/sample_training_data.json \
  --output models/target_section_ner \
  --epochs 5
```

3. Extract sections from sample reports:

```bash
python scripts/extract_sections.py \
  --input data/sample/reports \
  --output outputs/ \
  --model models/target_section_ner \
  --use-rules \
  --rules-data data/sample/sample_training_data.json \
  --log outputs/extraction_log.csv
```

---

## Project Structure

```text
FinReport-NLP/
├── src/finreport_nlp/     # Core library
│   ├── preprocessing.py
│   ├── dataset.py
│   ├── training.py
│   ├── inference.py
│   └── utils.py
├── scripts/               # CLI entry points
├── configs/
├── data/sample/           # Synthetic demo data only
├── models/                # Trained models (local / Release)
├── examples/
├── docs/
├── tests/
├── README.md
├── LICENSE
└── requirements.txt
```

---

## Dataset

The original financial-report corpus is **not** included. See [`data/README.md`](data/README.md).

A small synthetic sample is provided for demonstration. Please use your own
legally obtained documents for large-scale runs.

---

## Development History

The project evolved through multiple experimental iterations:

1. Financial document collection and PDF→text conversion
2. Keyword filtering (e.g. 管理层讨论与分析)
3. Training sample construction & JSON normalization
4. spaCy NER experimentation (`extract_agent6`)
5. Rule robustness improvements (`extract_agent7`, optional `end_marker`)
6. Large-scale batch inference (`extract_with_trained_model`)
7. Output validation and post-processing

See [`docs/development-history.md`](docs/development-history.md) for details.

---

## Use Cases

- Financial / academic research
- Financial text mining
- Corporate analysis
- Document intelligence / Document AI
- Alternative financial data construction

---

## Limitations

Extraction quality depends on report format, OCR/PDF text quality, document
structure, language, training data, and section definitions.

This repository is a **research and engineering reference implementation**, not
a production-ready financial data service.

---

## Roadmap

- [ ] Stronger preprocessing for heterogeneous report layouts
- [ ] Multilingual / multi-section support
- [ ] Evaluation benchmarks (Precision / Recall / F1)
- [ ] Pretrained model Release
- [ ] Docker support
- [ ] GitHub Actions CI
- [ ] Optional demo (e.g. Hugging Face Spaces)

---

## Contributing

Contributions, bug reports, and suggestions are welcome.
Please see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Citation

If you use this project in research, please cite it using [`CITATION.cff`](CITATION.cff).

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
