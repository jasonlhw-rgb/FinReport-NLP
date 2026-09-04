"""spaCy NER model training for target-section extraction."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import spacy
from spacy.training import Example
from spacy.util import minibatch

from .dataset import load_training_data


LABEL = "TARGET_SECTION"


def build_examples(nlp, training_data: list[dict[str, Any]]) -> list[Example]:
    """Build spaCy Example objects from annotated training records."""
    examples: list[Example] = []
    for item in training_data:
        input_text = item["input_text"]
        target_content = item["target_content"]
        start = input_text.find(target_content)
        if start == -1:
            continue
        end = start + len(target_content)
        annotations = {"entities": [(start, end, LABEL)]}
        doc = nlp.make_doc(input_text)
        examples.append(Example.from_dict(doc, annotations))
    return examples


def train_ner_model(
    training_data_path: str | Path,
    model_output_path: str | Path,
    *,
    n_epochs: int = 20,
    batch_size: int = 4,
    dropout: float = 0.2,
    lang: str = "zh",
) -> Path:
    """Train a blank-language spaCy NER model for TARGET_SECTION span detection.

    This mirrors the historical FinReport-NLP training pipeline
    (extract_agent6 / extract_agent7): Chinese blank model + NER pipe.
    """
    training_data = load_training_data(training_data_path)
    nlp = spacy.blank(lang)
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    ner.add_label(LABEL)
    train_data = build_examples(nlp, training_data)
    if not train_data:
        raise ValueError("No valid training examples found (target_content not located in input_text).")

    optimizer = nlp.begin_training()
    for epoch in range(n_epochs):
        losses: dict[str, float] = {}
        batches = minibatch(train_data, size=batch_size)
        for batch in batches:
            nlp.update(batch, drop=dropout, sgd=optimizer, losses=losses)
        print(f"Epoch {epoch + 1}/{n_epochs}, Losses: {losses}")

    model_output_path = Path(model_output_path)
    model_output_path.mkdir(parents=True, exist_ok=True)
    nlp.to_disk(model_output_path)
    print(f"Model saved to {model_output_path}")
    return model_output_path
