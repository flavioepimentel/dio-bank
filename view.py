"""
Interfaces de tela de console
"""


def unlogged_interface():
    """
    Apresenta o primeiro formulário para a primeira tela
    """
    return input("""
                 DIO BANK

[n] Nova Conta
[l] Login
[q] Sair

=> """).lower().strip()


def new_user_form() -> dict:
    print("""\n\n\n\n\n\n
                PREENCHA O FORMULÁRIO PARA CADASTRO
          \n\n\n""")

    user = str(input("Nome completo: ")).upper().strip()

    # capturar apenas os números, validar se já existe, validar se possui 11 dígitos
    cpf = str(input("CPF: ")).replace('.', '').replace('-', '').strip()

    email = str(input("E-mail: ")).lower().replace(' ', '')

    # válidar se >= 16 anos e <= 150 anos
    print('"Data de Nascimento: ')
    birth_date = str(input("Exemplo -> 20/01/1995: ")).strip()

    address = str(input("Endereço: ")).upper().strip()

    contact_number = str(input("Número para contato: ")).strip().replace(
        '-', '').replace('(', '').replace(')', '').replace(' ', '')

    password = str(input("Senha: ")).strip().replace(' ', '')
    password_conf = str(input("Confirme a sua senha: ")
                        ).strip().replace(' ', '')
    # objeto com dados nova da conta
    return {
        "user": user,
        "cpf": cpf,
        "email": email,
        "birth_date": birth_date,
        "address": address,
        "contact_number": contact_number,
        "password": password,
        "password_conf": password_conf
    }


def login_form() -> dict:
    # verificar se está cadastrado
    access = str(input("""\n\n\n\n\n\n
                       
                       SEJA BEM VINDO AO BANCO DIO
                       


Para iniciar a sessão informe:

                           
CPF (apenas números) ou E-mail: """)).lower().replace('-', '').replace(' ', '')
    password = str(input("Senha: ")).replace(
        ' ', '')  # verificar se corresponde
    return {"cpf": access, "email": access, "password": password}


def account_select(accounts: list[int]) -> int:
    prompt = '''\n\n\n\n\n\n
Selecione a conta que você deseja realizar o login: \n    

'''
    for i, value in enumerate(accounts):
        prompt += f' [{i + 1}] - Número da Conta: {value}'
    acc = accounts[int(input("Informe um número: ")) - 1]
    return acc


def login_redirect():
    return input("""\n\n\n\n\n\n
                
Encontramos um usuário com esse acesso, gostaria de
prosseguir e criar uma segunda conta bancaria?

                 
[s] Sim
[n] Não

                 
==>""").lower().strip()


def logged_interface(balance):
    return input(f"""\n\n\n\n\n\n
                DIO BANK

Saldo: {balance}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """).lower().strip()


def extrato_view(extrato: list, balance: float) -> None:
    """
    Organiza dados para apresentar no console como tela
    """
    if extrato == []:
        print("\n================ EXTRATO ================\n")
        print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")
    else:
        historico = ""
        for i, v in enumerate(extrato):
            historico += f'{extrato[i]["operation"]
                            } - R$ {extrato[i]["value"]:.2f}\n'
        print("\n================ EXTRATO ================\n")
        print(historico)
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")


# def withdrawal_form() -> float:
#     return float(str(input("Informe o valor do saque: ")).replace(',', '.'))

def withdrawal_form():
    user_input = str(input("Informe o valor do saque: "))
    try:
        value = float(user_input.replace(',', '.'))
        if value <= 0:
            raise ValueError("Valor inválido, deve ser maior que zero.")
        return value
    except ValueError:
        raise ValueError("Entrada inválida, não é um número válido.")
