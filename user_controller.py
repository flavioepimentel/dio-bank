import json
import datetime
from connection import write_operation, deserialize
from account_controller import account_creation


def access_validation(cpf: str, email: str, password: str) -> bool:
    data: list = deserialize(USER_DATA)
    if password in data and (cpf in data or email in data):
        return True
    else:
        return False


def new_user_validation(user, cpf, email) -> bool:
    data: list = deserialize(USER_DATA)
    if user in data and cpf in data and email in data:
        return True
    else:
        return False


def user_create(user, cpf, email, birth_date, address, contact_number, password) -> None:
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


def user_create(user, cpf, email, birth_date, address, contact_number, password) -> None:
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
        "": "",
        "password": password,
    }, USER_DATA)
