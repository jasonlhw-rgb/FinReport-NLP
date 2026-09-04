# Contributing

Thanks for your interest in FinReport-NLP!

## How to contribute

1. Fork the repository
2. Create a feature branch
3. Make focused changes with clear commits
4. Open a Pull Request describing **why** the change is needed

## Development setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/validate_dataset.py
```

## Guidelines

- Do **not** commit real financial-report corpora, personal data, cookies, tokens, or API keys
- Prefer synthetic or redistributable samples under `data/sample/`
- Keep scripts CLI-friendly (`argparse`), avoid hardcoded local paths
- Match existing code style; add a short note in `docs/` when behavior changes

## Reporting issues

Please include:

- Python / spaCy versions
- Minimal reproducible example
- Expected vs actual behavior
