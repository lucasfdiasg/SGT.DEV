import json

exercicios = []

opcoes = {
    "1": "Cadastrar Exercício",
    "2": "Listar Exercícios",
    "3": "Buscar Exercício",
    "4": "Atualizar Exercício",
    "5": "Remover Exercício",
    "6": "Resumo de Exercícios",
    "7": "Salvar Dados",
    "8": "Carregar Dados",
    "9": "Sair"
}

def base():
    print("\nOpções:")
    for i, valor in opcoes.items():
        print(f"{i}. {valor}")

def cadastrar_exercicio():
    nome = input("Qual é o nome do exercício que deseja: ").strip().lower()
    for i in exercicios:
        if i["nome"] == nome:
            print("Já existe esse exercício.")
            return
        
    exercicios.append({
        'nome': nome,
        'descrição': input("Descrição: "),
        'séries': input("Séries: "),
        'repetições': input("Repetições: "),
        'categoria': input("Categoria (ex: força, cardio): ").strip().lower(),
        'equipamento': input("Equipamento necessário (ex: halteres, barra): ").strip().lower()
    })
    print("Exercício cadastrado.")

def listar_exercicios():
    if exercicios:
        for i in exercicios:
            print(f"\nNome: {i['nome'].capitalize()}")
            print(f"Descrição: {i['descrição']}")
            print(f"Séries: {i['séries']}")
            print(f"Repetições: {i['repetições']}")
            print(f"Categoria: {i['categoria'].capitalize()}")
            print(f"Equipamento: {i['equipamento'].capitalize()}")
    else:
        print("Não há nenhum exercício cadastrado.")

def buscar_exercicio():
    nome = input("Nome do exercício: ").strip().lower()
    for i in exercicios:
        if i["nome"] == nome:
            print(f"\nNome: {i['nome'].capitalize()}")
            print(f"Descrição: {i['descrição']}")
            print(f"Séries: {i['séries']}")
            print(f"Repetições: {i['repetições']}")
            print(f"Categoria: {i['categoria'].capitalize()}")
            print(f"Equipamento: {i['equipamento'].capitalize()}")
            return
    print("Exercício não encontrado.")

def atualizar_exercicio():
    nome = input("Nome do exercício: ").strip().lower()
    for i in exercicios:
        if i["nome"] == nome:
            i["descrição"] = input("Nova descrição: ")
            i["séries"] = input("Novas séries: ")
            i["repetições"] = input("Novas repetições: ")
            i["categoria"] = input("Nova categoria: ")
            i["equipamento"] = input("Novo equipamento: ")
            print("Exercício atualizado.")
            return
    print("Exercício não encontrado.")

def remover_exercicio():
    nome = input("Nome do exercício: ").strip().lower()
    for indice, i in enumerate(exercicios):
        if i["nome"] == nome:
            del exercicios[indice]
            print("Exercício removido.")
            return
    print("Exercício não encontrado.")

def resumo_exercicios():
    if exercicios:
        print("\n--- Resumo dos Exercícios Cadastrados ---")
        total = len(exercicios)
        print(f"Total de Exercícios: {total}")
        categorias = set(i['categoria'] for i in exercicios)
        for categoria in categorias:
            contagem = sum(1 for i in exercicios if i['categoria'] == categoria)
            print(f"Categoria '{categoria.capitalize()}': {contagem} exercícios")
    else:
        print("Não há nenhum exercício cadastrado.")

def salvar_dados():
    with open("exercicios.json", "w") as file:
        json.dump(exercicios, file)
    print("Dados salvos com sucesso.")

def carregar_dados():
    try:
        with open("exercicios.json", "r") as file:
            global exercicios
            exercicios = json.load(file)
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Nenhum dado salvo encontrado.")

# Menu principal
while True:
    base()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_exercicio()
    elif opcao == "2":
        listar_exercicios()
    elif opcao == "3":
        buscar_exercicio()
    elif opcao == "4":
        atualizar_exercicio()
    elif opcao == "5":
        remover_exercicio()
    elif opcao == "6":
        resumo_exercicios()
    elif opcao == "7":
        salvar_dados()
    elif opcao == "8":
        carregar_dados()
    elif opcao == "9":
        break
    else:
        print("Opção inválida.")

#### 29/10/2024
#1.0