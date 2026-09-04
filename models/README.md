# Models

Trained spaCy models are **not** committed to this repository by default.

## Local historical model

During the original project (2024–2025), a spaCy Chinese NER model was trained
and saved locally as `mode7/` (label: `TARGET_SECTION`). That directory is
gitignored because it belongs to the private working tree.

To reproduce training from the sample dataset:

```bash
python scripts/train.py \
  --data data/sample/sample_training_data.json \
  --output models/target_section_ner
```

For larger production models, prefer publishing via:

- GitHub Release assets
- Hugging Face Model Hub

and linking them from the README.
