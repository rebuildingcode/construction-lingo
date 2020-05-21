import pytest
import spacy

from spacy.cli.download import download as spacy_download


@pytest.fixture()
def default_nlp_model():  # pragma: no cover
    spacy_download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')
    return nlp
