1 - criar uma nova pasta com o nome: 14_importacao_os.
2 - novo arquivo chamado: main.py.
3 - As bibliotecas são pastas que já vem no python ou não, e você precisa chamar elas com o import, existem 3 tipos de importações que podem ser feitas:

- Importações que já existem dentro do python, mas não estão disponíveis de cara. 
- Importações que são de terceiros e não são nativos no python, precisamos baixar no pc e instalar no nosso código.
- Importações que a gente pode desenvolver para nosso próprio projeto.

5 - vamos criar um programa básico criando um lapso de loop, a diferença e que dessa vez, a cada vez que a gente inserir os novos dados o programa vai limpar os dados do terminal.

6 - comando: import os , é o comando usado para fazer com que o terminal seja limpo depois de usar o programa.
7 - Atalho: shit alt + [seta pra baixo] - duplica a linha do código para baixo ou pra cima.
8 - Atalho: alt + [seta pra baixo] - move a linha do código para baixo ou para cima.
9 - Atalho: ctrl + [+] - tira e coloca zoom.
10 - Atalho Windows + [.] - para aparecer emojis de texto.
10 - Esse comando serve para fazer com que a tela do terminal seja limpa:

os.system("cls" if os.name == "nt" else "clear")

Mas para ele funcionar precisa do import os

------

- importação da biblioteca

import os

  - laço de repetição
while True:
    os.system("cls" if os.name == "nt" else "clear")

    # entrada de dados
    nome = input("Informe o nome: ").strip().title()
    idade = int(input("Informe a idade: "))
    cpf = input("informe o CPF: ").strip()
    email = input("informe o e-mail: ").strip().lower()
  
    os.system("cls" if os.name == "nt" else "clear")

    # saída de dados
    print(f"Nome: {nome}.")
    print(f"Idade: {idade}.")
    print(f"CPF: {cpf}.")
    print(f"E-mail: {email}.")

    # menu
    print("1 - Informar dados de outro usúario")
    print("2 - Sair do programa")

    opcao = input("Informe a opcao desejada: ").strip()

    match opcao:
        case "1":
            continue
        case "2":
            break
        case _:
            print("opção Inválida.")
