import menu
import candidatos_repository as cr

def candidatos_menu():
    cr.verify_candidatos_file()
    while True:
        pass


error_message_main_menu = ""
while True:
    menu.logo_app()
    print(error_message_main_menu)
    menu.options_main_menu()
    option = menu.input_program()
    match option:
        case 1:
            candidatos_menu()
        case 0:
            print("Saindo do programa...")
            break
        case _:
            error_message_main_menu = "Opção inválida... Escolha outra opção."
    menu.cls_terminal()


