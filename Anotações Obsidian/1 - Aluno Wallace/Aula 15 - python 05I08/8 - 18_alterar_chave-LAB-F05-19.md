1 - criar uma nova pasta com o nome: 18_alterar_chave.
2 - dentro dela o arquivo main.py
3 - vamos copiar o dicionário do programa anterior:
4 - comando cls serve para limpar o terminal.
5 - em vez de inserir uma chave nova, vai alterar uma chave já existente,
6 - Nesse programa o usuário vai informar uma chave para ser alterada.
7 - O comando .lower() serve para deixar a letra inicial minúscula, pois como o usuário vai alterar uma chave no programa, se a chave for maiúscula pode dar erro.
Ficando assim:

```python

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

```

