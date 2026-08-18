# TODO: atividade 01
"""
crie um programa que receba o nome, peso e altura do usuario e informe na tela o seu IMC o seu diagnostico com base no valor de IMC.
"""
import os
os.system("cls" if os.name == "nt" else "clear")
while True:
    print("      ")
    print("     -[Calculadora de IMC]-")
    print("---------------------------------")
    print("      ")
    nome = input("Informe seu nome: ").strip().title()
    peso = float(input("Informe seu peso (kg): ").replace(",","."))
    altura = float(input("Informe sua altura (m): ").replace(",","."))
    imc = peso / (altura ** 2)
    print("      ")
    print(f"{nome}, seu IMC é: [{imc:.2f}]")
    print("      ")
    print("---------------------------------")
    print("      ")
    print("Você deseja calcular outro IMC?")
    print("      ")
    print("[1] - Sim.")
    print("[2] - Encerrar programa.")
    print("      ")
    opcao = input("Informe a baixo: ")
    match opcao:
        case "1":
                continue
        case "2":
                print("programa encerrado.")
                break
        case _:
                print("Opção inválida, encerrando programa.")
                break
                