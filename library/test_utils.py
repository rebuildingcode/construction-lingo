import pytest
from unittest import mock

from .utils import get_pos, get_spacy_model


def test_get_pos():
    s = 'This house has 3 bedrooms and 2 bathrooms.'
    pos = get_pos(s)

    assert pos == ['DET', 'NOUN', 'AUX', 'NUM', 'NOUN', 'CCONJ', 'NUM',
                   'NOUN', 'PUNCT']


def test_get_invalid_nlp_model():
    with mock.patch('library.utils.log.info') as mock_log:
        nlp = get_spacy_model('any_model')

    mock_log.assert_called_with(
        'The %s model was not found. Loading "en_core_web_sm"...')
