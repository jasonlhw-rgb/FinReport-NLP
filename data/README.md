# Dataset

The original financial-report corpus used during development is **not** included
in this repository, because it contains text derived from real filings.

A small **synthetic** sample dataset is provided for demonstration and
reproducibility:

- `sample/sample_training_data.json` — annotated training records
- `sample/reports/` — plain-text demo reports

Users should provide their own **legally obtained** financial reports when
running the pipeline at scale.

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
