import datetime
from connection import write_operation, deserialize


LIMITE_VALOR_SAQUE: float = 500.0
LIMITE_NUMERO_SAQUES: int = 3


def generate_new_account_number(name_file_json: str) -> int:
    """
    Busca a última conta registrada e devolve um valor 
    válido de número de conta
    """
    data: list = deserialize(name_file_json)
    last_account: int = 0
    for indicie, valor in enumerate(data):
        if valor["account_number"] > last_account:
            last_account = valor["account_number"]
    return last_account + 1


def account_create(user: str, cpf: str, email: str, name_file_json: str) -> None:
    account_number: int = generate_new_account_number(name_file_json)
    write_operation({
        "timestamp": datetime.datetime.now(),
        "user": user,
        "cpf": cpf,
        "email": email,
        "account_number": account_number,
        "agencie_number": "0001",
        "balance": 0.0
    }, name_file_json)


def withdrawal_validation(withdrawal_value: float, balance: float, contagem_saques_dia: int) -> bool:

    if withdrawal_value > balance:
        print("\nOperação falhou! Você não tem saldo suficiente.")
        return False
    elif withdrawal_value > LIMITE_VALOR_SAQUE:
        print("\nOperação falhou! O valor do saque excede o limite.")
        return False
    elif contagem_saques_dia >= LIMITE_NUMERO_SAQUES:
        print("""\n
              
Operação falhou! Você excedeu o número máximo de saques diários.
               
Tente novamente amanhã.
              
              """)
        print("Saques realizados: ", contagem_saques_dia)
        return False
    elif withdrawal_value > 0:
        return True
    else:
        print("\nOperação falhou! O valor informado é inválido.")
        return False


# "2024-09-02 23:00:44.480308"
def deposit_operation(*, value: float, account_number: int, cpf: str, email: str, name_file_json: str) -> None:
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
    }, name_file_json)


def withdrawal_operation(*, withdrawal_value: float, account_number: int, cpf: str, email: str, name_file_json: str) -> None:
    """
    Realiza a operação de subtração na variável global SALDO_SESSION e 
    a escrita da operação no extrato
    """
    bank_statement: list = deserialize(name_file_json)
    if withdrawal_validation(
        withdrawal_value,
        balance=load_bank_balance(cpf, account_number, bank_statement), contagem_saques_dia=count_withdrawal_by_date(bank_statement)
    ):
        write_operation({
            "timestamp": datetime.datetime.now(),
            "cpf:": cpf,
            "email": email,
            "account_number": account_number,
            "operation": "Saque",
            "value": withdrawal_value,
            "location": "New York"
        }, name_file_json)


def load_bank_balance(cpf: str, account_number: int, bank_statement: list) -> float:
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


def count_withdrawal_by_date(bank_statement) -> int:
    """
    Realiza a contagem de saques realizados na data atual
    """
    withdrawal: int = 0
    for i, v in enumerate(bank_statement):
        if (bank_statement[i]["operation"] == "Saque") and (
                datetime.datetime.strptime(bank_statement[i]["timestamp"],
                                           "%Y-%m-%d %H:%M:%S.%f").day == datetime.datetime.now().day):
            withdrawal += 1
    return withdrawal
