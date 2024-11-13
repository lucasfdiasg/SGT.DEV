import json

from modules.geral import exibir_menu_um, clear_terminal, menu_login, verificar_login

# from modules.exercicio import 
clear_terminal()
def main():
    while True:
        opcao = exibir_menu_um()

        if opcao == '1':
            tipo_usuario, usuario, senha = menu_login()
            if verificar_login(tipo_usuario, usuario, senha):
                print("Login bem-sucedido!")
            else:
                print("Nome de usuário ou senha incorretos")
        elif opcao == '2':
            clear_terminal()
            print('''\
====================================
===                              ===
=== O Sistema está encerrando... ===
===                              ===
====================================                  
''')
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
