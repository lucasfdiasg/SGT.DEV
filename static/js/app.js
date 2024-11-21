const loginForm = document.getElementById('loginForm');
const errorMessage = document.getElementById('errorMessage');

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();  // Evita o envio do formulário tradicional

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;
    const tipoUsuario = document.getElementById('tipoUsuario').value;

    // Valida o tipo de usuário
    if (!tipoUsuario) {
        errorMessage.innerText = 'Selecione o tipo de usuário.';
        return;
    }

    if (tipoUsuario !== 'administrador') {
        errorMessage.innerText = 'Apenas administradores podem acessar o sistema.';
        return;
    }

    // Envia a requisição para a API de login
    const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ usuario, senha })  // Envia os dados do login
    });

    const result = await response.json();  // Processa a resposta JSON do backend

    // Se o login for bem-sucedido, redireciona para o menu
    if (result.success) {
        window.location.href = '/menu';
    } else {
        errorMessage.innerText = result.message || 'Credenciais inválidas.';
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const cadastroForm = document.getElementById('cadastroExercicioForm');
    const successMessage = document.getElementById('successMessage');
    const successText = document.getElementById('successText');
    const cadastrarNovoBtn = document.getElementById('cadastrarNovoBtn');
    const voltarMenuBtn = document.getElementById('voltarMenuBtn');
    const errorMessage = document.getElementById('errorMessage');
    const errorText = document.getElementById('errorText');
    const voltarBtnContainer = document.getElementById('voltarBtnContainer');

    // Lida com o envio do formulário
    cadastroForm.addEventListener('submit', async (e) => {
        e.preventDefault(); // Impede o envio tradicional do formulário

        const nome = document.getElementById('nome').value;
        const tipo = document.getElementById('tipo').value;

        if (!nome || !tipo) {
            errorMessage.style.display = 'block';
            errorText.innerText = 'Por favor, preencha todos os campos!';
            return;
        }

        const exercicio = { nome: nome, tipo: tipo };

        // Envia os dados para o servidor (API)
        const response = await fetch('/api/cadastrar-exercicio', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(exercicio)
        });

        const result = await response.json();

        if (result.success) {
            successMessage.style.display = 'block'; // Exibe a mensagem de sucesso
            successText.innerText = result.message;

            // Exibe o botão de cadastrar novo ou voltar ao menu
            cadastrarNovoBtn.addEventListener('click', () => {
                window.location.href = '/cadastrar-exercicio'; // Redireciona para cadastrar outro exercício
            });

            voltarMenuBtn.addEventListener('click', () => {
                window.location.href = '/exercicios'; // Redireciona para a página de exercícios
            });
        } else {
            errorMessage.style.display = 'block';
            errorText.innerText = result.message || 'Erro ao cadastrar exercício.';
        }
    });
});
