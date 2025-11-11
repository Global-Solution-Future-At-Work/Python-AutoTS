import os
import json

_filename = "candidatos.json"

def verify_candidatos_file():
    if not os.path.exists(_filename):
        with open(_filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)

def read_candidatos() -> list:
    with open(_filename, "r", encoding="utf-8") as f:
        return json.load(f)

def read_candidatos_by_id(id: int) -> dict | int:
    with open(_filename, "r", encoding="utf-8") as f:
        for i in json.load(f):
            if i["id"] == id:
                return i 
        return -1
     
def create_candidatos(
        id: int, 
        nome: str,
        foto: str,
        cargo: str,
        resumo: str,
        localizacao: str,
        area: str,
        habilidade_tecnicas: list[str],
        soft_skills: list[str],
        experiencias: list[dict],
        formacao: list[dict],
        projetos: list[dict],
        certificacoes: list[str],
        idiomas: list[dict],
        area_interesses: list[str]
        ) -> int:
    data = read_candidatos()
    data.append({
        "id": id,
        "nome": nome,
        "foto": foto,
        "cargo": cargo,
        "resumo": resumo,
        "localizacao": localizacao,
        "area": area,
        "habilidades_tecnicas": habilidade_tecnicas,
        "soft_skills": soft_skills,
        "experiencias": experiencias,
        "formacao": formacao,
        "projetos": projetos,
        "certificacoes": certificacoes,
        "idiomas": idiomas,
        "area_interesses": area_interesses
    })
    with open(_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return 1

def delete_candidatos(id: int) -> int:
    data = read_candidatos()
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
        nome: str = None,
        foto: str = None,
        cargo: str = None,
        resumo: str = None,
        localizacao: str = None,
        area: str = None,
        habilidade_tecnicas: list[str] = None,
        soft_skills: list[str] = None,
        experiencias: list[dict] = None,
        formacao: list[dict] = None,
        projetos: list[dict] = None,
        certificacoes: list[str] = None,
        idiomas: list[dict] = None,
        area_interesses: list[str] = None
        ) -> int:
    data = read_candidatos()
    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i]["nome"]                = nome                if nome != None                else data[i]["nome"]
            data[i]["foto"]                = foto                if foto != None                else data[i]["foto"]
            data[i]["cargo"]               = cargo               if cargo != None               else data[i]["cargo"]
            data[i]["resumo"]              = resumo              if resumo != None              else data[i]["resumo"]
            data[i]["localizacao"]         = localizacao         if localizacao != None         else data[i]["localizacao"]
            data[i]["area"]                = area                if area != None                else data[i]["area"]
            data[i]["habilidade_tecnicas"] = habilidade_tecnicas if habilidade_tecnicas != None else data[i]["habilidade_tecnicas"]
            data[i]["soft_skills"]         = soft_skills         if soft_skills != None         else data[i]["soft_skills"]
            data[i]["experiences"]         = experiencias        if experiencias != None        else data[i]["experiencias"]
            data[i]["formacao"]            = formacao            if formacao != None            else data[i]["formacao"]
            data[i]["projetos"]            = projetos            if projetos != None            else data[i]["projetos"]
            data[i]["certificacoes"]       = certificacoes       if certificacoes != None       else data[i]["certificacoes"]
            data[i]["idiomas"]             = idiomas             if idiomas != None             else data[i]["idiomas"]
            data[i]["area_interesses"]     = area_interesses     if area_interesses != None     else data[i]["soft_skills"]
            return 1
    return -1
