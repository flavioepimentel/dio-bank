import json
import datetime
from connection import write_operation, deserialize
from account_controller import account_creation


def access_validation(cpf: str, email: str, password: str) -> bool:
    """
    Retorna um valor booleano para a verificação da existencia das 
    primary key e password
    """
    data: list = deserialize(USER_DATA)
    if password in data and (cpf in data or email in data):
        return True
    else:
        return False


def new_user_validation(user, cpf, email) -> bool:
    """
    Retorna um valor booleano para a verificação da existencia das 
    primary key
    """
    data: list = deserialize(USER_DATA)
    if user in data and cpf in data and email in data:
        return True
    else:
        return False


def user_create(user, cpf, email, birth_date,
                address, contact_number, password) -> None:
    """
    Recebe dados para cadastro de novo usuário
    """
    global USER_DATA
    write_operation({
        "timestamp": datetime.datetime.now(),
        "user": user,
        "cpf": cpf,
        "email": email,
        "birth_date": birth_date,
        "address": address,
        "contact_number": contact_number,
        "password": password,
    }, USER_DATA)


def generate_new_account_number() -> int:
    """
    Busca a última conta registrada e devolve um valor 
    válido de número de conta
    """
    global ACCOUNT_DATA
    data: list = deserialize(ACCOUNT_DATA)
    last_account: int = 0
    for indicie, valor in enumerate(data):
        if valor["account_number"] > last_account:
            last_account = valor["account_number"]
    return last_account + 1


def user_create(user: str, cpf: str, email: str,
                password: str, account_number: str, agencie_number: str) -> None:
    """
    Recebe dados para cadastro de novo usuário
    """
    global USER_DATA
    write_operation({
        "timestamp": datetime.datetime.now(),
        "user": user,
        "cpf": cpf,
        "email": email,
        "account_number": account_number,
        "agencie_number": agencie_number,
        "password": password,
    }, USER_DATA)
