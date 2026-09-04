# Architecture

```text
┌─────────────────────────────────────────────────────────┐
│                     FinReport-NLP                       │
├─────────────────────────────────────────────────────────┤
│  preprocessing  →  dataset  →  training  →  inference   │
│       │               │            │            │       │
│   PDF/TXT          JSON NER     spaCy blank   Rules+NER │
│                   spans         zh + NER      batch I/O │
└─────────────────────────────────────────────────────────┘
```

## Core packages

- `finreport_nlp.preprocessing` — PDF text extraction
- `finreport_nlp.dataset` — training data load/save, TXT→JSON
- `finreport_nlp.training` — spaCy NER training loop
- `finreport_nlp.inference` — hybrid rule + model extraction

## CLI scripts

| Script | Purpose |
|--------|---------|
| `scripts/convert_pdfs.py` | PDF → TXT |
| `scripts/prepare_dataset.py` | TXT folder → JSON records |
| `scripts/validate_dataset.py` | Schema / span checks |
| `scripts/train.py` | Train NER model |
| `scripts/extract_sections.py` | Batch extraction |

## Data flow

1. User supplies legally obtained reports (PDF or TXT)
2. Optional PDF conversion
3. Annotated JSON built offline (markers + target span)
4. Train `TARGET_SECTION` NER
5. Run hybrid batch extraction → `outputs/`
