import pytest
from unittest.mock import patch
from main import logged_main, unlogged_main


@patch('builtins.input', side_effect=[])
def test_logged_main(mock_input):
    res = logged_main({}, 1)
    pass


@patch('builtins.input', side_effect=[
    'n',
    'joao maria silva santos',
    '12345678921',
    'user@email.com',
    '20/01/1995',
    'rua m, 123, centro  ',
    75991235393,
    1234,
    1234,

    'l',
    '12345678921',
    1234,

    'q'

])
def test_logged_main(mock_input):
    res = unlogged_main()
    pass
