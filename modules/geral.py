import os
from modules.exercicio import exercicios_menu

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================''')

def exibir_menu_um():
    cabecalho()
    print("\
== 1. Login                             ==")
    print("\
== 2. Sair                              ==")
    opcao = input("Escolha uma opção: ")
    return opcao

def menu_login():
    clear_terminal()
    cabecalho()
    print('''\
===                Login               ===
==========================================''')
    print('''\
== 1. Aluno                             ==''')
    print('''\
== 2. Administrador                     ==''')
    
    tipo_usuario = int(input("== Escolha o tipo de usuário: "))
    
    while tipo_usuario not in (1, 2):
        clear_terminal()
        cabecalho()
        print('''\
===                Login               ===
==========================================''')
        print('''\
===      Tipo de usuário inválido!     ===
===          Tente Novamente!          ===
==========================================''')
        print('''\
== 1. Aluno                             ==''')
        print('''\
== 2. Administrador                     ==''')
        tipo_usuario = input("== Escolha o tipo de usuário: ")

    clear_terminal()
    cabecalho()
    print('''\
===                Login               ===
==========================================''')    
    usuario = input("==  Digite seu nome de usuário: ")
    senha = input("==  Digite sua senha: ")

    return tipo_usuario, usuario, senha

def verificar_login(tipo_usuario, usuario, senha): 
    if tipo_usuario == '1':
        arquivo = 'data/alunos.csv'
    else:
        arquivo = 'data/administrador.csv'

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

def cabecalho_adm():
    print('''\
===            Administrador           ===
==========================================''')

def menu_admin():
    clear_terminal()
    cabecalho()
    cabecalho_adm()
    print('''\
==  1. Exercícios                       ==
==  2. Treinos                          ==
==  3. Alunos                           ==
==  4. Relatórios                       ==
==  5. Sair                             ==''')

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        exercicios_menu()
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




