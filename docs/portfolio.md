# Portfolio / Resume Copy

Ready-to-use text for resumes, LinkedIn, and project announcements.
Update the GitHub URL after the repository is published.

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

独立设计并实现基于 spaCy NER 的财务报告文本信息抽取系统，针对 20,000+ 份财务报告构建数据预处理、训练样本构建、模型训练、批量推理、目标文本抽取及结果验证完整流程，采用「规则优先 + NER 回退」的混合策略，实现从非结构化财务文档到结构化研究数据的自动化转换。

## English resume

**Financial Report NLP Information Extraction System (FinReport-NLP)**

Designed and developed an end-to-end NLP pipeline for large-scale financial
document information extraction. Processed 20,000+ financial reports and
implemented document preprocessing, training dataset construction, spaCy NER
model training (`TARGET_SECTION`), hybrid rule+model inference, validation,
and structured output generation.

## Technical interview talking points

1. Problem: locate MD&A-like sections across heterogeneous Chinese filings
2. Data: PDF→TXT, keyword filtering, annotated JSON spans
3. Model: `spacy.blank("zh")` + NER, not just regex
4. Iteration: agent6 → agent7 (empty end markers), then 20k batch run
5. Engineering: logging, post-processing, open-source reorganization

## 宣传文案（中文）

两年前，我做过一个比较“笨”但完整的 NLP 项目：面对 2 万多份财务报告，想让机器自动找到「管理层讨论与分析」等目标章节。

从 PDF 文本处理、训练数据构建，到 spaCy NER 训练、批量推理和结果验证，我把整条链路跑了一遍。最近把它整理成开源项目 **FinReport-NLP**——面向大规模财务报告的 NLP 信息抽取 pipeline。

欢迎 Star / Issue / PR。
