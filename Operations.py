
"""
Funções relacionadas a operações bancárias.
"""
import json
import datetime


def read_operation() -> str:
    """
    Realiza a tentativa de ler o arquivo e se não encontrado cria o arquivo com uma lista vazia
    """
    try:
        with open("OperationData.json", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "[]"


def deserialize_bank_statement() -> list:
    """
    Realiza a desserialização do arquivo json com os dados do extrato de string para objeto/dicionário (dict) do Python
    caso o arquivo seja encontrado em branco, ele devolve uma lista vazia para inicio dos registros do extrato.
    """
    if read_operation() != '':
        return json.loads(read_operation())
    else:
        return []


def write_operation(json_string) -> None:
    """
    Se existir o arquivo ele escreve um texto novo e se não existir cria e escreve o arquivo
    """
    historical_loads: list = deserialize_bank_statement()
    historical_loads.append(json_string)
    historical_dumps: str = json.dumps(historical_loads, default=str)
    with open("OperationData.json", "w") as file:
        file.write(historical_dumps)


# "2024-09-02 23:00:44.480308"

def deposit_operation(value) -> None:
    """
    Realiza a operação de soma na variável global SALDO_SESSION e a escrita da operação no extrato
    """
    global SALDO_SESSION
    SALDO_SESSION += value
    write_operation({
        "timestamp": datetime.datetime.now(),
        "operation": "Deposito",
        "value": value,
        "city": "New York"
    })


def withdrawal_operation(value) -> None:
    """
    Realiza a operação de subtração na variável global SALDO_SESSION e a escrita da operação no extrato
    """
    global SALDO_SESSION
    SALDO_SESSION -= value
    write_operation({
        "timestamp": datetime.datetime.now(),
        "operation": "Saque",
        "value": value,
        "city": "New York"
    })


def load_bank_balance():
    bank_statement: object | list = deserialize_bank_statement()
    saldo: float = 0.0

    for i, v in enumerate(bank_statement):

        if bank_statement[i]["operation"] == "Deposito":
            saldo += float(bank_statement[i]["value"])

        elif bank_statement[i]["operation"] == "Saque":
            saldo -= float(bank_statement[i]["value"])

    return saldo


def count_withdrawal_by_date():
    bank_statement: object | list = deserialize_bank_statement()
    withdrawal = 0
    for i, v in enumerate(bank_statement):
        if (bank_statement[i]["operation"] == "Saque") and (
                datetime.datetime.strptime(bank_statement[i]["timestamp"], "%Y-%m-%d %H:%M:%S.%f").day == datetime.datetime.now().day):
            withdrawal += 1
    return withdrawal
