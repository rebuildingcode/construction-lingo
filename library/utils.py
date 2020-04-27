import logging

import spacy
from spacy.cli.download import download as spacy_download

log = logging.getLogger(__name__)


def get_spacy_model(spacy_model_name='en_core_web_sm'):
    try:
        nlp = spacy.load(spacy_model_name)
    except OSError:
        log.info('The %s model was not found. Loading "en_core_web_sm"...')
        spacy_download('en_core_web_sm')
        nlp = spacy.load('en_core_web_sm')
    return nlp


def get_pos(s):
    """Return parts of speech for a string"""
    nlp = get_spacy_model()
    doc = nlp(s)

    pos = []
    for token in doc:
        pos.append(token.pos_)

    return pos
