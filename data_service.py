import os

def verify_data_dir():
    """
    Verifica se a pasta data do sistema está criado para funcionamento do aplicativo.
    """
    os.makedirs("data", exist_ok=True)
