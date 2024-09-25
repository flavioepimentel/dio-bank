import pytest
from unittest.mock import patch
from view import unlogged_interface, new_user_form, login_form, logged_interface, login_redirect, account_select, extrato_view, withdrawal_form


@patch('builtins.input', side_effect=['n', 'N', 'l', 'll', 'L', 'Q'])
def test_unlogged_interface(mock_input):
    resultado1 = unlogged_interface()
    assert resultado1 == "n"

    resultado2 = unlogged_interface()
    assert resultado2 == "n"

    resultado1 = unlogged_interface()
    assert resultado1 == "l"

    resultado1 = unlogged_interface()
    assert resultado1 == "ll"

    resultado1 = unlogged_interface()
    assert resultado1 == "l"

    resultado1 = unlogged_interface()
    assert resultado1 == "q"


@patch('builtins.input', side_effect=[
    'joao maria silva santos',
    '12345678921',
    'user@email.com',
    '20/01/1995',
    'rua m, 123, centro  ',
    75991235393,
    1234,
    1234,

    ' joao maria silva santos',
    12345678921,
    'USER@EMAIL.COM ',
    '20/01/1995 ',
    'rua m, 123, centro  ',
    '759912 35393',
    '12 34',
    '12 34',

    'joao maria silva santos ',
    '123.456.789-21',
    '  USER  @ EMAIL. COM ',
    '20/01/1995',
    'rua m, 123, centro  ',
    '(75) 9 9123-5393',
    '12 3  4  ',
    '12 3  4  ',

])
def test_new_user_form(mock_input):
    res = new_user_form()
    assert res == {
        "user": 'JOAO MARIA SILVA SANTOS',
        "cpf": '12345678921',
        "email": 'user@email.com',
        "birth_date": '20/01/1995',
        "address": 'RUA M, 123, CENTRO',
        "contact_number": '75991235393',
        "password": '1234',
        "password_conf": '1234'
    }

    res = new_user_form()
    assert res == {
        "user": 'JOAO MARIA SILVA SANTOS',
        "cpf": '12345678921',
        "email": 'user@email.com',
        "birth_date": '20/01/1995',
        "address": 'RUA M, 123, CENTRO',
        "contact_number": '75991235393',
        "password": '1234',
        "password_conf": '1234'
    }

    res = new_user_form()
    assert res == {
        "user": 'JOAO MARIA SILVA SANTOS',
        "cpf": '12345678921',
        "email": 'user@email.com',
        "birth_date": '20/01/1995',
        "address": 'RUA M, 123, CENTRO',
        "contact_number": '75991235393',
        "password": '1234',
        "password_conf": '1234'
    }


@patch('builtins.input', side_effect=[
    ' 12345678921 ',
    1234,

    12345678921,
    '12 34',

    '  USER  @ EMAIL. COM ',
    '12 3  4  ',

    'USER@EMAIL.COM ',
    '1234'

])
def test_login_form(mock_input):
    res = login_form()
    assert res == {
        "cpf": '12345678921',
        "email": '12345678921',
        "password": '1234'
    }

    res = login_form()
    assert res == {
        "cpf": '12345678921',
        "email": '12345678921',
        "password": '1234'
    }

    res = login_form()
    assert res == {
        "cpf": 'user@email.com',
        "email": 'user@email.com',
        "password": '1234'
    }

    res = login_form()
    assert res == {
        "cpf": 'user@email.com',
        "email": 'user@email.com',
        "password": '1234'
    }


@patch('builtins.input', return_value='2')
def test_account_select(mock_input):
    res = account_select([1, 5, 8])
    assert res == 5


@patch('builtins.input', side_effect=[' S ', 's', 'N', 'n'])
def test_login_redirect(mock_input):
    res = login_redirect()
    assert res == 's'

    res = login_redirect()
    assert res == 's'

    res = login_redirect()
    assert res == 'n'

    res = login_redirect()
    assert res == 'n'


@patch('builtins.input', side_effect=[' D ', 'S ', ' e ', 'Q'])
def test_logged_interface(mock_input):
    res = logged_interface(100)
    assert res == 'd'

    res = logged_interface(100)
    assert res == 's'

    res = logged_interface(100)
    assert res == 'e'

    res = logged_interface(100)
    assert res == 'q'


@patch('builtins.input', side_effect=[])
def test_extrato_view(mock_input):
    res = extrato_view([{
        "timestamp": '2024-09-17 23:39:35.300690',
        "cpf:": '12345678921',
        "email": 'user@email.com',
        "account_number": 1,
        "operation": "Deposito",
        "value": 60.0,
        "location": "New York"
    },
        {
        "timestamp": '2024-09-18 13:52:05.300690',
            "cpf:": '12345678921',
            "email": 'user@email.com',
            "account_number": 1,
            "operation": "Saque",
            "value": 50.0,
            "location": "New York"
    }], 10)
    assert res == None


@patch('builtins.input', side_effect=[
    'test',
    -50,
    '10,50',
    '25',
    80,
    '999.9',
    '05,50',
    15.75
])
def test_withdrawal_form(mock_input):
    with pytest.raises(ValueError):
        withdrawal_form()

    with pytest.raises(ValueError):
        withdrawal_form()

    res = withdrawal_form()
    assert res == 10.5

    res = withdrawal_form()
    assert res == 25.0

    res = withdrawal_form()
    assert res == 80.0

    res = withdrawal_form()
    assert res == 999.9

    res = withdrawal_form()
    assert res == 5.5

    res = withdrawal_form()
    assert res == 15.75
