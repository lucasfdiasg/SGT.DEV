import os
import json
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
    clear()
    cabecalho_exercicios()
    print('''\
==   1. Cadastrar Exercício             ==
==   2. Listar Exercícios               ==
==   3. Buscar Exercício                ==
==   4. Atualizar Exercício             ==
==   5. Remover Exercício               ==
==   9. Sair                            ==''')
    try:
        opcao = int(input("==   Escolha uma opção: "))
        if opcao == 1:
            cadastrar_exercicio()
        elif opcao == 2:
            listar_exercicios()
        elif opcao == 3:
            buscar_exercicio()
        elif opcao == 4:
            atualizar_exercicio()
        elif opcao == 5:
            remover_exercicio()
        else:
            print("Opção inválida!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def cadastrar_exercicio():
    clear()
    cabecalho_exercicios()
    print('''\
===       Cadastro de Exercícios       ===
==========================================''')
    nome_exercicio = input("==  Digite o nome do exercício:         ==\n\n>>>>    ").strip()
    tipo_exercicio = input("\n==  Digite o tipo do exercício:         ==\n\n>>>>    ").strip()


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
        print(f"Erro ao cadastrar exercício: {e}")

    clear()
    cabecalho_exercicios()
    print('''\
===                                    ===
===  Exercício cadastrado com sucesso! ===
===                                    ===
==========================================''')
    cadastrar_novo = int(input('''
>>>>    Cadastrar novo exercício?
        1. SIM    2. NÃO
'''))
    while cadastrar_novo not in (1, 2):
        clear()
        cabecalho_exercicios()
        print('''\
===           OPÇÃO INVÁLIDA           ===
==========================================''')
        cadastrar_novo = int(input('''
>>>>    Cadastrar novo exercício?
        1. SIM    2. NÃO
                '''))
    cadastrar_exercicio() if cadastrar_novo == 1 else exercicios_menu()    

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
                    print(f"== {i}. Nome: {exercicio['nome']}, Tipo: {exercicio['tipo']}")
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
    exercicios_menu()

def buscar_exercicio():
    # Implementação futura
    pass

def atualizar_exercicio():
    # Implementação futura
    pass

def remover_exercicio():
    # Implementação futura
    pass
