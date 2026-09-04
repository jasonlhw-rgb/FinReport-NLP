# Dataset

This repository only ships a small **synthetic** sample under `data/sample/`
for quick demos. Larger corpora used in the original project are hosted
externally (for academic / research use).

## External corpora (research access)

| Resource | Contents | Link |
|----------|----------|------|
| Full plain-text corpus | ~**22,800** financial-report `.txt` files | https://caiwushi.net/ |
| Training / test / smaller datasets | Annotated training sets, test sets, and related smaller files | [Google Drive folder](https://drive.google.com/drive/folders/19Qco5VdHnL1niEejzCE-LQr3aiEFF6E-?usp=drive_link) |

Please respect applicable copyright and data-use rules when downloading or
redistributing filing-derived text. For questions about academic reuse,
contact: **jason.lhw2025@gmail.com**.

## In-repo sample

- `sample/sample_training_data.json` — annotated training records (synthetic)
- `sample/reports/` — plain-text demo reports (synthetic)

## Training record schema

```json
{
  "data": [
    {
      "file_name": "sample_report_01.txt",
      "input_text": "... full report text ...",
      "target_content": "... target section body ...",
      "start_marker": "第三节 管理层讨论与分析",
      "end_marker": "第四节 公司治理"
    }
  ]
}
```

`target_content` must be a contiguous substring of `input_text` so that spaCy
NER spans can be constructed automatically.
