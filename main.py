import menu
import candidatos_repository as cr
import empresa_repository as er
import vagas_repository as vr

def candidatos_menu():
    """
    Interface de console no módulo de candidatos.
    """
    cr.verify_candidatos_file()
    while True:
        menu.options_candidatos_menu()
        option = menu.input_int_program("Selecione qual opção você deseja usar: ")
        match option:
            case 1:
                print("\nLista de candidatos registrados")
                print("===============================")
                for i in cr.read_candidatos():
                    print(f"ID: {i["id"]}")
                    print(f"NOME: {i["nome"]}")
                    print(f"RESUMO: {i["resumo"]}")
                    print(f"IDIOMAS ->")
                    for idioma in i["idiomas"]:
                        print("--------------------------------")
                        for idioma_key, idioma_value in idioma.items():
                            print(f"\t{idioma_key}: {idioma_value}")
                        print("--------------------------------")
                    print("===============================")
            case 2:
                person_id = menu.input_int_program("Selecione o ID do candidato que deseja ver: ")
                if person_id == None:
                    print("Insira um valor válido para o ID.")
                else:
                    candidato = cr.read_candidatos_by_id(person_id)
                    if candidato == -1:
                        print("Candidato não achado.")
                    else:
                        print(f"ID: {candidato["id"]}")
                        print(f"NOME: {candidato["nome"]}")
                        print(f"FOTO: {candidato["foto"]}")
                        print(f"CARGO: {candidato["cargo"]}")
                        print(f"RESUMO: {candidato["resumo"]}")
                        print(f"LOCALIZAÇÃO: {candidato["localizacao"]}")
                        print(f"AREA: {candidato["area"]}")
                        print(f"HABILIDADES ->")
                        
                        for habilidade in candidato["habilidades_tecnicas"]:
                            print(f"{habilidade}", end="; ")
                        print("\n--------------------------------")

                        print("SOFT SKILLS ->")
                        for soft_skills in candidato["soft_skills"]:
                            print(f"{soft_skills}", end="; ")
                        print("\n--------------------------------")

                        print("EXPERIÊNCIAS ->")
                        for experiencia in candidato["experiencias"]:
                            print("--------------------------------")
                            for key, value in experiencia.items():
                                print(f"\t{key}: {value}")
                            print("--------------------------------")
                            
                        print("FORMAÇÃO ->")
                        for formacao in candidato["formacao"]:
                            print("--------------------------------")
                            for key, value in formacao.items():
                                print(f"\t{key}: {value}")
                            print("--------------------------------")

                        print("PROJETOS ->")
                        for projeto in candidato["projetos"]:
                            print("--------------------------------")
                            for key, value in projeto.items():
                                print(f"\t{key}: {value}")
                            print("--------------------------------")

                        print("CERTIFICAÇÕES ->")
                        for certificacao in candidato["certificacoes"]:
                            print(f"{certificacao}", end="; ")
                        print("\n--------------------------------")

                        print(f"IDIOMAS ->")
                        for idioma in candidato["idiomas"]:
                            print("--------------------------------")
                            for key, value in idioma.items():
                                print(f"\t{key}: {value}")
                            print("--------------------------------")

                        print(f"ÁREAS DE INTERESSES ->")
                        for area in candidato["area_interesses"]:
                            print(f"{area}", end="; ")
                        print("\n--------------------------------")
                        print()
            case 3:
                id = menu.input_int_program("Insira um ID para o candidato: ")
                if id == None:
                    print("ID inválido. Tente novamente.\n")
                    continue
                is_valid_id = True
                for i in cr.read_candidatos():
                    if i["id"] == id:
                        is_valid_id = False
                        print("ID existente, não pode ter duplicidade. Tente novamente com outro ID.\n")
                if not is_valid_id:
                    continue

                nome = input("Insira o nome do candidato: ")
                foto = input("Insira a URL do candidato: ")
                cargo = input("Insira o cargo atual do candidato: ")
                resumo = input("Insira o resumo do candidato: ")
                localizacao = input("Insira a localização do candidato: ")
                area = input("Insira a área do candidato: ")
                
                habilidades_tecnicas = []
                while True:
                    ht_value = input("\nInsira as habilidades técnicas do candidato, aperte ENTER sem digitar para finalizar:\n")
                    if ht_value == "":
                        break
                    else:
                        habilidades_tecnicas.append(ht_value)
                
                soft_skills = []
                while True:
                    sk_value = input("\nInsira as soft skills do candidato, aperte ENTER sem digitar para finalizar:\n")
                    if sk_value == "":
                        break
                    else:
                        soft_skills.append(sk_value)

                experiencias = []
                while True:
                    xp = input("Insira as experiências do candidato sendo seguido o padrão abaixo ->\nNOME_EMPRESA;CARGO;DATA_INICIO;DATA_FINAL;DESCRICAO\nAperte ENTER sem digitar para finalizar:\n")
                    if xp == "":
                        break
                    else:
                        try:
                            xp = xp.split(";")
                            experiencias.append({
                                "empresa": xp[0],
                                "cargo": xp[1],
                                "inicio": xp[2],
                                "fim": xp[3],
                                "descricao": xp[4]
                            })
                        except IndexError:
                            print("Formato com informações faltando, tente novamente.")
                
                formacao = []
                while True:
                    frm = input("Insira as formações do candidato sendo seguido o padrão abaixo ->\nCURSO;INSTITUIÇÃO;ANO\nAperte ENTER sem digitar para finalizar:\n")
                    if frm == "":
                        break
                    else:
                        try:
                            frm = frm.split(";")
                            formacao.append({
                                "curso": frm[0],
                                "instituicao": frm[1],
                                "ano": frm[2]
                            })
                        except IndexError:
                            print("Formato com informações faltando, tente novamente.")

                projetos = []
                while True:
                    prj = input("Insira os projetos do candidato sendo seguido o padrão abaixo ->\nTÍTULO;LINK\nAperte ENTER sem digitar para finalizar:\n")
                    if prj == "":
                        break
                    else:
                        try:
                            prj = prj.split(";")
                            projetos.append({
                                "titulo": prj[0],
                                "link": prj[1]
                            })
                        except IndexError:
                            print("Formato com informações faltando, tente novamente.")
                
                certificacoes = []
                while True:
                    cert_value = input("\nInsira as certificações do candidato, aperte ENTER sem digitar para finalizar:\n")
                    if cert_value == "":
                        break
                    else:
                        certificacoes.append(cert_value)

                idiomas = []
                while True:
                    idm = input("\nInsira os idiomas do candidato sendo seguido o padrão abaixo ->\nIDIOMA;ANO\nAperte ENTER sem digitar para finalizar:\n")
                    if idm == "":
                        break
                    else:
                        try:
                            idm = idm.split(";")
                            idiomas.append({
                                "idioma": idm[0],
                                "ano": idm[1]
                            })
                        except IndexError:
                            print("Formato com informações faltando, tente novamente.")

                area_interesses = []
                while True:
                    ai_value = input("\nInsira as áreas de interesse do candidato, aperte ENTER sem digitar para finalizar:\n")
                    if ai_value == "":
                        break
                    else:
                        area_interesses.append(ai_value)
                
                cr.create_candidatos(
                    id, nome, foto,
                    cargo, resumo, localizacao,
                    area, habilidades_tecnicas,
                    soft_skills, experiencias,
                    formacao, projetos, certificacoes,
                    idiomas, area_interesses
                )
            case 4:
                person_id = menu.input_int_program("Selecione o ID do candidato que deseja atualizar: ")
                if person_id == None:
                    print("Insira um valor válido para o ID.")
                else:
                    candidato = cr.read_candidatos_by_id(person_id)
                    if candidato == -1:
                        print("Candidato não achado.")
                    else:
                        nome = input(f"Atual: {candidato["nome"]} -> Insira um nome para atualizar. Aperte ENTER sem digitar para não atualizar: ")
                        nome = None if nome == "" else nome
                        foto = input(f"Atual: {candidato["foto"]} -> Insira uma foto para atualizar. Aperte ENTER sem digitar para não atualizar: ")
                        foto = None if foto == "" else foto
                        cargo = input(f"Atual: {candidato["cargo"]} -> Insira um cargo para atualizar. Aperte ENTER sem digitar para não atualizar: ")
                        cargo = None if cargo == "" else cargo
                        resumo = input(f"Atual: {candidato["resumo"]} -> Insira um resumo para atualizar. Aperte ENTER sem digitar para não atualizar: ")
                        resumo = None if resumo == "" else resumo
                        localizacao = input(f"Atual: {candidato["localizacao"]} -> Insira uma localização para atualizar. Aperte ENTER sem digitar para não atualizar: ")
                        localizacao = None if localizacao == "" else localizacao
                        area = input(f"Atual: {candidato["area"]} -> Insira uma área para atualizar. Aperte ENTER sem digitar para não atualizar: ")
                        area = None if area == "" else area
                        

                        print("Habilidades técnicas atuais:")
                        for i in candidato["habilidades_tecnicas"]:
                            print(i, end="; ")
                        change_ht = input("\nDeseja atualiza a lista de habilidades técnicas? Digite 'SIM' para confirmar: ")
                        habilidades_tecnicas = []
                        if change_ht == "SIM":
                            while True:
                                print("\n")
                                print("Lista de habilidades técnicas:")
                                for i in habilidades_tecnicas:
                                    print(i, end="; ")
                                print("\n===========================")
                                ht_value = input("Insira uma habilidade técnica para adicionar a lista. Use '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if ht_value == "":
                                    break
                                elif ht_value == "<":
                                    habilidades_tecnicas.pop()
                                else:
                                    habilidades_tecnicas.append(ht_value)
                        habilidades_tecnicas = None if habilidades_tecnicas == [] else habilidades_tecnicas

                        print("Soft skills atuais:")
                        for i in candidato["soft_skills"]:
                            print(i, end="; ")
                        change_ss = input("\nDeseja atualiza a lista de soft skills? Digite 'SIM' para confirmar: ")
                        soft_skills = []
                        if change_ss == "SIM":
                            while True:
                                print("\n")
                                print("Lista de soft skills:")
                                for i in soft_skills:
                                    print(i, end="; ")
                                print("\n===========================")
                                ss_value = input("Insira uma soft skills para adicionar a lista. Use '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if ss_value == "":
                                    break
                                elif ss_value == "<":
                                    soft_skills.pop()
                                else:
                                    soft_skills.append(ss_value)
                        soft_skills = None if soft_skills == [] else soft_skills

                        print("Experiências atuais:")
                        for i in candidato["experiencias"]:
                            print("===========================")
                            for key, value in i.items():
                                print(f"{key}: {value}")
                            print("===========================")
                        change_xp = input("Deseja atualiza a lista de experiências? Digite 'SIM' para confirmar: ")
                        experiencias = []
                        if change_xp == "SIM":
                            while True:
                                print("\n")
                                print("Lista de experiências:")
                                for i in experiencias:
                                    for key, value in i.items():
                                        print(f"{key}: {value}")
                                    print("---------------------------")
                                print("===========================")
                                xp_value = input("Insira uma experiência para adicionar a lista. Deve obedecer o seguinte padrão -> \nEMPRESA;CARGO;DATA_INICIO;DATA_FINAL;DESCRICAO\nUse '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if xp_value == "":
                                    break
                                elif xp_value == "<":
                                    experiencias.pop()
                                else:
                                    try:
                                        xp_value = xp_value.split(";")
                                        experiencias.append({
                                            "empresa": xp_value[0],
                                            "cargo": xp_value[1],
                                            "inicio": xp_value[2],
                                            "fim": xp_value[3],
                                            "descricao": xp_value[4]
                                        })
                                    except IndexError:
                                        print("Formato com informações faltando, tente novamente.")
                        experiencias = None if experiencias == [] else experiencias        

                        print("Formações atuais:")
                        for i in candidato["formacao"]:
                            print("===========================")
                            for key, value in i.items():
                                print(f"{key}: {value}")
                            print("===========================")
                        change_frm = input("Deseja atualiza a lista de formações? Digite 'SIM' para confirmar: ")
                        formacao = []
                        if change_frm == "SIM":
                            while True:
                                print("\n")
                                print("Lista de formações:")
                                for i in formacao:
                                    for key, value in i.items():
                                        print(f"{key}: {value}")
                                    print("---------------------------")
                                print("===========================")
                                frm_value = input("Insira uma formação para adicionar a lista. Deve obedecer o seguinte padrão -> \nCURSO;INSTITUIÇÃO;ANO\nUse '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if frm_value == "":
                                    break
                                elif frm_value == "<":
                                    formacao.pop()
                                else:
                                    try:
                                        frm_value = frm_value.split(";")
                                        formacao.append({
                                            "curso": frm_value[0],
                                            "instituicao": frm_value[1],
                                            "ano": frm_value[2]
                                        })
                                    except IndexError:
                                        print("Formato com informações faltando, tente novamente.")
                        formacao = None if formacao == [] else formacao        

                        print("Projetos atuais:")
                        for i in candidato["projetos"]:
                            print("===========================")
                            for key, value in i.items():
                                print(f"{key}: {value}")
                            print("===========================")
                        change_prj = input("Deseja atualiza a lista de projetos? Digite 'SIM' para confirmar: ")
                        projetos = []
                        if change_prj == "SIM":
                            while True:
                                print("\n")
                                print("Lista de projetos:")
                                for i in projetos:
                                    for key, value in i.items():
                                        print(f"{key}: {value}")
                                    print("---------------------------")
                                print("===========================")
                                prj_value = input("Insira um projeto para adicionar a lista. Deve obedecer o seguinte padrão -> \nTITULO;LINK\nUse '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if prj_value == "":
                                    break
                                elif prj_value == "<":
                                    projetos.pop()
                                else:
                                    try:
                                        prj_value = prj_value.split(";")
                                        projetos.append({
                                            "titulo": prj_value[0],
                                            "link": prj_value[1],
                                        })
                                    except IndexError:
                                        print("Formato com informações faltando, tente novamente.")
                        projetos = None if projetos == [] else projetos

                        print("Certificações atuais:")
                        for i in candidato["certificacoes"]:
                            print(i, end="; ")
                        change_cert = input("\nDeseja atualiza a lista de certificações? Digite 'SIM' para confirmar: ")
                        certificacoes = []
                        if change_cert == "SIM":
                            while True:
                                print("\n")
                                print("Lista de certificações:")
                                for i in certificacoes:
                                    print(i, end="; ")
                                print("\n===========================")
                                cert_value = input("Insira uma certificação para adicionar a lista. Use '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if cert_value == "":
                                    break
                                elif cert_value == "<":
                                    certificacoes.pop()
                                else:
                                    certificacoes.append(cert_value)
                        certificacoes = None if certificacoes == [] else certificacoes

                        print("Idiomas atuais:")
                        for i in candidato["idiomas"]:
                            print("===========================")
                            for key, value in i.items():
                                print(f"{key}: {value}")
                            print("===========================")
                        change_idm = input("Deseja atualiza a lista de idiomas? Digite 'SIM' para confirmar: ")
                        idiomas = []
                        if change_idm == "SIM":
                            while True:
                                print("\n")
                                print("Lista de idiomas:")
                                for i in idiomas:
                                    for key, value in i.items():
                                        print(f"{key}: {value}")
                                    print("---------------------------")
                                print("===========================")
                                idm_value = input("Insira um idioma para adicionar a lista. Deve obedecer o seguinte padrão -> \nIDIOMA;ANO\nUse '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if idm_value == "":
                                    break
                                elif idm_value == "<":
                                    idiomas.pop()
                                else:
                                    try:
                                        idm_value = idm_value.split(";")
                                        idiomas.append({
                                            "idioma": idm_value[0],
                                            "ano": idm_value[1],
                                        })
                                    except IndexError:
                                        print("Formato com informações faltando, tente novamente.")
                        idiomas = None if idiomas == [] else idiomas

                        print("Áreas de interesse atuais:")
                        for i in candidato["area_interesses"]:
                            print(i, end="; ")
                        change_ai = input("\nDeseja atualiza a lista de áreas interessadas? Digite 'SIM' para confirmar: ")
                        area_interesses = []
                        if change_ai == "SIM":
                            while True:
                                print("\n")
                                print("Lista de áreas de interesse:")
                                for i in area_interesses:
                                    print(i, end="; ")
                                print("\n===========================")
                                ai_value = input("Insira uma área interessada para adicionar a lista. Use '<' depois ENTER para apagar o último da lista ou apenas ENTER para sair da nova lista.\n")
                                if ai_value == "":
                                    break
                                elif ai_value == "<":
                                    area_interesses.pop()
                                else:
                                    area_interesses.append(ai_value)
                        area_interesses = None if area_interesses == [] else area_interesses


                        cr.update_candidatos(
                            person_id, nome, foto,
                            cargo, resumo, localizacao,
                            area, habilidades_tecnicas,
                            soft_skills, experiencias,
                            formacao, projetos,
                            certificacoes, idiomas,
                            area_interesses        
                        )
            case 5:
                person_id = menu.input_int_program("Selecione o ID do candidato que deseja deletar: ")
                if person_id == None:
                    print("Insira um valor válido para o ID.")
                else:
                    candidato = cr.read_candidatos_by_id(person_id)
                    if candidato == -1:
                        print("Candidato não achado.")
                    else:  
                        person_data = cr.read_candidatos_by_id(person_id)
                        print(f"ID: {person_data["id"]}")
                        print(f"NOME: {person_data["nome"]}")
                        print(f"RESUMO: {person_data["resumo"]}")
                        print(f"IDIOMAS ->")
                        for idioma in person_data["idiomas"]:
                            print("--------------------------------")
                            for idioma_key, idioma_value in idioma.items():
                                print(f"\t{idioma_key}: {idioma_value}")
                            print("--------------------------------")
                        print("===============================")
                        print("\nTem certeza que deseja deletar esse candidato? Digite 'SIM' para confirmar.")
                        conf = input("")
                        if conf == "SIM":
                            print("Deletando...")
                            cr.delete_candidatos(person_id)
                            print("Deletado!")
                        else:
                            print("Cancelado!")  
            case 0:
                menu.cls_terminal()
                break
            case _:
                print("\nOpção inválida. Escolha uma das opções disponíveis")
        print()

def empresa_vagas_menu():
    """
    Interface de console no módulo de empresa e vagas.
    """
    er.verify_empresa_file()
    vr.verify_vagas_file()
    while True:
        menu.options_empresa_vagas_menu()
        option = menu.input_int_program("Selecione qual opção você deseja usar: ")
        match option:
            case 1:
                print("\nInformações da empresa:")
                for key, value in er.read_empresa().items():
                    print(f"{key}: {value}")
                print()
            case 2:
                nome = input("\nInsira o nome da empresa: ")
                descricao = input("Insira a descrição da empresa: ")
                er.create_empresa(nome, descricao)
                print("Definido com sucesso!")
            case 3:
                print("\nVagas em aberto no sistema: ")
                print("====================================")
                for i in vr.read_vagas():
                    for key, value, in i.items():
                        print(f"{key}: {value}")
                    print("====================================")
            case 4:
                id = menu.input_int_program("Insira um ID para a vaga: ")
                if id == None:
                    print("ID inválido. Tente novamente.\n")
                    continue
                is_valid_id = True
                for i in vr.read_vagas():
                    if i["id"] == id:
                        is_valid_id = False
                        print("ID existente, não pode ter duplicidade. Tente novamente com outro ID.\n")
                if not is_valid_id:
                    continue
                
                descricao = input("\nDescreva a vaga e seus requisitos:\n")
                qtnd = 0
                while True:
                    qtnd = menu.input_int_program("\nInsira a quantidade de vagas que devem ser preenchidas: ")
                    if qtnd != None:
                        break

                vr.create_vagas(id, descricao, qtnd)
            case 5:
                role_id = menu.input_int_program("Selecione o ID da vaga que deseja atualizar: ")
                if role_id == None:
                    print("Insira um valor válido para o ID.")
                else:
                    vaga = vr.read_vagas_by_id(role_id)
                    if vaga == -1:
                        print("Candidato não achado.")
                    else:
                        descricao = input(f"Atual: {vaga["descricao_requisitos"]} -> Insira uma descricao de requisitos para atualizar. Aperte ENTER sem digitar para não atualizar: \n")
                        descricao = None if descricao == "" else descricao
                        qtnd = input(f"Atual: {vaga["quantidade_vagas"]} -> Insira uma quantidade de vagas para atualizar. Aperte ENTER sem digitar para não atualizar: ")
                        qtnd = None if qtnd == "" else qtnd

                        vr.update_candidatos(role_id, descricao, qtnd)
            case 6:
                role_id = menu.input_int_program("Selecione o ID da vaga que deseja deletar: ")
                if role_id == None:
                    print("Insira um valor válido para o ID.")
                else:
                    vaga = vr.read_vagas_by_id(role_id)
                    if vaga == -1:
                        print("Vaga não achada.")
                    else:  
                        role_data = vr.read_vagas_by_id(role_id)
                        print(f"ID: {role_data["id"]}")
                        print(f"DESCRIÇÃO_REQUISITO: {role_data["descricao_requisitos"]}")
                        print(f"QUANTIDADE DE VAGAS: {role_data["quantidade_vagas"]}")
                        print("===============================")
                        print("\nTem certeza que deseja deletar essa vaga? Digite 'SIM' para confirmar.")
                        conf = input("")
                        if conf == "SIM":
                            print("Deletando...")
                            vr.delete_vagas(role_id)
                            print("Deletado!")
                        else:
                            print("Cancelado!")  
            case 0:
                menu.cls_terminal()
                break
            case _:
                print("\nOpção inválida. Escolha uma das opções disponíveis")
        print()
                

while True:
    menu.logo_app()
    menu.options_main_menu()
    option = menu.input_int_program("Selecione qual opção você deseja usar: ")
    match option:
        case 1:
            menu.cls_terminal()
            candidatos_menu()
            menu.cls_terminal()
        case 2:
            menu.cls_terminal()
            empresa_vagas_menu()
            menu.cls_terminal()
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("\nOpção inválida. Escolha uma das opções disponíveis")

