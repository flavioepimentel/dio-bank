from unittest.mock import patch
from view import unlogged_interface, new_user_form, login_form, logged_interface, login_redirect, account_select, extrato_view, withdrawal_form


# @patch('builtins.input', return_value='teste')
# def test_minha_funcao(mock_input):
#     resultado = minha_funcao()
#     assert resultado == "Você digitou: teste"


# @patch('builtins.input', side_effect=['primeiro', 'segundo'])
# def test_minha_funcao(mock_input):
#     resultado1 = minha_funcao()
#     assert resultado1 == "Você digitou: primeiro"

#     resultado2 = minha_funcao()
#     assert resultado2 == "Você digitou: segundo"


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
    'joao maria silva santos'
    '12345678921',
    'user@email.com',
    '20/01/1995',
    'rua m, 123, centro  ',
    75991235393,
    1234,
    1234,

    ' joao   maria silva santos',
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
    resultado1 = new_user_form()
    assert resultado1 == {
        "user": 'JOAO MARIA SILVA SANTOS',
        "cpf": '12345678921',
        "email": 'user@email.com',
        "birth_date": '20/01/1995',
        "address": 'RUA M, 123, CENTRO',
        "contact_number": '75991235393',
        "password": '1234',
        "password_conf": '1234'
    }

    resultado2 = new_user_form()
    assert resultado2 == {
        "user": 'JOAO MARIA SILVA SANTOS',
        "cpf": '12345678921',
        "email": 'user@email.com',
        "birth_date": '20/01/1995',
        "address": 'RUA M, 123, CENTRO',
        "contact_number": '75991235393',
        "password": '1234',
        "password_conf": '1234'
    }

    resultado3 = new_user_form()
    assert resultado3 == {
        "user": 'JOAO MARIA SILVA SANTOS',
        "cpf": '12345678921',
        "email": 'user@email.com',
        "birth_date": '20/01/1995',
        "address": 'RUA M, 123, CENTRO',
        "contact_number": '75991235393',
        "password": '1234',
        "password_conf": '1234'
    }
