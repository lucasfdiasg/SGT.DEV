import os
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho_treino():
    print('''
==========================================
=== Sistema de Gerenciamento de Treino ===
==========================================
===            Administrador           ===
==========================================
===               Treino               ===
==========================================''')