import os



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
    cabecalho_exercicios()
    print('''\
===       Cadastro de Exercícios       ===
==========================================''')
    nome_exercicio = str(input('''\
==  Digite o nome do exercício:         ==\
'''))
    tipo_exercicio = str(input('''\
==  Digite o tipo do exercício:         ==\
'''))
    exercicio = {
        "nome" : nome_exercicio,
        "tipo" : tipo_exercicio
    }

    try:
        with open('exercicios.json' )

def listar_exercicios():
    ...

def buscar_exercicio():
    ...

def atualizar_exercicio():
    ...

def remover_exercicio():
    ...

def exercicios_menu():
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
        cadastrar_exercicio():
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
