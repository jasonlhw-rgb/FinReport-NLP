# Portfolio / Resume Copy

Ready-to-use text for resumes, LinkedIn, and project announcements.

**Repo:** https://github.com/jasonlhw-rgb/FinReport-NLP  
**Contact:** jason.lhw2025@gmail.com

## One-line (GitHub Description)

```text
Large-scale NLP pipeline for extracting structured information from financial reports.
```

## Topics (GitHub)

```text
nlp, natural-language-processing, financial-nlp, financial-reports,
information-extraction, document-ai, text-mining, machine-learning,
python, finance, fintech, spacy, ner
```

## 中文简历

**大规模财务报告 NLP 信息抽取系统（FinReport-NLP）**

独立设计并实现基于 spaCy NER 的财务报告文本信息抽取系统。针对约 **22,800** 份财务报告，完成数据预处理、训练样本构建、多轮模型迭代（mode1→mode7）、批量推理、目标文本抽取与结果验证；采用「规则优先 + NER 回退」混合策略。最终 **mode7** 模型在全量语料上稳定完成抽取，并交付给付费委托的博士研究者，对方对结果高度认可。项目已开源，含预训练模型与外部研究数据链接。

## English resume

**Financial Report NLP Information Extraction System (FinReport-NLP)**

Designed and developed an end-to-end NLP pipeline for large-scale financial
document information extraction. Processed ~22,800 financial reports with
document preprocessing, training dataset construction, iterative spaCy NER
training (**mode1→mode7**), hybrid rule+model inference, validation, and
structured output generation. The final **mode7** model was delivered in a
paid PhD research engagement with strong client satisfaction. Open-sourced
with the pretrained model and external corpus links for academic reuse.

## Technical interview talking points

1. Problem: locate MD&A-like sections across heterogeneous Chinese filings
2. Data: PDF→TXT, keyword filtering, annotated JSON spans; ~22.8k corpus
3. Model: `spacy.blank("zh")` + NER; iterated mode1→mode7 (not one-shot)
4. Hybrid: rules first, NER fallback; agent6 → agent7 improvements
5. Impact: paid PhD engagement; client highly satisfied with full-corpus results
6. Open source: model + docs + external data mirrors (caiwushi.net / Drive)

## 宣传文案（中文）

两年前，我做过一个完整的 NLP 工程：面对约 2.28 万份财务报告，要自动抽取「管理层讨论与分析」等目标章节。

从 PDF 文本处理、训练数据构建，到多轮 spaCy NER 训练（一直迭代到 **mode7**）、批量推理和结果验证，整条链路都跑通了。项目最初是一位博士付费委托的数据处理任务——对方拿到全量抽取结果时非常满意。

最近把它整理成开源项目 **FinReport-NLP**（含 mode7 预训练模型）。完整 TXT 语料与训练/测试数据分别在 caiwushi.net 与 Google Drive，欢迎学术同行取用交流：jason.lhw2025@gmail.com

欢迎 Star / Issue / PR。
