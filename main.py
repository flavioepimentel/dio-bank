"""
    DIO BANK É UMA APLICAÇÃO QUE TEM O OBJETIVO DE DEMONSTRAR OPERAÇÕES BÁSICAS DE UM APP DE BANCO
"""
from connection import OPERATION_DATA, ACCOUNT_DATA, USER_DATA
from account_controller import deposit_operation, load_bank_balance, deserialize, withdrawal_operation, account_create
from user_controller import new_user_validation, user_create, password_validation, access_validation, check_account_number, load_user
from view import new_user_form, unlogged_interface, logged_interface, login_form, extrato_view, withdrawal_form, login_redirect, account_select


STATUS_SESSION = []


def logged_main(user_session: dict, /,  account_number: int) -> str:
    """
    'Main' lógica acessada após confirmado o login
    """
    bank_statement: list = deserialize(OPERATION_DATA)

    balance = load_bank_balance(
        user_session['cpf'], account_number, bank_statement)

    opcao = logged_interface(balance)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            deposit_operation(value=valor, account_number=account_number,
                              cpf=user_session['cpf'], email=user_session['email'], name_file_json=OPERATION_DATA)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        # Carrega informações da conta
        withdrawal_value = withdrawal_form()
        withdrawal_operation(withdrawal_value=withdrawal_value, account_number=account_number,
                             cpf=user_session['cpf'], email=user_session['email'], name_file_json=OPERATION_DATA)

    elif opcao == "e":
        bank_statement: list = deserialize(OPERATION_DATA)
        balance = load_bank_balance(
            user_session['cpf'], account_number, bank_statement)
        extrato_view(bank_statement, balance)
    elif opcao == "q":
        return 'break'

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


def unlogged_main():
    """
    'Main' lógica acessada no inicio sem uma conta/seção iniciada
    """
    opcao = unlogged_interface()
    if opcao == 'n':
        user_object = new_user_form()

        if (
            new_user_validation(
                user_object["cpf"], user_object["email"], USER_DATA)
            and password_validation(user_object["password"], user_object["password_conf"])
        ):

            """
            Se usuário não existe e se as duas senhas estão iguais 

            """

            user_create(
                user_object["user"], user_object["cpf"], user_object["email"],
                user_object["contact_number"], user_object["password"],
                user_object["birth_date"], user_object["address"], USER_DATA)

            account_create(user_object["user"],
                           user_object["cpf"], user_object["email"], ACCOUNT_DATA)

            form_data = login_form()

            if access_validation(
                    form_data["cpf"], form_data["email"],
                    form_data["password"], USER_DATA):

                user_session = load_user(
                    form_data["cpf"], ACCOUNT_DATA, USER_DATA)

                account_number = check_account_number(
                    user_session['accounts'], account_select)

                logged_main(user_session[0], account_number)

        elif (
            not new_user_validation(
                user_object["cpf"], user_object["email"], USER_DATA)
            and password_validation(user_object["password"], user_object["password_conf"])
        ):

            """
                Se usuário existe ele é redirecionado a validação 
                da criação de uma conta após o login.

            """

            if login_redirect() == "s":
                """
                Confirma que quer criar uma nova conta para um usuário existente

                """

                form_data = login_form()

                if access_validation(
                        form_data["cpf"], form_data["email"], form_data["password"], USER_DATA):

                    user_session = load_user(
                        form_data["cpf"], ACCOUNT_DATA, USER_DATA)

                    account_create(user_session[0]['user'], user_object['cpf'],
                                   user_object['email'], ACCOUNT_DATA)

                    account_number = check_account_number(
                        user_session[0]['accounts'], account_select)
                    if STATUS_SESSION == []:
                        STATUS_SESSION.append(user_session[0])

                    logged_main(user_session[0], account_number)

            elif login_redirect == 'n':
                """
                Recusa criar uma nova conta para um usuário existente

                """

                form_data = login_form()

                if access_validation(
                        form_data["cpf"], form_data["email"], form_data["password"], USER_DATA):

                    user_session = load_user(
                        form_data["cpf"], ACCOUNT_DATA, USER_DATA)

                    account_number = check_account_number(
                        user_session[0]['accounts'], account_select)

                    if STATUS_SESSION == []:
                        STATUS_SESSION.append(user_session[0])

                    logged_main(user_session[0], account_number)

    elif opcao == "l":
        """
        Opção e login direto, será realizada a autenticação padrão de conta.

        """

        form_data = login_form()

        if access_validation(
                form_data["cpf"], form_data["email"], form_data["password"], USER_DATA):

            user_session = load_user(
                form_data["cpf"], ACCOUNT_DATA, USER_DATA)
            account_number = check_account_number(
                user_session[0]['accounts'], account_select)

            if STATUS_SESSION == []:
                STATUS_SESSION.append(user_session[0])

            logged_main(user_session[0], account_number)

    elif opcao == "q":

        return 'break'


if __name__ == '__main__':
    while True:
        if STATUS_SESSION == []:
            if unlogged_main() == 'break':
                break
        elif STATUS_SESSION != []:
            print(STATUS_SESSION)
            if logged_main(STATUS_SESSION[0], STATUS_SESSION[0]["accounts"][0]['account_number']) == 'break':
                break
        else:
            STATUS_SESSION = []
            if unlogged_main() == 'break':
                break
