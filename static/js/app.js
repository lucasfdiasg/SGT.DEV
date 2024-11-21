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
