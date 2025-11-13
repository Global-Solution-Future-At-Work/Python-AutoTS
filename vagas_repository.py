import os
import json

_filename = "data/vagas.json"

def verify_vagas_file():
    """
    Verifica se o JSON de vagas está criado para funcionamento do aplicativo.
    """
    if not os.path.exists(_filename):
        with open(_filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)

def read_vagas() -> list:
    """
    Traz todos as vagas registrados no sistema.
    """
    with open(_filename, "r", encoding="utf-8") as f:
        return json.load(f)

def read_vagas_by_id(id: int) -> dict | int:    
    """
    Traz a vaga respectiva pelo ID informado.
    """
    with open(_filename, "r", encoding="utf-8") as f:
        for i in json.load(f):
            if i["id"] == id:
                return i 
        return -1
    
def create_vagas(id: int, descricao: str, qtnd: int):
    """
    Cria uma entrada de vaga dentro do arquivo JSON.
    """
    data = read_vagas()
    data.append({
        "id": id,
        "descricao_requisitos": descricao,
        "quantidade_vagas": qtnd
    })
    with open(_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return 1

def delete_vagas(id: int) -> int:
    """
    Deleta a entrada de uma vaga ao receber o seu respectivo ID.
    Caso o ID seja inexistente ou inválido, retorna -1
    """
    data = read_vagas()
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

def update_candidatos(
        id: int, 
        descricao: str = None,
        qtnd: int = None
        ) -> int:
    """
    Atualiza o registro de uma vaga registrado no sistema.
    Caso o ID seja inexistente ou inválido, retorna -1
    """
    data = read_vagas()
    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i]["descricao_requisitos"] = descricao if descricao != None else data[i]["descricao_requisitos"]
            data[i]["quantidade_vagas"] = qtnd if qtnd != None else data[i]["quantidade_vagas"]
            with open(_filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return 1
    return -1
