"""
    DIO BANK É UMA APLICAÇÃO QUE TEM O OBJETIVO DE DEMONSTRAR OPERAÇÕES BÁSICAS DE UM APP DE BANCO
"""
from Operations import (
    deposit_operation,
    load_bank_balance,
    count_withdrawal_by_date,
    withdrawal_operation,
    deserialize_bank_statement
)

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
