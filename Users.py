"""
Funções relacionadas a usuarios.
"""

import json
import datetime


def read_operation() -> str:
    """
    Realiza a tentativa de ler o arquivo e se não encontrado cria o arquivo com uma lista vazia
    """
    try:
        with open("UserData.json", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "[]"


def deserialize() -> list:
    """
    Realiza a desserialização do arquivo json com os dados do extrato de string para objeto/dicionário (dict) do Python
    caso o arquivo seja encontrado em branco, ele devolve uma lista vazia para inicio dos registros do extrato.
    """
    if read_operation() != '':
        return json.loads(read_operation())
    else:
        return []


def write_operation(json_string) -> None:
    """
    Se existir o arquivo ele escreve um texto novo e se não existir cria e escreve o arquivo
    """
    historical_loads: list = deserialize()
    historical_loads.append(json_string)
    historical_dumps: str = json.dumps(historical_loads, default=str)
    with open("UserData.json", "w") as file:
        file.write(historical_dumps)


def register_operation(cpf) -> None:
    """

    """
    write_operation({
        "timestamp": datetime.datetime.now(),
        "fullname": "Deposito",
        "cpf": cpf,
        "birth_date": ""
    })
