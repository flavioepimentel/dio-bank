"""
    DIO BANK É UMA APLICAÇÃO QUE TEM O OBJETIVO DE DEMONSTRAR OPERAÇÕES BÁSICAS DE UM APP DE BANCO
"""
from account_controller import (
    deposit_operation, load_bank_balance, count_withdrawal_by_date,
    withdrawal_operation, deserialize, saque_validation)
from view import new_user_form, beggin_interface, logged_interface, login_form, extrato_view, saque_form


SALDO_SESSION: float = 0.0
LIMITE_VALOR_SAQUE: float = 500.0
CONTAGEM_SAQUES_DIA: int = 0
LIMITE_NUMERO_SAQUES: int = 3


def logged_menu_cotroller() -> str:
    saldo = load_bank_balance()
    opcao = logged_interface(saldo)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            deposit_operation(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        global CONTAGEM_SAQUES_DIA
        # Carrega informações da conta
        saldo = load_bank_balance()
        CONTAGEM_SAQUES_DIA = count_withdrawal_by_date()
        valor_saque = saque_form()
        saque_validation(valor_saque, saldo)

    elif opcao == "e":
        extrato = deserialize()
        saldo = load_bank_balance()
        extrato_view(extrato, saldo)
    elif opcao == "q":
        return 'break'

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


def home_controller():
    opcao = beggin_interface()
    if opcao == 'n':
        return new_user_form()
    elif opcao == "l":
        return login_form()  # objeto com dados da conta existente
    elif opcao == "q":
        return 'break'


if __name__ == '__main__':
    while True:
        pass
