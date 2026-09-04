# Publishing Models Beyond GitHub

This guide explains how to publish **mode7** (and future models) on other
platforms. The spaCy model already lives in this repository under
`models/mode7/` (~3.7 MB). Extra hubs are optional but improve discovery.

## 1. GitHub (already done)

- Model directory: [`models/mode7/`](../models/mode7/)
- Optional: attach a zip of `models/mode7` as a **Release** asset
  (`v0.1`) so downloads are one-click.

```bash
# Create a release zip locally
Compress-Archive -Path models/mode7 -DestinationPath mode7-spacy.zip
# Then upload mode7-spacy.zip in GitHub → Releases → Draft a new release
```

## 2. Hugging Face Hub (recommended)

Yes — Hugging Face is a good place for this model, even though it is spaCy
(not Transformers). Many researchers search HF first.

### One-time setup

1. Create an account: https://huggingface.co/join
2. Create an access token (write scope): https://huggingface.co/settings/tokens
3. Install tools:

```bash
pip install huggingface_hub
huggingface-cli login
```

### Create a model repo

Suggested name: `jasonlhw-rgb/finreport-nlp-mode7` (or your HF username).

On the website: **New model** → name `finreport-nlp-mode7` → license MIT → public.

Or via CLI:

```bash
huggingface-cli repo create finreport-nlp-mode7 --type model
```

### Upload mode7

```bash
# From the FinReport-NLP repo root
huggingface-cli upload jasonlhw-rgb/finreport-nlp-mode7 models/mode7 . --repo-type model
```

Or with Python:

```python
from huggingface_hub import HfApi
api = HfApi()
api.upload_folder(
    folder_path="models/mode7",
    repo_id="jasonlhw-rgb/finreport-nlp-mode7",
    repo_type="model",
)
```

### Add a model card (`README.md` on the HF repo)

Include:

- Task: Chinese financial-report section extraction (NER `TARGET_SECTION`)
- Library: spaCy 3.8
- How to load:

```python
import spacy
# after downloading the folder
nlp = spacy.load("path/to/mode7")
```

- Link back to: https://github.com/jasonlhw-rgb/FinReport-NLP
- Dataset / corpus links (caiwushi.net + Google Drive)
- Contact: jason.lhw2025@gmail.com

### Tags to set on HF

`spacy`, `ner`, `zh`, `financial-nlp`, `information-extraction`, `document-ai`

## 3. Optional: Hugging Face Spaces (Demo)

Later you can add a small Gradio/Streamlit demo:

- Upload a short `.txt` report
- Run `mode7` extraction
- Show the extracted MD&A-like section

This is optional (see project Roadmap) and is the highest-visibility next step
after the model card.

## 4. Other platforms

| Platform | Fit for this project | Notes |
|----------|----------------------|-------|
| **Hugging Face Models** | ★★★★★ | Best discovery for NLP models |
| **Hugging Face Spaces** | ★★★★ | Interactive demo |
| **GitHub Releases** | ★★★★ | Simple zip download |
| **Zenodo** | ★★★ | DOI for academic citation |
| **Papers with Code** | ★★ | If you add a paper / benchmark |
| **ModelScope (魔搭)** | ★★★ | Better reach for CN audience |
| **OpenXLab / OpenI** | ★★ | CN academic mirrors |

### Zenodo (DOI)

1. Connect GitHub → Zenodo
2. Enable the FinReport-NLP repo
3. Create a release on GitHub → Zenodo mints a DOI
4. Put the DOI into `CITATION.cff`

### ModelScope (optional, China)

Similar to HF: create a model repo, upload `models/mode7`, write a Chinese
model card, link GitHub + datasets.

## 5. Status (2026-09)

1. Keep `models/mode7` on GitHub — **done**
2. HF model repo + model card — **done** → https://huggingface.co/jasonlhw-rgb/finreport-nlp-mode7
3. GitHub Release zip — **done** → https://github.com/jasonlhw-rgb/FinReport-NLP/releases/tag/v0.1.0
4. Zenodo DOI — **needs your Zenodo login** → see [`zenodo-setup.md`](zenodo-setup.md)
5. (Later) HF Space demo — optional
