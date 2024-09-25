import json
import datetime
from connection import write_operation, deserialize


def access_validation(cpf: str, email: str, password: str, user_data: str) -> bool:
    """
    Retorna um valor booleano para a verificação da existencia das 
    primary key e password
    """
    user_data: list = deserialize(user_data)
    for i, v in enumerate(user_data):
        if (password in user_data[i]["password"]):
            print("senha ok")

            if ((
                cpf in user_data[i]["cpf"]
                or email in user_data[i]["email"]
            )
            ):
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


def load_user(cpf: str, account_data: str, user_data: str):
    user_data: list = deserialize(user_data)
    account_data: list = deserialize(account_data)
    user_data = [i for i in user_data if i['cpf'] == cpf]
    account_data = [i for i in account_data if i['cpf'] == cpf]
    user_data[0]['accounts'] = account_data
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
    for i, v in enumerate(data):
        if cpf not in data[i]["cpf"] and email not in data[i]["email"]:
            return True
    return False


def check_account_number(account_data: list, account_select):
    """
    Função checa a existência de mais de uma conta corrente utilizada
    pelo mesmo usuário.

    """
    print(account_data)
    if len(account_data) > 1:
        return account_select(account_data)
    elif account_data == []:
        return '''
        Error: No accounts found
        
        <!> Para corrigir finalize acesse nova conta e finalize o seu cadastro

        '''
    return account_data[0]['account_number']


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
