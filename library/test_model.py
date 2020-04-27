import spacy

from .model import CodeReader


def test_code_reader():
    model = CodeReader()

    assert type(model.nlp) == spacy.lang.en.English
