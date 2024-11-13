import os
import json
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho_exercicios():
    print('''\
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================
===            Administrador           ===
==========================================
===             Exercícios             ===
==========================================''')

def cadastrar_exercicio():
    clear()
    cabecalho_exercicios()
    print('''\
===       Cadastro de Exercícios       ===
==========================================''')
    nome_exercicio = str(input('''\
==  Digite o nome do exercício:         ==
==   '''))
    tipo_exercicio = str(input('''\
==  Digite o tipo do exercício:         ==
==   '''))
    exercicio = {
        "nome" : nome_exercicio,
        "tipo" : tipo_exercicio
    }

    try:
        with open('data/exercicios.json', mode='r', encoding='utf-8') as arq:
            exercicios = json.load(arq)
            exercicios.append(exercicio)
            arq.seek(0)
            json.dump(exercicios, arq, indent=4)
    except FileNotFoundError:
        with open('data/exercicios.json', mode='w', encoding='utf-8') as arq:
            json.dump([exercicio], arq, indent=4)   
    clear()
    cabecalho_exercicios()
    print('''\
===  Exercício cadastrado com sucesso! ===
==========================================''')

    

def listar_exercicios():
    cabecalho_exercicios()
    print('''\
===         Lista de Exercícios        ===
==========================================''')
    try:
        with open('exercicios.json', 'r', encoding='utf-8') as arq:
            exercicios = json.load(arq)
            if not exercicios:
                print("Nenhum exercício cadastrado.")
            else:
                for i, exercicio in enumerate(exercicios, 1):
                    print(f"{i}. Nome: {exercicio['nome']}, Tipo: {exercicio['tipo']}")
    except FileNotFoundError:
        print("Nenhum exercício cadastrado.")
    
    input("\nPressione Enter para continuar...")
    clear()

def buscar_exercicio():
    ...

def atualizar_exercicio():
    ...

def remover_exercicio():
    ...

def exercicios_menu():
    clear()
    cabecalho_exercicios()
    print('''\
==   1. Cadastrar Exercício             ==
==   2. Listar Exercícios               ==
==   3. Buscar Exercício                ==
==   4. Atualizar Exercício             ==
==   5. Remover Exercício               ==
==   9. Sair                            ==''')
    opcao = int(input("==   Escolha uma opção: "))
    if opcao == 1:
        cadastrar_exercicio()
    elif opcao == 2:
        ...
    elif opcao == 3:
        ...
    elif opcao == 4:
        ...
    elif opcao == 5:
        ...
    else:
        ...
