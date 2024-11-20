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


def menu_treino_modelo():
    clear()
    cabecalho_treino()
    print('''\
===         Modelo de Treino           ===
==========================================
== [1] Criar modelo de Treino           ==
== [2] Treino de Alunos                 ==
== [9] Voltar                           ==
==========================================''')
    try:
        opcao = input('''\n\
>>>   Escolha uma opção: ''')
        if opcao == '1':
            criar_modelo_treino()
        elif opcao == '2':
            treino_de_alunos()
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
    nome_do_treino = input(">>> Digite o nome do novo treino: ").strip()

    if not nome_do_treino:
        input("Nome do treino não pode estar vazio! Pressione Enter para tentar novamente.")
        return criar_modelo_treino() 

    nome_do_treino_normalizado = nome_do_treino.lower()

    try:
        
        if os.path.exists('data/treinos.json'):
            with open('data/treinos.json', 'r+', encoding='utf8') as arq:
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

        treinos.append(novo_treino)
        with open('data/treinos.json', 'w', encoding='utf8') as arq:
            json.dump(treinos, arq, indent=4)

        input(f"Treino '{nome_do_treino}' cadastrado com sucesso!\n\
Pressione Enter para continuar.")
    except Exception as e:
        input(f"Erro ao cadastrar treino: {e}\nPressione Enter para continuar.")

    cabeçalho_criar_modelo_treino()
    print(f'''\
 Cadastrando Treino: {nome_do_treino}''')
    input("")


def treino_de_alunos():
    pass
