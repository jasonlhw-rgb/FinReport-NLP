# Models

## mode7 (final production model) — included

The final trained spaCy Chinese NER model from the original project is published
in this repository:

```text
models/mode7/
```

| Item | Detail |
|------|--------|
| Framework | spaCy `>=3.8.3,<3.9.0` |
| Base | `spacy.blank("zh")` + `ner` |
| Label | `TARGET_SECTION` |
| Size | ~3.7 MB |
| Role | Final model after iterative training rounds (mode1 → mode7) |

### Load and extract

```bash
python scripts/extract_sections.py \
  --input data/sample/reports \
  --output outputs/ \
  --model models/mode7
```

```python
import spacy
nlp = spacy.load("models/mode7")
doc = nlp(open("report.txt", encoding="utf-8").read())
print([ent.text for ent in doc.ents if ent.label_ == "TARGET_SECTION"])
```

### Training evidence

See the original training terminal log (loss converging over 20 epochs, then
batch extraction):

![mode7 training terminal](../docs/images/mode7_training_terminal.jpg)

### Retrain a demo model from sample data

```bash
python scripts/train.py \
  --data data/sample/sample_training_data.json \
  --output models/target_section_ner
```

### Publish elsewhere

See [`docs/publishing.md`](../docs/publishing.md) for Hugging Face, Zenodo,
ModelScope, and GitHub Releases.
