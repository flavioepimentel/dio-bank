
import json
import datetime
from connection import write_operation, deserialize


def generate_new_account_number() -> int:
    """
    Busca a última conta registrada e devolve um valor 
    válido de número de conta
    """
    global ACCOUNT_DATA
    data: list = deserialize(ACCOUNT_DATA)
    last_account: int = 0
    for indicie, valor in enumerate(data):
        if valor["account_number"] > last_account:
            last_account = valor["account_number"]
    return last_account + 1


def account_create(user: str, cpf: str, email: str) -> None:
    account_number: int = generate_new_account_number()
    write_operation({
        "timestamp": datetime.datetime.now(),
        "user": user,
        "cpf": cpf,
        "email": email,
        "account_number": account_number,
        "agencie_number": "0001",
        "balance": 0.0
    })


def withdrawal_validation(withdrawal_value: float, balance: float, limite_valor_saque: float, contagem_saques_dia: int, limite_numero_saques: int) -> bool:
    excedeu_saldo = withdrawal_value > balance
    excedeu_limite = withdrawal_value > limite_valor_saque
    excedeu_saques = contagem_saques_dia >= limite_numero_saques
    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
        return False
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
        return False
    elif excedeu_saques:
        print("""\nOperação falhou! Você excedeu o número máximo de saques diários. 
Tente novamente amanhã.""")
        print("Saques realizados: ", contagem_saques_dia)
        return False
    elif withdrawal_value > 0:
        return True
    else:
        print("\nOperação falhou! O valor informado é inválido.")
        return False


# "2024-09-02 23:00:44.480308"
def deposit_operation(*, value: float, account_number: int, cpf: str, email: str, operation_data, limite_valor_saque: float, contagem_saques_dia: int, limite_numero_saques: int) -> None:
    """
    Realiza a operação de soma na variável global SALDO_SESSION 
    e a escrita da operação no extrato
    """
    write_operation({
        "timestamp": datetime.datetime.now(),
        "cpf:": cpf,
        "email": email,
        "account_number": account_number,
        "operation": "Deposito",
        "value": value,
        "location": "New York"
    }, operation_data, limite_valor_saque, contagem_saques_dia,
    limite_numero_saques)


def withdrawal_operation(*, withdrawal_value: float, balance,
                         account_number, cpf, email) -> None:
    """
    Realiza a operação de subtração na variável global SALDO_SESSION e 
    a escrita da operação no extrato
    """
    global SALDO_SESSION, OPERATION_DATA
    SALDO_SESSION -= withdrawal_value
    if withdrawal_validation(withdrawal_value, balance):
        write_operation({
            "timestamp": datetime.datetime.now(),
            "cpf:": cpf,
            "email": email,
            "account_number": account_number,
            "operation": "Saque",
            "value": withdrawal_value,
            "location": "New York"
        }, OPERATION_DATA)


def load_bank_balance(cpf: str, account_number, bank_statement) -> float:
    """
    Carrega saldo do usuário, calculando o saldo com base no extrato da conta
    """
    bank_statement = [i for i in bank_statement if i["cpf:"]
                      == cpf and i["account_number"] == account_number]

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
