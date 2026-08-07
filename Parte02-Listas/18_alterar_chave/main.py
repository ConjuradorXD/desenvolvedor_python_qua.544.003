# Alterar chave:

import os
os.system("cls" if os.name == "nt" else "clear")

usuario = {
    'nome': "Fulano",
    'idade': 35,
    'email': "fulanodetal@gmail.com",
    'cpf': "123,456,789-12",
    }

# Alterando a chave escolhida pelo usuario:
chave = input("Informe o nome da chave: ").strip().lower()

if chave in usuario:
    # usario informa o novo valor para a chave

    usuario[chave] = input(f"Informe o novo valor para {chave}: ").strip()

    # Exibe o dicionário com o novo valor da chave escolhida

    print("")
    print("------------------")
    print("")
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")

else:
    print("Chave não encontrada.")

