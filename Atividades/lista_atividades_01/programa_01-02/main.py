# TODO: Atividade 02 
"""Crie um programa que recebe uma vez o nome e a idade do ususario, em seguida, mostre os filmes em idade do usuario, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
# - filme 1 (livre)
# - filme 2 ( 12 anos)
# - filme 3 ( 16 anos)
# - filme 4 ( 18 anos)
# O usuario ira escolher a sala onde o filme desejado está passando, caso o usario não tenha idade, o programa impede sua entrada e re exibe a lista para o mesmo possa escolher outro filme.
# caso o usuario tenha idade minima, o programa grava em um arquivo o bilhete do filme e encerra o programa.
"""
import os
os.system("cls" if os.name == "nt" else "clear")
while True: 
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))

    print("Filmes em cartaz hoje:")
    print("Sala [1] - Deu a louca na chapeuzinho vermelho. (Livre)")
    print("Sala [2] - A viagem de chiriho. (12 anos)")
    print("Sala [3] - Os incriveis. (16 anos)")
    print("Sala [4] - Resident Evil. (18 anos)")
    print("Desistir de assistir [5].")

    opcao = input("Informe a baixo a Sala que deseja: ")
    match opcao:
        case "1":
            idade = 12
            with open(f"programa_01-02/Bilhetes/{nome_arquivo}.txt", "w", encoding="utf-8") as f:



