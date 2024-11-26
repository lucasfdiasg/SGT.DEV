import os
import json

########## GERAL ###########

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================''')

def cabecalho_adm():
    print('''\
===            Administrador           ===
==========================================''')
    

def exibir_menu_um():
    clear_terminal()
    cabecalho()
    print('''\
== 1. Login                             ==
== 2. Sair                              ==
==========================================''')
    opcao = input("\n>>>> Escolha uma opção e press 'Enter': ")
    return opcao

def menu_login():
    clear_terminal()
    cabecalho()
    print('''\
===                Login               ===
==========================================
== 1. Aluno                             ==
== 2. Instrutor                         ==
== 3. Administrador                     ==
==========================================''')
    
    tipo_usuario = input("\n>>>> Escolha o tipo de usuário: ")
    
    while tipo_usuario not in ('1', '2', '3'):
        clear_terminal()
        cabecalho()
        print('''\
===                Login               ===
==========================================
== 1. Aluno                             ==
== 2. Instrutor                         ==
== 3. Administrador                     ==
==========================================''')
        tipo_usuario = input("\n>>>> Escolha o tipo de usuário: ")

    clear_terminal()
    cabecalho()
    print('''\
===                Login               ===
==========================================
''')    
    usuario = input(">>>> Digite seu nome de usuário: ")
    senha = input("\n>>>> Digite sua senha: ")

    return tipo_usuario, usuario, senha

def verificar_login(tipo_usuario, usuario, senha): 
    if tipo_usuario == '3':
        arquivo = 'data/administrador.csv'
    else:
        input("Funcionalidade em desenvolvimento.\n\
Pressione Enter para voltar...")
        return

    try:
        with open(arquivo, mode='r', encoding='utf8') as arq:
            linhas = arq.readlines()[1:]
            for linha in linhas:
                try:
                    nome_arq, senha_arq = linha.strip().split(';')
                    if nome_arq.strip() == usuario.strip() and senha_arq.strip() == senha.strip():
                        return True
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Usuário não encontrado.")
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    return False

def menu_admin():
    clear_terminal()
    cabecalho()
    cabecalho_adm()
    print('''\
==  1. Exercícios                       ==
==  2. Treinos                          ==
==  3. Alunos                           ==
==  4. Configurações Administrativas    ==
==  9. Sair                             ==
==========================================''')

    opcao = input("\n>>>> Escolha uma opção: ")
    if opcao == '1':
        exercicios_menu()
        menu_admin()
    elif opcao == '2':
        menu_admin_treino()
        menu_admin()
    elif opcao == '3':
        menu_admin_alunos()
        menu_admin()
    elif opcao in ('4'):
        input("Funcionalidade em desenvolvimento. Pressione Enter para voltar.")
        menu_admin()
    elif opcao == '9':
        return


########## FUNÇÕES EM EXERCÍCIOS #########

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho_exercicios():
    print('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================
===            Administrador           ===
==========================================
===             Exercícios             ===
==========================================''')

def exercicios_menu():
    while True:
        clear()
        cabecalho_exercicios()
        print('''\
==  1. Cadastrar Exercício              ==
==  2. Listar Exercícios                ==
==  3. Buscar Exercício                 ==
==  9. Voltar                           ==
==========================================''')
        try:
            opcao = input("\n>>>   Escolha uma opção: ")
            if opcao == '1':
                cadastrar_exercicio()
            elif opcao == '2':
                listar_exercicios()
            elif opcao == '3':
                buscar_exercicio()
            elif opcao == '9':
                break 
            else:
                clear()
                input('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================
===            Administrador           ===
==========================================
===             Exercícios             ===
==========================================
===          Opção Inválida            ===
===     Pressione Enter retornar       ===
===        ao menu anterior...         ===
==========================================''')
                exercicios_menu()
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")



def cadastrar_exercicio():
    clear()
    cabecalho_exercicios()
    print('''\
===       Cadastro de Exercícios       ===
==========================================''')
    nome_exercicio = input("==  Digite o nome do exercício:         ==\n\n>>>>    ").strip()
    if not nome_exercicio:
        cadastrar_exercicio()
    tipo_exercicio = input("\n==  Digite o tipo do exercício:         ==\n\n>>>>    ").strip()
    if not tipo_exercicio:
        cadastrar_exercicio()

    nome_exercicio_normalizado = nome_exercicio.lower()

    exercicio = {
        "nome": nome_exercicio,
        "tipo": tipo_exercicio
    }

    try:

        if os.path.exists('data/exercicios.json'):
            with open('data/exercicios.json', mode='r+', encoding='utf-8') as arq:
                try:
                    exercicios = json.load(arq)
                except json.JSONDecodeError:
                    exercicios = []

                nomes_existentes = [ex['nome'].lower() for ex in exercicios]

                if nome_exercicio_normalizado in nomes_existentes:
                    clear()
                    cabecalho_exercicios()
                    print('''\
===    Exercício já está cadastrado!   ===
===       Não é possível duplicar      === 
==========================================''')
                    input('''\
===     Pressione Enter retornar       ===
===        ao menu anterior...         ===
==========================================''')                    
                    return

                exercicios.append(exercicio)
                arq.seek(0)
                json.dump(exercicios, arq, indent=4)

        else:
            with open('data/exercicios.json', mode='w', encoding='utf-8') as arq:
                json.dump([exercicio], arq, indent=4)

    except Exception as e:
        input(f"Erro ao cadastrar exercício: {e}")

    clear()
    cabecalho_exercicios()
    print('''\
===                                    ===
===  Exercício cadastrado com sucesso! ===
===                                    ===
==========================================''')

    cadastrar_novo = input('''
>>>>    Cadastrar novo exercício?
        1. SIM    2. NÃO
                ''')
    while cadastrar_novo not in ('1', '2'):
        clear()
        cabecalho_exercicios()
        print('''\
===           OPÇÃO INVÁLIDA           ===
==========================================''')
        cadastrar_novo = input('''
>>>>    Cadastrar novo exercício?
        1. SIM    2. NÃO
                ''')
    if cadastrar_novo == '1':
        cadastrar_exercicio()
    else:
        return

def listar_exercicios():
    clear()
    cabecalho_exercicios()
    print('''\
===         Lista de Exercícios        ===
==========================================''')
    try:
        with open('data/exercicios.json', 'r', encoding='utf-8') as arq:
            exercicios = json.load(arq)
            if not exercicios:
                print("Nenhum exercício cadastrado.")
            else:
                for i, exercicio in enumerate(exercicios, 1):
                    print(f"== {i}. {exercicio['nome']}, Tipo: {exercicio['tipo']}")
    except FileNotFoundError:
        print('''\
==      Nenhum Exercício Cadastrado!    ==''')
    except json.JSONDecodeError:
        print('''\
==         Erro ao carregar dados!      ==''')  
    input('''\
==                                      ==
==      Pressione Enter retornar        ==
==         ao menu anterior...          ==
==========================================''')
    clear()
    return

def buscar_exercicio():
    clear()
    cabecalho_exercicios()
    print('''===        Busca de Exercícios         ===
==========================================''')
    nome_exercicio = input('''\
==      Digite o nome do exercício      ==
==     ou 'Enter' para listar todos     ==
==========================================

>>>>    ''').strip().lower()
    
    try:
        with open('data/exercicios.json', 'r+', encoding='utf-8') as arq:
            exercicios = json.load(arq)
            
            resultados = [(i, ex) for i, ex in enumerate(exercicios)\
                          if nome_exercicio in ex['nome'].lower()]
            
            if resultados:
                clear()
                cabecalho_exercicios()
                print('''\
===         Resultado da Busca         ===
==========================================''')
                for idx, exercicio in resultados:
                    print(f'''\
ID: {idx}. {exercicio['nome']}, Tipo: {exercicio['tipo']}''')
                
                index_selecionado = input('''
>>> Selecione o exercício digitando seu ID
        ou 'x' para voltar ao menu  ''')             
                if index_selecionado.lower() == 'x':
                    return
                try:
                    index_selecionado = int(index_selecionado)
                    if index_selecionado in [idx for idx, _ in resultados]:
                        exercicio_selecionado = exercicios[index_selecionado]    
                        clear()
                        cabecalho_exercicios()
                        print(f'''\
===         Resultado da Busca         ===
==========================================
=== Exercício selecionado:              ==

>>>  {exercicio_selecionado['nome']}, {exercicio_selecionado['tipo']}
''')
                        print("\
==  1. Atualizar exercício              ==\n\
==  2. Remover este exercício           ==\n\
==  3. Sair                             ==\n\
==========================================")
                        escolha = input("\n>>> Selecione uma opção acima: ")
                        if escolha == '1':
                            atualizar_exercicio(index_selecionado, exercicios)
                        elif escolha == '2':
                            remover_exercicio(index_selecionado, exercicios)
                        else:
                            input("\nSaindo da busca...")
                    else:
                        input("Índice inválido.\n\
Pressione Enter para tentar novamente.")
                        buscar_exercicio()
                except ValueError:
                    input("\
Entrada inválida!\n\
Por favor, refaça a busca!")
                    buscar_exercicio()
            else:
                input("    Nenhum exercício encontrado\n\
    com o termo informado.\n\n\
    >>> Refaça a busca... ")
                buscar_exercicio()
                
    except FileNotFoundError:
        input("Nenhum exercício cadastrado.")
    except json.JSONDecodeError:
        input("Erro ao carregar dados.")
    return
    

def atualizar_exercicio(indice, exercicios):
    clear()
    cabecalho_exercicios()
    print('''\
===         Atualizar Exercício        ===
==========================================''')
    
    novo_nome = input("\n>>>>  Novo nome ou Enter para manter: \n\n>>>>    ").strip()
    novo_tipo = input("\n>>>>  Novo tipo ou Enter para manter: \n\n>>>>    ").strip()

    if novo_nome:
        exercicios[indice]['nome'] = novo_nome
    if novo_tipo:
        exercicios[indice]['tipo'] = novo_tipo

    with open('data/exercicios.json', 'w', encoding='utf-8') as arq:
        json.dump(exercicios, arq, indent=4)
    print("\n\
        Exercício atualizado com sucesso!\n")
    input(">>> Pressione Enter para retornar ao menu...")
    return

def remover_exercicio(indice, exercicios):
    clear()
    cabecalho_exercicios()
    print(f"\
===        Remover Exercício           ===\n\
==========================================\n\
===   Tem certeza que deseja remover   ===\n\
===     o exercício selecionado???     ===\n\
==========================================\n\
===          [1] Sim     [2] Não       ===\n\
==========================================")
    confirmacao = input(">>>>   ").strip().lower()
    
    if confirmacao == '1':
        exercicios.pop(indice)
        with open('data/exercicios.json', 'w', encoding='utf-8') as arq:
            json.dump(exercicios, arq, indent=4)
        input("\n\
>>> Exercício removido com sucesso!\n\
    Pressione Enter para continuar...")
    else:
        input("    Remoção cancelada.\n\
    Pressione Enter para continuar...")

########## FUNÇÕES EM TREINO ##########

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho_treino():
    print('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================
===            Administrador           ===
==========================================
===               Treino               ===
==========================================''')
    
def menu_admin_treino():
    clear()
    cabecalho_treino()
    print('''\
== [1] Modelo de Treinos                ==
== [2] Treinos de Alunos                ==
== [9] Voltar                           ==
==========================================''')
    try:
        opcao = input('''\
>>>   Escolha uma opção: ''')
        if opcao == '1':
            menu_treino_modelo()
        elif opcao == '2':
            menu_treino_alunos()
        elif opcao == '9':
            return
        else:
            clear()
            cabecalho_treino()
            input('''\
===          Opção Inválida            ===
===     Pressione Enter retornar       ===
===        ao menu anterior...         ===
==========================================''')
            menu_admin_treino()
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def listar_modelos():
    clear()
    cabecalho_treino()
    print('''\
===          Modelos de Treino         ===
==========================================''')
    try:
        with open('data/modelos.json', 'r', encoding='utf8') as arq:
            modelos = json.load(arq)
            if not modelos:
                input("\nNenhum modelo cadastrado...\n\
Pressione enter para continuar...")
            else:
                for i, modelo in enumerate(modelos, 1):
                    print(f'\n\
{i}. {modelo['nome']}')
    except FileNotFoundError:
        print('''\
==        Nenhum Treino Cadastrado!     ==''')
    except json.JSONDecodeError:
        print('''\
==         Erro ao carregar dados!      ==''')  
    input('''\
==                                      ==
==      Pressione Enter retornar        ==
==         ao menu anterior             ==
==========================================''')
    clear()
    menu_treino_modelo()

def buscar_treino():
    clear()
    cabecalho_treino()
    print('''\
===          Busca de Treinos          ===
==========================================''')
    nome_treino = input('''\
==        Digite o nome do treino       ==
==     ou 'Enter' para listar todos     ==
==========================================

>>>>    ''').strip().lower()

    try:
        with open('data/modelos.json', 'r', encoding='utf8') as arq:
            modelos = json.load(arq)

            resultados = [(i, mod) for i, mod in enumerate(modelos) \
                           if nome_treino in mod['nome'].lower()]
            if resultados:
                clear()
                cabecalho_treino()
                print('''\
===         Resultado da Busca         ===
==========================================''')
                for idx, treino in resultados:
                    print(f'''\
 ID: {idx}. {treino['nome']}''')
                    
                index_selecionado = input('''
>>>   Selecione o treino digitando seu ID
            ou 'x' para retornar ao menu   ''')
                if index_selecionado.lower() == 'x':
                    menu_admin_treino()
                try:
                    index_selecionado = int(index_selecionado)
                    if index_selecionado in [idx for idx, _ in resultados]:
                        modelo_selecionado = modelos[index_selecionado]
                        clear()
                        cabecalho_treino()
                        print(f'''\
===         Resultado da Busca         ===
==========================================
=== Treino selecionado:                 ==

>>>  {modelo_selecionado['nome']}
''')
                        print("\
==  1. Remover este treino              ==\n\
==  9. Sair                             ==\n\
==========================================")
                        escolha = input("\n>>> Selecione uma opção acima: ")
                        if escolha == '1':
                            remover_treino(index_selecionado, modelos)
                        else:
                            input('\n Saindo da busca...')
                            menu_admin_treino()
                    else:
                        input("Índice inválido.\n\
Pressione Enter para tentar novamente.")
                        buscar_treino()
                except ValueError:
                    input("\
Entrada inválida!\n\
Por favor, refaça a busca!")
                    buscar_treino()
                else:
                    input("    Nenhum treino encontrado\n\
    com o termo informado.\n\n\
\
    >>> Refaça a busca... ")
                    buscar_treino()

    except FileNotFoundError:
        input("Nenhum treino cadastrado.")
    except json.JSONDecodeError:
        input("Erro ao carregar dados.")
    menu_admin_treino()

def remover_treino(indice, modelos):
    clear()
    cabecalho_treino()
    print(f"\
===        Remover Exercício           ===\n\
==========================================\n\
===   Tem certeza que deseja remover   ===\n\
===       o treino selecionado???      ===\n\
==========================================\n\
===          [1] Sim     [2] Não       ===\n\
==========================================")
    confirmacao = input(">>>>   ").strip().lower()
    
    if confirmacao == '1':
        modelos.pop(indice)
        with open('data/modelos.json', 'w', encoding='utf8') as arq:
            json.dump(modelos, arq, indent=4)
        input("\n\
      Exercício removido com sucesso!\n\
>>>   Pressione Enter para continuar...")
        menu_treino_modelo()
    else:
        input("    Remoção cancelada.\n\
    Pressione Enter para continuar...")
        menu_treino_modelo()
        
def menu_treino_modelo():
    clear()
    cabecalho_treino()
    print('''\
===         Modelo de Treino           ===
==========================================
== [1] Criar modelo de Treino           ==
== [2] Listar Modelos de Treino         ==
== [3] Buscar Treino                    ==
== [9] Voltar                           ==
==========================================''')
    try:
        opcao = input('''\n\
>>>   Escolha uma opção: ''')
        if opcao == '1':
            criar_modelo_treino()
        elif opcao == '2':
            listar_modelos()
        elif opcao == '3':
            buscar_treino()
        elif opcao == '9':
            return
        else:
            clear()
            cabecalho_treino()
            input('''\
===          Opção Inválida            ===
===     Pressione Enter retornar       ===
===        ao menu anterior...         ===
==========================================''')
            menu_admin_treino()
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def menu_treino_alunos():
    input("Funcionalidade em desenvolvimento. Pressione Enter para voltar.")
    return

def cabeçalho_criar_modelo_treino():
    clear()
    cabecalho_treino()
    print('''\
===        Novo Modelo de Treino       ===
==========================================''')

def criar_modelo_treino():
    cabeçalho_criar_modelo_treino()
    nome_do_treino = input("\
==     Digite o nome do novo treino:    ==\n\
==========================================\n\
\n>>>   ").strip()

    if not nome_do_treino:
        input("Nome do treino não pode estar vazio!\n\
Pressione Enter para tentar novamente...")
        return criar_modelo_treino()

    nome_do_treino_normalizado = nome_do_treino.lower()

    try:
        if os.path.exists('data/modelos.json'):
            with open('data/modelos.json', 'r+', encoding='utf8') as arq:
                try:
                    treinos = json.load(arq)
                except json.JSONDecodeError:
                    treinos = []
        else:
            treinos = []

        nomes_treinos_existentes = [treino['nome'].lower() for treino in treinos]
        if nome_do_treino_normalizado in nomes_treinos_existentes:
            clear()
            cabeçalho_criar_modelo_treino()
            input('''\
=== Nome do treino já está cadastrado! ===
===       Não é possível duplicar      ===
==========================================
Pressione Enter para tentar novamente...''')
            return criar_modelo_treino()

        novo_treino = {"nome": nome_do_treino, "exercicios": []}
        sair = False

        while not sair:
            cabeçalho_criar_modelo_treino()
            print(f"Cadastrando Treino: {nome_do_treino}")
            print("=" * 42)
            
            if novo_treino["exercicios"]:
                print("Exercícios adicionados:")
                for idx, ex in enumerate(novo_treino["exercicios"]):
                    print(f"[{idx + 1}] {ex['nome']} | Séries: {ex['series']} | Rep: {ex['repeticoes']}")
                print("=" * 42)
            else:
                print("   Nenhum exercício adicionado até agora.")
                print("=" * 42)

            escolha = input('''\
== Adicionar Exercício                  ==
==                                      ==
== [1] Buscar por Nome                  ==
== [2] Exercício Personalizado          ==
== [9] Finalizar e Salvar Treino        ==
==========================================
>>>  ''').strip()

            if escolha == '1':
                adicionar_exercicio_por_busca(novo_treino)
            elif escolha == '2':
                adicionar_exercicio_personalizado(novo_treino)
            elif escolha == '9':
                sair = True
            else:
                input("Escolha inválida! Pressione Enter para tentar novamente.")
        treinos.append(novo_treino)
        with open('data/modelos.json', 'w', encoding='utf8') as arq:
            json.dump(treinos, arq, indent=4)

        input(f"Treino '{nome_do_treino}' salvo com sucesso!\n\nPressione Enter para continuar....")

    except Exception as e:
        input(f"Erro ao cadastrar treino: {e}\nPressione Enter para continuar.")


def adicionar_exercicio_por_busca(treino):
    try:
        with open('data/exercicios.json', 'r', encoding='utf8') as arq:
            exercicios = json.load(arq)

        nome_exercicio = input("\
Digite o nome do exercício para buscar:\n\
>>>   ").strip().lower()
        resultados = [ex for ex in exercicios if nome_exercicio in ex['nome'].lower()]

        if resultados:
            print("\n\
==========================================\n\
===        Resultados da busca         ===\n")
            for i, ex in enumerate(resultados):
                print(f"[{i}] Nome: {ex['nome']}, Tipo: {ex['tipo']}")

            indice = input("\nSelecione o índice do exercício\n\
desejado ou 'x' para cancelar:\n>>>   ").strip()
            if indice.lower() == 'x':
                return

            try:
                indice = int(indice)
                if 0 <= indice < len(resultados):
                    exercicio = resultados[indice]
                    series = int(input(f"\n\
Digite o número de séries para:\n\
'{exercicio['nome']}' >>>    ").strip())
                    repeticoes = input(f"\n\
Digite as repetições para:\n\
'{exercicio['nome']}' >>>   ").strip()
                    exercicio_completo = {
                        "nome": exercicio['nome'],
                        "tipo": exercicio['tipo'],
                        "series": series,
                        "repeticoes": repeticoes,
                    }
                    treino["exercicios"].append(exercicio_completo)
                    input(f"\n\
==========================================\n\
===   Exercício '{exercicio['nome']}'\n\
===       adicionado com sucesso!      ===\n\
==========================================\n\
Pressione Enter para continuar....")
                else:
                    input("Índice inválido!\n\nPressione Enter para tentar novamente.")
            except ValueError:
                input("Entrada inválida!\n\nPressione Enter para tentar novamente.")
        else:
            input("Nenhum exercício encontrado!\n\nPressione Enter para tentar novamente.")
    except FileNotFoundError:
        input("Arquivo de exercícios não encontrado!\n\nPressione Enter para continuar.")
    except json.JSONDecodeError:
        input("Erro ao ler o arquivo de exercícios!\n\nPressione Enter para continuar.")

def adicionar_exercicio_personalizado(novo_treino):
    cabeçalho_criar_modelo_treino()
    print('''\
===  Adicionar Exercício Personalizado ===
==========================================''')

    try:
        nome = input("Digite o nome do exercício:\n>>>   ").strip()
        if not nome:
            input("O nome do exercício não pode estar vazio! Pressione Enter para tentar novamente.")
            return adicionar_exercicio_personalizado(novo_treino)

        tipo = input("Digite o tipo do exercício:\n>>>   ").strip()
        if not tipo:
            input("O tipo do exercício não pode estar vazio! Pressione Enter para tentar novamente.")
            return adicionar_exercicio_personalizado(novo_treino)

        try:
            series = int(input("Digite o número de séries:\n>>>   ").strip())
        except ValueError:
            input("Número de séries inválido! Pressione Enter para tentar novamente.")
            return adicionar_exercicio_personalizado(novo_treino)

        repeticoes = input("Digite o número de repetições:\n>>>   ").strip()
        if not repeticoes:
            input("O número de repetições não pode estar vazio! Pressione Enter para tentar novamente.")
            return adicionar_exercicio_personalizado(novo_treino)

        exercicio_personalizado = {
            "nome": nome,
            "tipo": tipo,
            "series": series,
            "repeticoes": repeticoes,
        }

        novo_treino["exercicios"].append(exercicio_personalizado)

        input(f"\nExercício '{nome}' adicionado com sucesso!\nPressione Enter para continuar...")

    except Exception as e:
        input(f"Erro ao adicionar exercício personalizado: {e}\nPressione Enter para continuar.")

########## FUNÇÕES EM ALUNOS ##########

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

#v.21/11/2024