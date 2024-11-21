import os
import json

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
    else:
        input("    Remoção cancelada.\n\
    Pressione Enter para continuar...")
        

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
            menu_admin_treino()
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
    pass

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
            
            # Exibir os exercícios adicionados no formato ficha
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

        # Salvar treino no arquivo
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
