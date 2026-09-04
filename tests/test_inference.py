"""Basic unit tests for FinReport-NLP core helpers."""

from finreport_nlp.inference import extract_with_rules
from finreport_nlp.dataset import load_training_data


def test_extract_with_rules_between_markers():
    text = "AAA\n第三节 管理层讨论与分析\n目标正文\n第四节 公司治理\nBBB"
    result = extract_with_rules(text, "第三节 管理层讨论与分析", "第四节 公司治理")
    assert result == "目标正文"


def test_extract_with_rules_to_eof():
    text = "前言\n第三节 管理层讨论与分析\n一直到结尾"
    result = extract_with_rules(text, "第三节 管理层讨论与分析", None)
    assert result is not None
    assert "一直到结尾" in result


def test_load_sample_training_data():
    items = load_training_data("data/sample/sample_training_data.json")
    assert len(items) >= 1
    assert "input_text" in items[0]
    assert items[0]["target_content"] in items[0]["input_text"]
