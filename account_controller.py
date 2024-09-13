
import json
import datetime
from main import SALDO_SESSION, LIMITE_VALOR_SAQUE, CONTAGEM_SAQUES_DIA, LIMITE_NUMERO_SAQUES
from connection import write_operation, deserialize, OPERATION_DATA
from user_controller import access_validation, new_user_validation


def account_validation():
    pass


def account_creation(user, cpf, email, birth_date, address, contact_number, password):
    if new_user_validation(user, cpf, email):
        pass
    elif access_validation(cpf, email, password):
        pass
    return write_operation({})


def saque_validation(valor_saque: float, saldo: float) -> None:
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > LIMITE_VALOR_SAQUE
    excedeu_saques = CONTAGEM_SAQUES_DIA >= LIMITE_NUMERO_SAQUES
    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("""\nOperação falhou! Você excedeu o número máximo de saques diários. 
Tente novamente amanhã.""")
        print("Saques realizados: ", CONTAGEM_SAQUES_DIA)

    elif valor_saque > 0:
        withdrawal_operation(valor_saque)
    else:
        print("\nOperação falhou! O valor informado é inválido.")


# "2024-09-02 23:00:44.480308"
def deposit_operation(value: float) -> None:
    """
    Realiza a operação de soma na variável global SALDO_SESSION 
    e a escrita da operação no extrato
    """
    global SALDO_SESSION, OPERATION_DATA
    SALDO_SESSION += value
    write_operation({
        "timestamp": datetime.datetime.now(),
        "operation": "Deposito",
        "value": value,
        "city": "New York"
    }, OPERATION_DATA)


def withdrawal_operation(value: float) -> None:
    """
    Realiza a operação de subtração na variável global SALDO_SESSION e 
    a escrita da operação no extrato
    """
    global SALDO_SESSION, OPERATION_DATA
    SALDO_SESSION -= value
    write_operation({
        "timestamp": datetime.datetime.now(),
        "operation": "Saque",
        "value": value,
        "city": "New York"
    }, OPERATION_DATA)


def load_bank_balance() -> float:
    """
    Calcula o saldo com base no extrato da conta
    """
    bank_statement: object | list = deserialize()
    saldo: float = 0.0

    for i, v in enumerate(bank_statement):

        if bank_statement[i]["operation"] == "Deposito":
            saldo += float(bank_statement[i]["value"])

        elif bank_statement[i]["operation"] == "Saque":
            saldo -= float(bank_statement[i]["value"])

    return saldo


def count_withdrawal_by_date() -> int:
    """
    Realiza a contagem de saques realizados na data atual
    """
    bank_statement: object | list = deserialize()
    withdrawal: int = 0
    for i, v in enumerate(bank_statement):
        if (bank_statement[i]["operation"] == "Saque") and (
                datetime.datetime.strptime(bank_statement[i]["timestamp"],
                                           "%Y-%m-%d %H:%M:%S.%f").day == datetime.datetime.now().day):
            withdrawal += 1
    return withdrawal
