import os
from modules.exercicio import exercicios_menu, listar_exercicios
from modules.alunos import menu_admin_alunos

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

def menu_admin():
    clear_terminal()
    cabecalho()
    cabecalho_adm()
    print('''\
==  1. Exercícios                       ==
==  2. Treinos                          ==
==  3. Alunos                           ==
==  4. Relatórios                       ==
==  5. Administradores                  ==
==  9. Sair                             ==
==========================================''')

    opcao = input("\n>>>> Escolha uma opção: ")
    if opcao == '1':
        exercicios_menu()
        menu_admin()
    elif opcao == '2':
        input("Funcionalidade em desenvolvimento. Pressione Enter para voltar.")
        menu_admin()
    elif opcao == '3':
        menu_admin_alunos()
        menu_admin()
    elif opcao in ('4', '5'):
        input("Funcionalidade em desenvolvimento. Pressione Enter para voltar.")
        menu_admin()


