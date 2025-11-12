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
                                    
  O seu amigo, para todas as vagas!               
          """)
    print("-"*bar_size)
    print()

def input_int_program(text):
    try:
        value = int(input(text))
        return value
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
    print("2 - Gerenciar Parâmetros de Vaga.")
    print("3 - Processo de análise de vagas para candidatos (AI).")
    #Ver Historico da IA
    print("0 - Fechar aplicativo.")

def options_candidatos_menu():
    """
    Menu com opções para gerenciar candidatos.
    """
    print("1 - Ver lista de candidatos registrados.")
    print("2 - Ver candidado detalhado por ID.")
    print("3 - Registrar um candidato.")
    print("4 - Atualizar um candidato.")
    print("5 - Deletar um candidato.")
    print("0 - Voltar ao menu principal.")

def options_empresa_vagas_menu():
    print("1 - Ler Dados e Ramos Empresariais.")
    print("2 - Definir Dados e Ramos Empresariais.")
    print("3 - Ver Padrões de Vaga em aberto.")
    print("4 - Criar Padrão de Vaga.")
    print("5 - Atualizar Padrão de Vaga.")
    print("6 - Deletar Padrão de Vaga.")
    print("0 - Voltar ao menu Principal. ")