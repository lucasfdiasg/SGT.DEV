from flask import Flask, render_template, request, jsonify
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

# Página de Cadastro de Exercício
@app.route('/cadastro-exercicio')
def cadastro_exercicio():
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

# API para Cadastrar Exercício
@app.route('/api/cadastrar-exercicio', methods=['POST'])
def cadastrar_exercicio():
    data = request.json
    nome = data.get('nome')
    tipo = data.get('tipo')

    if not nome or not tipo:
        return jsonify({'success': False, 'message': 'Nome e tipo do exercício são obrigatórios!'})

    try:
        with open('data/exercicios.json', 'r+', encoding='utf-8') as arq:
            exercicios = json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        exercicios = []

    # Adiciona o novo exercício
    exercicio = {'nome': nome, 'tipo': tipo}
    exercicios.append(exercicio)

    # Salva no arquivo
    with open('data/exercicios.json', 'w', encoding='utf-8') as arq:
        json.dump(exercicios, arq, indent=4)

    return jsonify({'success': True, 'message': 'Exercício cadastrado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
