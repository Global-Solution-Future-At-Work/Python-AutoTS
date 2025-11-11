def logo_app():
    """
    Logo do Aplicativo.
    """
    bar_size = 37
    print("-"*bar_size)
    print("""
                _     _______ _____ 
     /\        | |   |__   __/ ____|
    /  \  _   _| |_ ___ | | | (___  
   / /\ \| | | | __/ _ \| |  \___ \ 
  / ____ \ |_| | || (_) | |  ____) |
 /_/    \_\__,_|\__\___/|_| |_____/ 
                                    
                Bem-vindo!               
          """)
    print("-"*bar_size)
    print()

def input_program():
    try:
        return int(input("Selecione qual opção você deseja usar: "))
    except ValueError:
        return None

def cls_terminal():
    """
    Limpa o terminal para melhorar a visualização do usuário.
    """
    for i in range(50):
        print()

def options_main_menu():
    """
    Menu com opções disponiveis no programa.
    """
    print("1 - Gerenciar Candidatos.")
    #Ver resumos
    #Definir empresa
    #Definir processo seletivo
    #Usar IA
    #Ver Historico da IA
    #Exportar Arquivo resumido de resultados que eu quiser da opção de cima
    print("0 - Fechar aplicativo.")

def options_candidatos_menu():
    """
    Menu com opções para gerenciar candidatos.
    """
    print("1 - Ver lista de candidatos registrados.")
    print("2 - Ver candidado detalhado por ID")
    print("3 - Registrar um candidato.")
    print("4 - Atualizar um candidato.")
    print("5 - Deletar um candidato.")
    print("0 - Voltar ao menu principal.")