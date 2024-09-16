import json
import datetime
from connection import write_operation, deserialize


def access_validation(cpf: str, email: str, password: str, *user_data) -> bool:
    """
    Retorna um valor booleano para a verificação da existencia das 
    primary key e password
    """
    user_data: list = deserialize(user_data)
    if password in user_data and (cpf in user_data or email in user_data):
        return True
    return False


def password_validation(password: str, password_conf: str):
    if password == password_conf:
        return True
    return False


def cpf_validation(cpf: str) -> bool:
    if len(cpf) == 11:
        return True
    return False


def load_user(cpf, ACCOUNT_DATA, USER_DATA):
    user_data: list = deserialize(USER_DATA)
    account_data: list = deserialize(ACCOUNT_DATA)
    user_data = [i for i in user_data if i['cpf'] == cpf]
    account_data = [i for i in account_data if i['cpf'] == cpf]
    user_data['accounts'] = account_data
    return user_data


def birthday_validation(birth_date: str) -> bool:
    try:
        date = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
        return age_validation(date)
    except ValueError:
        print('Data de nascimento está em um formato fora do padrão.')
        return False


def age_validation(birth_date: datetime) -> bool:
    if datetime.datetime.now() - birth_date > datetime.timedelta(days=(16*365)):
        return True
    print('Usuário possui menos de 16 anos.')
    return False


def new_user_validation(cpf: str, email: str, user_data: str) -> bool:
    """
    Retorna um valor booleano para a verificação de novo usuário, 
    se as chaves primárias existirem, não é um novo usuário (false)
    """
    data: list = deserialize(user_data)
    if cpf not in data and email not in data:
        return True
    return False


def check_account_number(account_data, account_select):
    """
    Função checa a existência de mais de uma conta corrente utilizada
    pelo mesmo usuário.

    """
    if len(account_data) > 1:
        return account_select(account_data)
    return account_data['account_number']


def user_create(user: str, cpf: str, email: str, contact_number: str,
                password: str, birth_date: str, address: str, user_data) -> None:
    """
    Recebe dados para cadastro de novo usuário
    """
    if new_user_validation(cpf, email, user_data):
        write_operation({
            "timestamp": datetime.datetime.now(),
            "user": user,
            "cpf": cpf,
            "email": email,
            "contact_number": contact_number,
            "birth_date": birth_date,
            "address": address,
            "password": password,
        }, user_data)
