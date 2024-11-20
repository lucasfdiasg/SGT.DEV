import os
import json


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho_admin_alunos():
    print('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================
===            Administrador           ===
==========================================
===               Alunos               ===
==========================================''')

def cadastrar_alunos():
    clear()
    cabecalho_admin_alunos()
    print('''\
===        Cadastro de Alunos          ===
==========================================''')
    try:
        if os.path.exists('data/alunos.json'):
            with open('data/alunos.json', mode='r+', encoding='utf-8') as arq:
                try:
                    alunos = json.load(arq)
                except json.JSONDecodeError:
                    alunos = []
        else:
            alunos = []
        matricula = 1000 + len(alunos)

        nome = input("==  Digite o nome completo do aluno:    ==\n\n>>>>    ").strip()
        nome_normalizado = nome.lower()
        nomes_existentes = [al['nome'].lower() for al in alunos]

        if nome_normalizado in nomes_existentes:
            clear()
            cabecalho_admin_alunos()
            print('''\
===     Nome já está cadastrado!       ===
===       Não é possível duplicar      ===
==========================================''')
            input("\n>>> Pressione Enter para voltar ao menu...")
            menu_admin_alunos()

        clear()
        cabecalho_admin_alunos()
        idade = int(input("==  Digite a idade do aluno:            ==\n\n>>>>    ").strip())

        clear()
        cabecalho_admin_alunos()
        m_ou_f = input("\
==      Selecione o sexo do aluno:      ==\n\
==     [1] Masculino   [2] Feminino     ==\n\
==========================================\n>>>>    ").strip()
        while m_ou_f not in ("1", "2"):
            clear()
            cabecalho_admin_alunos()
            print("===      Opção inválida! Tente novamente.     ===\n")
            m_ou_f = input("\
==      Selecione o sexo do aluno:      ==\n\
==     [1] Masculino   [2] Feminino     ==\n\
==========================================\n>>>>    ").strip()
        sexo = "masculino" if m_ou_f == '1' else "feminino"

        clear()
        cabecalho_admin_alunos()
        peso = float(input("==  Digite o peso do aluno (kg):        ==\n\
==========================================\n\n>>>>    ").strip())

        clear()
        cabecalho_admin_alunos()
        altura_cm = float(input("==  Digite a altura do aluno (cm):      ==\n\
==========================================\n\n>>>>    ").strip())
        altura = altura_cm / 100

        clear()
        cabecalho_admin_alunos()
        f_h_e = input("==  Selecione o objetivo do aluno:      ==\n\
===     [1] Força   [2] Hipertrofia    ===\n\
===         [3] Emagrecimento          ===\n\
==========================================\n>>>>    ").strip()
        while f_h_e not in ("1", "2", "3"):
            clear()
            cabecalho_admin_alunos()
            print("===      Opção inválida! Tente novamente.     ===\n")
            f_h_e = input("==  Selecione o objetivo do aluno:      ==\n\
===     [1] Força   [2] Hipertrofia    ===\n\
===         [3] Emagrecimento          ===\n\
==========================================\n\n>>>>    ").strip()
        objetivo = "Força" if f_h_e == "1" else "Hipertrofia" if f_h_e == "2" else "Emagrecimento"

        aluno = {
            "matricula": matricula,
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
            "peso": peso,
            "altura": altura,
            "objetivo": objetivo
        }

        alunos.append(aluno)
        with open('data/alunos.json', mode='w', encoding='utf-8') as arq:
            json.dump(alunos, arq, indent=4)

        clear()
        cabecalho_admin_alunos()
        print(f'''\
===                                    ===
===    Aluno cadastrado com sucesso!   ===
===          Matrícula: {matricula}           ===
===                                    ===
==========================================''')

    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")

    cadastrar_novo = input('''\n\
>>> Deseja cadastrar outro aluno?
    [1] SIM    [2] NÃO

>>>>    ''').strip()
    while cadastrar_novo not in ('1', '2'):
        clear()
        cabecalho_admin_alunos()
        print("===  Opção inválida! Tente novamente. ===\n")
        cadastrar_novo = input('''\n\
>>> Deseja cadastrar outro aluno?
    [1] SIM    [2] NÃO

>>>>    ''').strip()
    cadastrar_alunos() if cadastrar_novo == '1' else menu_admin_alunos()

def listar_alunos():
    clear()
    cabecalho_admin_alunos()
    print('''\
===          Lista de Alunos           ===
==========================================''')

    try:
        if os.path.exists('data/alunos.json'):
            with open('data/alunos.json', mode='r', encoding='utf-8') as arq:
                try:
                    alunos = json.load(arq)
                except json.JSONDecodeError:
                    alunos = []
        else:
            alunos = []

        if not alunos:
            print('''\
===      Nenhum aluno cadastrado!       ===
==========================================''')
            input("\n>>> Pressione Enter para voltar ao menu...")
            menu_admin_alunos()

        print(f"\n{'Matrícula':<10} | Nome")
        print(f"{'-'*10} | {'-'*30}")

        for aluno in alunos:
            print(f"{aluno['matricula']:<10} | {aluno['nome']}")

        print("==========================================")
        input("\n>>> Pressione Enter para voltar ao menu...")

    except Exception as e:
        print(f"Erro ao listar alunos: {e}")
        input("\n>>> Pressione Enter para voltar ao menu...")

    menu_admin_alunos()


def buscar_alunos():
    clear()
    cabecalho_admin_alunos()
    print('''\
===        Busca de Alunos             ===
==========================================''')

    try:
        if os.path.exists('data/alunos.json'):
            with open('data/alunos.json', mode='r+', encoding='utf-8') as arq:
                try:
                    alunos = json.load(arq)
                except json.JSONDecodeError:
                    alunos = []
        else:
            alunos = []

        if not alunos:
            print('''\
===      Nenhum aluno cadastrado!       ===
==========================================''')
            input("\n>>> Pressione Enter para voltar ao menu...")
            menu_admin_alunos()

        nome_busca = input("\n>>> Digite o nome do aluno a ser buscado:\n\n>>>  ").strip().lower()

        alunos_encontrados = [
            aluno for aluno in alunos if nome_busca in aluno['nome'].lower()
        ]

        if not alunos_encontrados:
            clear()
            cabecalho_admin_alunos()
            print('''\
===   Nenhum aluno encontrado com o    ===
===       nome especificado!           ===
==========================================''')
            input("\n>>> Pressione Enter para voltar ao menu...")
            menu_admin_alunos()

        print(f"\n{'Matrícula':<10} | Nome")
        print(f"{'-'*10} | {'-'*30}")
        for aluno in alunos_encontrados:
            print(f"{aluno['matricula']:<10} | {aluno['nome']}")
        print("\n==========================================")

        matricula_selecionada = int(input("\n>>> Digite a matrícula do aluno desejado: ").strip())
        aluno_selecionado = next((aluno for aluno in alunos if aluno['matricula'] == matricula_selecionada), None)

        if not aluno_selecionado:
            clear()
            cabecalho_admin_alunos()
            print('''\
===     Matrícula não encontrada!      ===
==========================================''')
            input("\n>>> Pressione Enter para voltar ao menu...")
            buscar_alunos()

        while True:
            clear()
            cabecalho_admin_alunos()
            print(f'''\n>>> Aluno selecionado: {aluno_selecionado['nome']}
==========================================''')
            print('''\
===    O que deseja fazer?             ===
===  [1] Exibir informações            ===
===  [2] Atualizar informações         ===
===  [9] Voltar                        ===
==========================================''')
            opcao = input("\n>>> Escolha uma opção: ").strip()

            if opcao == '1':  # Exibir informações
                clear()
                cabecalho_admin_alunos()
                print(f'''\n>>> Informações do Aluno:
==========================================
Matrícula: {aluno_selecionado['matricula']}
Nome: {aluno_selecionado['nome']}
Idade: {aluno_selecionado['idade']}
Sexo: {aluno_selecionado['sexo']}
Peso: {aluno_selecionado['peso']} kg
Altura: {aluno_selecionado['altura']} m
Objetivo: {aluno_selecionado['objetivo']}
==========================================''')
                input("\n>>> Pressione Enter para voltar...")

            elif opcao == '2':
                atualizar_informacoes_aluno(alunos, aluno_selecionado)
                break

            elif opcao == '9':
                break

            else:
                clear()
                cabecalho_admin_alunos()
                print('''\
===           OPÇÃO INVÁLIDA           ===
==========================================''')
                input("\n>>> Pressione Enter para tentar novamente...")

    except Exception as e:
            clear()
            cabecalho_admin_alunos()
            print('''\
===     Matrícula não encontrada!      ===
==========================================''')
            input("\n>>> Pressione Enter para voltar ao menu...")
            buscar_alunos()
    menu_admin_alunos()

def atualizar_informacoes_aluno(alunos, aluno):
    clear()
    cabecalho_admin_alunos()
    print(f'''\n>>> Atualizando informações do aluno: {aluno['nome']}
==========================================''')

    try:
        aluno['nome'] = input(f"Novo nome [{aluno['nome']}]: ").strip() or aluno['nome']
        aluno['idade'] = int(input(f"Nova idade [{aluno['idade']}]: ").strip() or aluno['idade'])
        
        clear()
        cabecalho_admin_alunos()
        print(f"\n>>> Atualizar sexo do aluno:")
        print(f"Sexo atual: {aluno['sexo']}")
        sexo_opcao = input('''\
===  [1] Masculino
===  [2] Feminino
==========================================
>>> Escolha o novo sexo (1/2): ''').strip()
        while sexo_opcao not in ('1', '2'):
            clear()
            cabecalho_admin_alunos()
            print(f"\n>>> Atualizar sexo do aluno:")
            print(f"Sexo atual: {aluno['sexo']}")
            sexo_opcao = input('''\
===  [1] Masculino
===  [2] Feminino
==========================================
>>> Escolha o novo sexo (1/2): ''').strip()
        aluno['sexo'] = "masculino" if sexo_opcao == '1' else "feminino"

        aluno['peso'] = float(input(f"Novo peso [{aluno['peso']} kg]: ").strip() or aluno['peso'])

# altura_cm = float(input("==  Digite a altura do aluno (cm):      ==\n\
# ==========================================\n\n>>>>    ").strip())
#         altura = altura_cm / 100

        aluno_cm = float(input(f"Nova altura [{int(aluno['altura'] * 100)} cm]: ").strip() or aluno['altura'])
        aluno['altura'] = aluno_cm / 100

        clear()
        cabecalho_admin_alunos()
        print(f"\n>>> Atualizar objetivo do aluno:")
        print(f"Objetivo atual: {aluno['objetivo']}")
        objetivo_opcao = input('''\
===  [1] Força
===  [2] Hipertrofia
===  [3] Emagrecimento
==========================================
>>> Escolha o novo objetivo (1/2/3): ''').strip()
        while objetivo_opcao not in ('1', '2', '3'):
            clear()
            cabecalho_admin_alunos()
            print(f"\n>>> Atualizar objetivo do aluno:")
            print(f"Objetivo atual: {aluno['objetivo']}")
            objetivo_opcao = input('''\
===  [1] Força
===  [2] Hipertrofia
===  [3] Emagrecimento
==========================================
>>> Escolha o novo objetivo (1/2/3): ''').strip()
        aluno['objetivo'] = "Força" if objetivo_opcao == '1' else "Hipertrofia" if objetivo_opcao == '2' else "Emagrecimento"

        with open('data/alunos.json', mode='w', encoding='utf-8') as arq:
            json.dump(alunos, arq, indent=4)

        clear()
        cabecalho_admin_alunos()
        print('''\
===   Informações atualizadas com      ===
===          sucesso!                  ===
==========================================''')
        input("\n>>> Pressione Enter para voltar...")

    except Exception as e:
        print(f"Erro ao atualizar informações: {e}")
        input("\n>>> Pressione Enter para voltar...")


def menu_admin_alunos():
    clear()
    cabecalho_admin_alunos()
    print('''\
==  1. Cadastrar Aluno                  ==
==  2. Listar Alunos                    ==
==  3. Buscar Alunos                    ==
==  9. Voltar                           ==
==========================================''')
    try:
        opcao = input("\n>>>   Escolha uma opção: ")
        if opcao == '1':
            cadastrar_alunos()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_alunos()
        elif opcao == '9':
            return
        else:
            clear()
            input('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================
===            Administrador           ===
==========================================
===               Alunos               ===
==========================================
===          Opção Inválida            ===
===     Pressione Enter retornar       ===
===        ao menu anterior...         ===
==========================================''')
            menu_admin_alunos()
    except ValueError:
        input("Entrada inválida! Por favor, insira um número.")

        