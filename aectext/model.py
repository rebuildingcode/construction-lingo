import spacy

from .utils import get_spacy_model


class CodeReader:
    def __init__(self):
        self.nlp = get_spacy_model()