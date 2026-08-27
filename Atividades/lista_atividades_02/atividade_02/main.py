# TODO: Atividade 02 

"""Crie um programa que recebe uma vez o nome e a idade do usuario, em seguida, mostre os filmes em idade do usuario, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
# - filme 1 (livre)
# - filme 2 ( 12 anos)
# - filme 3 ( 16 anos)
# - filme 4 ( 18 anos)
# O usuario ira escolher a sala onde o filme desejado está passando, caso o usario não tenha idade, o programa impede sua entrada e re exibe a lista para o mesmo possa escolher outro filme.
# caso o usuario tenha idade minima, o programa grava em um arquivo o bilhete do filme e encerra o programa.
"""

# importa biblioteca
import os

# limpa tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

# entrada de dados
nome = input("Digite seu nome: ").strip()
idade = int(input("Digite sua idade: "))

os.system('cls' if os.name == 'nt' else 'clear')

# inicia loop infinito
while True:
    # exibe as salas e os filmes
    print(f"\n{'-'*20}CINE COBRA{'-'*20}\n")
    print("Sala 1 - A Volta dos Que Não Foram (livre)")
    print("Sala 2 - A Roda Quadrada (12 anos)")
    print("Sala 3 - As Tranças do Rei Careca (14 anos)")
    print("Sala 4 - Poeira em Alto Mar (16 anos)")
    print("Sala 5 - A Vingança do Frango Assado (18 anos)")

    # recebe do usuário a sala desejada
    sala = input("Escolha a sala do filme desejado (1-5): ").strip()

    os.system('cls' if os.name == 'nt' else 'clear')

    # verifica a sala informada, atribui a idade mínima e o filme
    match sala:
        case "1":
            idade_minima = 0
            filme = "A Volta dos Que Não Foram"
        case "2":
            idade_minima = 12
            filme = "A Roda Quadrada"
        case "3":
            idade_minima = 14
            filme = "As Tranças do Rei Careca"
        case "4":
            idade_minima = 16
            filme = "Poeira em Alto Mar"
        case "5":
            idade_minima = 18
            filme = "A Vingança do Frango Assado"
        case _:
            # caso a sala informada não exista
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sala inexistente. Escolha outra sala.")
            continue

    os.system('cls' if os.name == 'nt' else 'clear')

    # verifica se o usuário tem a idade mínima
    if idade < idade_minima:
        # proibe a entrada do usuário
        print(f"{nome}, você não tem idade suficiente para assistir '{filme}'.")
        print("Por favor, escolha outro filme.")

        # reinicia o loop
        continue
    else:
        # imprime a mensagem de sucesso
        print("Ingresso comprado com sucesso! Tenha um bom filme!")

        # grava o ingresso em arquivo
        ingresso = f"🎫 Ingresso comprado para: {nome}\n🎞️ Filme: {filme}\n😎 Tenha um bom filme!"
        with open("PROGRAMA_01-02/Bilhetes/ingresso.txt", "w", encoding="utf-8") as f:
            f.write(ingresso)
        
        # encerra o loop
        break


