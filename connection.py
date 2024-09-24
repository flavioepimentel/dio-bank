"""
Esse arquivo hospeda fuções básicas e reaproveitaveis para as models, essas funções garantem a 
conexão com os respectivos arquivo .json que estão funcionando como base de dados do protótipo.
"""
import json

USER_DATA = 'UserData.json'
ACCOUNT_DATA = 'AccountData.json'
OPERATION_DATA = 'OperationData.json'


def read_operation(name_file_json: str):
    """
    Realiza a tentativa de ler o arquivo e se não encontrado cria o arquivo com uma lista vazia
    """
    try:
        with open(name_file_json, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "[]"


def deserialize(name_file_json: str) -> list:
    """
    Realiza a desserialização do arquivo json com os dados do extrato de string para objeto/dicionário 
    (dict) do Python caso o arquivo seja encontrado em branco, ele devolve uma lista vazia para inicio 
    dos registros do extrato.
    """
    if read_operation(name_file_json) != '':
        return json.loads(read_operation(name_file_json))
    return []


def write_operation(json_string: object, name_file_json: str) -> None:
    """
    Se existir o arquivo ele escreve um texto novo e se não existir cria e escreve o arquivo.
    """
    historical_loads: list = deserialize(name_file_json)
    historical_loads.append(json_string)
    historical_dumps: str = json.dumps(historical_loads, default=str)
    with open(name_file_json, "w") as file:
        file.write(historical_dumps)
