---
language:
  - zh
license: mit
library_name: spacy
tags:
  - spacy
  - ner
  - zh
  - financial-nlp
  - information-extraction
  - document-ai
  - finreport-nlp
pipeline_tag: token-classification
---

# FinReport-NLP mode7

Final spaCy Chinese NER model from **[FinReport-NLP](https://github.com/jasonlhw-rgb/FinReport-NLP)** for extracting target sections (e.g. 管理层讨论与分析 / MD&A) from financial reports.

## Model details

| Item | Value |
|------|--------|
| Framework | spaCy `>=3.8.3,<3.9.0` |
| Base | `spacy.blank("zh")` + `ner` |
| Label | `TARGET_SECTION` |
| Iteration | Final model after **mode1 → mode7** |
| Scale | Applied to ~**22,800** plain-text reports in production |

## How to use

```bash
# clone or download this model folder
pip install "spacy>=3.8.0,<3.9.0"
```

```python
import spacy

nlp = spacy.load(".")  # or path to the downloaded model directory
text = open("report.txt", encoding="utf-8").read()
doc = nlp(text)
for ent in doc.ents:
    if ent.label_ == "TARGET_SECTION":
        print(ent.text[:500])
```

Or use the GitHub CLI pipeline:

```bash
git clone https://github.com/jasonlhw-rgb/FinReport-NLP.git
cd FinReport-NLP
pip install -r requirements.txt
python scripts/extract_sections.py \
  --input data/sample/reports \
  --output outputs/ \
  --model models/mode7
```

## Datasets

- Full TXT corpus (~22,800): https://caiwushi.net/
- Training / test / smaller sets: [Google Drive](https://drive.google.com/drive/folders/19Qco5VdHnL1niEejzCE-LQr3aiEFF6E-?usp=drive_link)

## Links

- GitHub: https://github.com/jasonlhw-rgb/FinReport-NLP
- Release zip: https://github.com/jasonlhw-rgb/FinReport-NLP/releases
- Contact: jason.lhw2025@gmail.com

## Citation

Please cite the GitHub repository / `CITATION.cff` when using this model in research.

## License

MIT
