import json
import datetime


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3


def write_operation(json_string):
    with open("data.json", "w") as file:
        file.write(json_string)


def read_operation(json_string):
    with open("data.json", "r") as file:
        file.read(json_string)


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            ct = datetime.datetime.now()

            data = {
                "timestamp": ct,
                "operation": "John",
                "value": 30,
                "city": "New York"
            }

            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            ct = datetime.datetime.now()

            data = {
                "timestamp": ct,
                "operation": "John",
                "value": 30,
                "city": "New York"
            }

            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
