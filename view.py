"""
Interfaces de tela de console
"""


def beggin_interface():
    """
    Apresenta o primeiro formulário para a primeira tela
    """
    return input("""
                 DIO BANK

[n] Nova Conta
[l] Login
[q] Sair

=> """)


def logged_interface(saldo):
    return input(f"""
                DIO BANK

Saldo: {saldo}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """)


def extrato_view(extrato, saldo):
    """
    Organiza dados para apresentar no console como tela
    """
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


def new_user_form():
    user = str(input("Nome completo: "))
    # capturar apenas os números, validar se já existe, validar se possui 11 dígitos
    cpf = str(input("CPF: "))
    email = str(input("E-mail: "))
    # válidar se >= 16 anos e <= 150 anos
    birth_date = str(input("Data de Nascimento: "))
    address = str(input("Endereço: "))
    contact_number = str(input("Número para contato: "))
    password = str(input("Senha: "))
    password_conf = str(input("Confirme a sua senha: "))
    # objeto com dados nova da conta
    return (
        user,
        cpf,
        email,
        birth_date,
        address,
        contact_number,
        password,
        password_conf
    )


def login_form():
    cpf = str(input("Nome completo: "))  # verificar se está cadastrado
    password = str(input("Senha: "))  # verificar se corresponde
    return (cpf, password)


def saque_form() -> float:
    return float(input("Informe o valor do saque: "))
