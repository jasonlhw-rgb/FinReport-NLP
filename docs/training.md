# Training

## Goal

Learn to locate a target section span (e.g. 管理层讨论与分析) inside a full
financial-report text document.

## Method

1. Load annotated JSON (`input_text`, `target_content`)
2. Locate `target_content` offsets inside `input_text`
3. Create spaCy NER entities labeled `TARGET_SECTION`
4. Train `spacy.blank("zh")` with the `ner` pipe
5. Save model with `nlp.to_disk(...)`

## Command

```bash
python scripts/train.py \
  --data data/sample/sample_training_data.json \
  --output models/target_section_ner \
  --epochs 20 \
  --batch-size 4 \
  --dropout 0.2
```

## Tips for real corpora

- Keep `target_content` an **exact** substring of `input_text`
- Prefer consistent section markers when using `--use-rules`
- Start with a small validated set, then scale annotations
- Evaluate on a held-out report set before large-scale runs
