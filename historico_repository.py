import os
import json

_filename = "historico_resultados.json"

def verify_historico_file():
    """
    Verifica se o JSON do historico está criado para funcionamento do aplicativo.
    """
    if not os.path.exists(_filename):
        with open(_filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)

def read_historico() -> dict:
    """
    Traz o dicionário contendo as informações da empresa.
    """
    with open(_filename, "r", encoding="utf-8") as f:
        return json.load(f)

def read_historico_by_id(id: int) -> dict | int:    
    """
    Traz o histórico respectiva pelo ID informado.
    """
    with open(_filename, "r", encoding="utf-8") as f:
        for i in json.load(f):
            if i["id"] == id:
                return i 
        return -1
   
def create_historico(resultado: dict) -> int:
    """
    Cria o resultado da análise para avaliação do usuário.
    """
    data = read_historico()
    data.append(resultado)
    with open(_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return 1

def delete_historico(id: int) -> int:
    """
    Deleta a entrada de um histórico anterior ao receber o seu respectivo ID.
    Caso o ID seja inexistente ou inválido, retorna -1
    """
    data = read_historico()
    index = None
    for i in range(len(data)):
        if id == data[i]["id"]:
            index = i
            break
    if index != None:
        data.pop(index)
        with open(_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return 1
    return -1