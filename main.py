"""
    DIO BANK É UMA APLICA
"""

import json
import datetime


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


SALDO = 0
LIMITE_VALOR_SAQUE = 500
CONTAGEM_SAQUES_DIA = 0
LIMITE_NUMERO_SAQUES = 3


def write_operation(json_string) -> None:
    """
    Se existir o arquivo ele escreve um texto novo e se não existir cria e escreve o arquivo
    """
    with open("data.json", "w") as file:
        file.write(json_string)


def read_operation():
    """
    Realiza a tentativa de ler o arquivo e se não encontrado cria o arquivo com uma lista vazia
    """
    try:
        with open("data.json", "r") as file:
            return file.read()
    except FileNotFoundError:
        write_operation("[]")


def deposit_operation(value) -> None:
    global SALDO
    SALDO += value


def withdrawal_operation(value) -> None:
    global SALDO
    SALDO -= value


if __name__ == '__main__':
    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                extrato = read_operation()
                deposit_operation(valor)
                ct = datetime.datetime.now()

                data = {
                    "timestamp": ct,
                    "operation": "Deposito",
                    "value": valor,
                    "city": "New York"
                }

                write_operation(data)

                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > SALDO

            excedeu_limite = valor > LIMITE_VALOR_SAQUE

            excedeu_saques = CONTAGEM_SAQUES_DIA >= LIMITE_NUMERO_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                withdrawal_operation(valor)
                ct = datetime.datetime.now()

                data = {
                    "timestamp": ct,
                    "operation": "John",
                    "value": 30,
                    "city": "New York"
                }

                extrato += f"Saque: R$ {valor:.2f}\n"
                CONTAGEM_SAQUES_DIA += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {SALDO:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
