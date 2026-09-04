# 我是如何用 NLP 从 2 万多份财报中自动提取「管理层讨论与分析」的？

> 开源项目：[FinReport-NLP](https://github.com/jasonlhw-rgb/FinReport-NLP)  
> 预训练模型：[`mode7`（GitHub / Hugging Face）](https://huggingface.co/jasonlhw-rgb/finreport-nlp-mode7)  
> DOI：https://doi.org/10.5281/zenodo.22304240  
> 联系邮箱：jason.lhw2025@gmail.com

两年前，我接到一个很具体、也很「笨重」的任务：面对大约 **22,800** 份财务报告文本，把其中的「管理层讨论与分析」（MD&A）等目标章节自动抽出来，交给一位博士做研究。

不是做一个 Demo 分类器，而是要把整条链路跑通——PDF/文本预处理、训练数据构建、模型训练、批量推理、结果校验——并且结果必须能交付。

最近我把这套东西重新整理成了开源项目 **FinReport-NLP**。这篇文章按真实工程路径，把关键决策和踩坑写清楚。

---

## 1. 为什么不能只靠正则？

财报版式极度不统一：

- 章节标题写法不同（「第三节 / 第五节 / （一）」……）
- 结束边界不稳定（有的后面没有清晰的下一节标题）
- 同一公司不同年份结构也会变

纯 `re.search` 在几百份上还能凑合，到上万份就会大量漏抽、截断、串段。

所以最终方案是 **混合抽取**：

```text
规则（起止标记）优先
        │
        ├─ 成功 → 直接输出
        │
        └─ 失败 → spaCy NER（TARGET_SECTION）兜底
```

---

## 2. 数据怎么准备？

大致流程：

1. PDF → TXT（`pdfplumber`）
2. 关键词过滤（先筛出包含「管理层讨论与分析」的文件）
3. 抽样标注：`input_text` + `target_content` + `start_marker` / `end_marker`
4. 做成 JSON 训练集，并校验 `target_content` 必须是 `input_text` 的连续子串

这一步很枯燥，但决定了后面 NER 能不能训起来。

开源仓库里只放了**合成样例数据**。完整约 2.28 万份 TXT、以及训练/测试等较小数据集，分别放在：

- 全量 TXT：https://caiwushi.net/
- 训练/测试等：Google Drive（见仓库 `data/README.md`）

---

## 3. 模型：spaCy 中文空白模型 + NER

最终技术选型（以真实代码为准）：

| 项目 | 选择 |
|------|------|
| 框架 | spaCy 3.8 |
| 底座 | `spacy.blank("zh")` |
| 任务 | NER |
| 标签 | `TARGET_SECTION` |
| 训练 | 20 epoch，batch=4，dropout=0.2 |

把「目标章节整段」标成一个很长的实体跨度，让模型学习「哪一段是要抽的内容」。

这不是最 fancy 的方案，但对当时的目标——**可交付的大规模抽取**——非常务实。

---

## 4. 为什么有 mode1 到 mode7？

很多人开源时只放最终模型，看起来像「一次训成」。

真实情况是：**连续迭代了多个版本**。数据在改，规则在改，模型也在换。`extract_agent6` → `extract_agent7`，最终定稿 **mode7**：

- 规则侧增强：允许 `end_marker` 为空（抽到文末）
- 模型侧：在更完整的 `training_data7` 上训练
- 工程侧：独立推理脚本 + Excel 日志，支撑上万文件批处理

训练日志里能看到 loss 从极高快速下降，并最终收敛（仓库 README 里有终端截图）。

---

## 5. 大规模跑批：22,800 份

mode7 定稿后，我对全量文本做了批量抽取。结果目录里大约 **22,800** 个输出文件；打开若干样本可以看到，抽出的正是「管理层讨论与分析」正文（含表格化财务对比等内容）。

这不是实验室小样本幻想，而是真实交付场景：博士客户拿到结果时非常满意。对我来说，这比刷一个排行榜分数更有说服力——**它解决了真实研究数据问题**。

---

## 6. 开源时我刻意做了什么、没做什么？

### 做了

- 重组为 `src/` + `scripts/` 可复现结构
- 发布 **mode7**（仓库内 + Release zip + Hugging Face）
- 写清技术栈、历史迭代、数据获取方式
- MIT 许可，方便学习与二次开发

### 没做 / 刻意排除

- 不把含 Cookie 的下载脚本开源
- 不把完整原始语料直接塞进 GitHub（体量与版权风险）
- 不虚构 BERT/大模型叙事——用的就是 spaCy NER + 规则混合

---

## 7. 你怎么快速试用？

```bash
git clone https://github.com/jasonlhw-rgb/FinReport-NLP.git
cd FinReport-NLP
pip install -r requirements.txt

python scripts/extract_sections.py \
  --input data/sample/reports \
  --output outputs/ \
  --model models/mode7
```

Hugging Face 模型页：

https://huggingface.co/jasonlhw-rgb/finreport-nlp-mode7

---

## 8. 局限与后续

- 效果依赖 PDF 转文本质量、版式、标注一致性
- 目前更偏工程参考实现，不是生产级数据服务
- 后续可做：定量 P/R/F1、多章节/多语言、HF Spaces Demo、更强预处理

如果你在做金融文本挖掘、财报结构化、Document AI，欢迎直接用，也欢迎提 Issue。

有学术合作或数据使用问题，可以邮件联系：**jason.lhw2025@gmail.com**

---

## 一句话总结

FinReport-NLP 想证明的不是「我会调用某个大模型 API」，而是：

> 面对两万份真实财报，能从 0 到 1 把数据、标注、训练、迭代、批处理、交付整条 NLP 工程链路做完，并开源复盘。

如果这篇文章或项目对你有帮助，欢迎 Star，也欢迎分享你的改进。
