import os
import json

_filename = "data/empresa.json"

def verify_empresa_file():
    """
    Verifica se o JSON da empresa está criado para funcionamento do aplicativo.
    """
    if not os.path.exists(_filename):
        with open(_filename, "w", encoding="utf-8") as f:
            json.dump({
                "nome": None,
                "descricao": None
            }, f, ensure_ascii=False)

def read_empresa() -> dict:
    """
    Traz o dicionário contendo as informações da empresa.
    """
    with open(_filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
def create_empresa(nome: str, descricao: str) -> int:
    """
    Atualiza/Cria as informações da empresa para uso do sistema.
    """
    data = read_empresa()
    data["nome"] = nome
    data["descricao"] = descricao
    with open(_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return 1
