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


def func_a():
    return input("Digite algo para func_a: ")


def func_b(param):
    return param * 2


def func_c(param):
    return param + 5


def main_function():
    a = func_a()
    b = func_b(int(a))
    c = func_c(b)
    return c


@patch('builtins.input', side_effect=['10'])
@patch('__main__.func_b', return_value=20)
@patch('__main__.func_c', return_value=25)
def test_main_function(mock_input, mock_func_b, mock_func_c):
    result = main_function()
    assert result == 25
    mock_input.assert_called_once()
    mock_func_b.assert_called_once_with(10)
    mock_func_c.assert_called_once_with(20)
