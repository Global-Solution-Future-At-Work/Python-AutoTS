import requests
import json
_api_key = "AIzaSyApDGEswD43RbCsJHfjjzylbabzwQuX7xM"

def send_gemini_process(
    empresa: dict,
    vaga: dict,
    candidatos: dict
) -> dict:
    """
    Faz uma requisição a API do Gemini (Google) para fazer o processamento
    de vaga dos candidatos cadastro na base de dados de acordo com a vaga
    requisitada no momento.
    """
    prompt = """
    Você ira análisar uma base de dados de candidatos registrados de um sistema e baseado nele, vai retornar os 
    IDs dos melhores candidato de forma imparcial de acordo com a quantidade de vagas que está em aberto.
    O seu objetivo é retorna um JSON em Português-Brasil, que segue a estrutura a seguir (podem estar em formato Dict do Python): 
    {"candidatos_selecionados": [...IDs dos candidatos em Integer], "resumo_analise": "...texto resumido da análise"}.
    Você vai receber três JSONs na seguinte ordem: EMPRESA, VAGA e CANDIDATOS. Logo após isso, faça a análise. 
    """
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
    data = {
        "system_instruction": {
            "parts": [
                {
                "text": prompt
                }
            ]
        },
        "contents": [
            {
                "parts": [
                    {
                        "text": f"EMPRESA: {empresa} ||| VAGA: {vaga} ||| CANDIDATOS: {candidatos}"
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0,
        }
    }
    headers = {
        "x-goog-api-key": _api_key,
        "Content-Type": "application/json"
    }
    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()["candidates"][0]["content"]["parts"][0]["text"].replace("```", "").replace("json", "")
    return json.loads(result)
