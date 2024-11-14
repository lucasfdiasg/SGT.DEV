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
==  1. Cadastrar Exercício              ==
==  2. Listar Exercícios                ==
==  3. Buscar Exercício                 ==
==  9. Sair                             ==
==========================================''')
    try:
        opcao = input("\n>>>   Escolha uma opção: ")
        if opcao == '1':
            cadastrar_exercicio()
        elif opcao == '2':
            listar_exercicios()
        elif opcao == '3':
            buscar_exercicio()
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
    cadastrar_exercicio() if cadastrar_novo == '1' else exercicios_menu()    

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
    clear()
    cabecalho_exercicios()
    print('''===        Busca de Exercícios         ===
==========================================''')
    nome_exercicio = input('''\
==  Digite o nome do exercício:         ==
==========================================

>>>>    ''').strip().lower()
    
    try:
        with open('data/exercicios.json', 'r+', encoding='utf-8') as arq:
            exercicios = json.load(arq)
            
            resultados = [(i, ex) for i, ex in enumerate(exercicios) if nome_exercicio in ex['nome'].lower()]
            
            if resultados:
                print("\nExercícios encontrados:\n")
                for idx, exercicio in resultados:
                    print(f'''\
ID: {idx}. {exercicio['nome']}, Tipo: {exercicio['tipo']}''')
                
                index_selecionado = input('''
>>> Selecione o exercício digitando seu ID
        ou 'Enter' para voltar ao menu  ''')             
        
                try:
                    index_selecionado = int(index_selecionado)
                    if index_selecionado in [idx for idx, _ in resultados]:
                        # Exibe as opções de atualização ou remoção
                        escolha = input("Deseja (1) Atualizar ou (2) Remover este exercício? (3 para sair): ")
                        if escolha == '1':
                            atualizar_exercicio(index_selecionado, exercicios)
                        elif escolha == '2':
                            remover_exercicio(index_selecionado, exercicios)
                        else:
                            input("Saindo da busca.")
                    else:
                        input("Índice inválido.")
                except ValueError:
                    input("Entrada inválida. Por favor, insira um número de índice.")
            else:
                input("Nenhum exercício encontrado com o termo informado.")
                
    except FileNotFoundError:
        input("Nenhum exercício cadastrado.")
    except json.JSONDecodeError:
        input("Erro ao carregar dados.")
    exercicios_menu()
    

def atualizar_exercicio(indice, exercicios):
    clear()
    cabecalho_exercicios()
    print("===      Atualizar Exercício       ===")
    novo_nome = input("==  Novo nome do exercício (ou Enter para manter): \n\n>>>>    ").strip()
    novo_tipo = input("==  Novo tipo do exercício (ou Enter para manter): \n\n>>>>    ").strip()

    if novo_nome:
        exercicios[indice]['nome'] = novo_nome
    if novo_tipo:
        exercicios[indice]['tipo'] = novo_tipo

    with open('data/exercicios.json', 'w', encoding='utf-8') as arq:
        json.dump(exercicios, arq, indent=4)
    print("Exercício atualizado com sucesso!")

def remover_exercicio(indice, exercicios):
    clear()
    cabecalho_exercicios()
    print("===      Remover Exercício         ===")
    confirmacao = input("Tem certeza de que deseja remover este exercício? (s/n): ").strip().lower()
    
    if confirmacao == 's':
        exercicios.pop(indice)
        with open('data/exercicios.json', 'w', encoding='utf-8') as arq:
            json.dump(exercicios, arq, indent=4)
        print("Exercício removido com sucesso!")
    else:
        print("Remoção cancelada.")