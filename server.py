import os
from flask import Flask, json, render_template, request, jsonify
import csv

app = Flask(__name__)

# Página de Login
@app.route('/')
def login_page():
    return render_template('login.html')

# Página do Menu
@app.route('/menu')
def menu_page():
    return render_template('menu.html')

# Página de Exercícios
@app.route('/exercicios')
def exercicios_page():
    return render_template('exercicios.html')

@app.route('/cadastrar-exercicio')
def cadastro_exercicio():
    print("Rota /cadastrar-exercicio acessada!")  # Adicionando um log para depuração
    return render_template('cadastro_exercicio.html')



# API para login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('usuario')
    senha = data.get('senha')

    # Lê o arquivo administradores.csv para validar o login
    try:
        with open('data/administrador.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)  # Pula o cabeçalho
            for row in csv_reader:
                nome_usuario, senha_usuario = row
                # Verifica se o nome de usuário e a senha batem
                if nome_usuario == usuario and senha_usuario == senha:
                    return jsonify({"success": True})

        # Se não encontrar o usuário ou senha correspondentes
        return jsonify({"success": False, "message": "Credenciais inválidas"})
    
    except FileNotFoundError:
        return jsonify({"success": False, "message": "Arquivo administrador.csv não encontrado"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Erro ao processar o arquivo: {str(e)}"})

import os
import json
from flask import Flask, request, jsonify

@app.route('/api/cadastrar-exercicio', methods=['POST'])
def cadastrar_exercicio():
    data = request.json
    nome = data.get('nome')
    tipo = data.get('tipo')

    # Verificação de campos obrigatórios
    if not nome or not tipo:
        return jsonify({'success': False, 'message': 'Nome e tipo do exercício são obrigatórios!'})

    # Normalizando o nome do exercício (para não ser sensível a maiúsculas/minúsculas)
    nome_normalizado = nome.strip().lower()

    try:
        # Verifica se o arquivo 'exercicios.json' já existe
        exercicios_path = 'SGT.DEV/data/exercicios.json'
        if os.path.exists(exercicios_path):
            with open(exercicios_path, 'r+', encoding='utf-8') as arq:
                try:
                    exercicios = json.load(arq)
                except json.JSONDecodeError:
                    exercicios = []

                # Verifica se o exercício já existe
                nomes_existentes = [ex['nome'].lower() for ex in exercicios]
                if nome_normalizado in nomes_existentes:
                    return jsonify({'success': False, 'message': 'Exercício já está cadastrado! Não é possível duplicar.'})

                # Adiciona o novo exercício ao arquivo
                exercicios.append({"nome": nome, "tipo": tipo})
                arq.seek(0)  # Volta para o início do arquivo
                json.dump(exercicios, arq, indent=4)

        else:
            # Caso o arquivo não exista, cria um novo com o exercício
            with open(exercicios_path, 'w', encoding='utf-8') as arq:
                json.dump([{"nome": nome, "tipo": tipo}], arq, indent=4)

        return jsonify({'success': True, 'message': 'Exercício cadastrado com sucesso!'})

    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao cadastrar exercício: {str(e)}'})

@app.route('/listar-exercicios')
def listar_exercicios_page():
    return render_template('listar_exercicios.html')


@app.route('/api/listar-exercicios', methods=['GET'])
def listar_exercicios():
    try:
        exercicios_path = 'SGT.DEV/data/exercicios.json'
        
        if os.path.exists(exercicios_path):
            with open(exercicios_path, 'r', encoding='utf-8') as arq:
                exercicios = json.load(arq)
            return jsonify({'success': True, 'exercicios': exercicios})
        else:
            return jsonify({'success': False, 'message': 'Nenhum exercício cadastrado.'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao carregar os exercícios: {str(e)}'})



if __name__ == '__main__':
    app.run(debug=True)
