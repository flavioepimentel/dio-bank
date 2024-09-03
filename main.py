"""
    DIO BANK É UMA APLICAÇÃO QUE TEM O OBJETIVO DE DEMONSTRAR OPERAÇÕES BÁSICAS DE UM APP DE BANCO
"""

import json
import datetime


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


SALDO_SESSION: float = 0.0
LIMITE_VALOR_SAQUE: float = 500.0
CONTAGEM_SAQUES_DIA: int = 0
LIMITE_NUMERO_SAQUES: int = 3


def read_operation() -> str:
    """
    Realiza a tentativa de ler o arquivo e se não encontrado cria o arquivo com uma lista vazia
    """
    try:
        with open("data.json", "r") as file:
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
    with open("data.json", "w") as file:
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


if __name__ == '__main__':
    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                deposit_operation(valor)

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo = load_bank_balance()
            CONTAGEM_SAQUES_DIA = count_withdrawal_by_date()

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > LIMITE_VALOR_SAQUE

            excedeu_saques = CONTAGEM_SAQUES_DIA >= LIMITE_NUMERO_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print(
                    """\nOperação falhou! Você excedeu o número máximo de saques diários. 
Tente novamente amanhã.""")
                print("Saques realizados: ", CONTAGEM_SAQUES_DIA)

            elif valor > 0:
                withdrawal_operation(valor)

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            extrato = deserialize_bank_statement()
            saldo = load_bank_balance()
            if extrato == []:
                print("\n================ EXTRATO ================\n")
                print("Não foram realizadas movimentações.")
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("==========================================")
            else:
                historico = ""
                for i, v in enumerate(extrato):
                    historico += f'{extrato[i]["operation"]
                                    } - R$ {extrato[i]["value"]:.2f}\n'

                print("\n================ EXTRATO ================\n")

                print(historico)

                print(f"\nSaldo: R$ {saldo:.2f}")
                print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
