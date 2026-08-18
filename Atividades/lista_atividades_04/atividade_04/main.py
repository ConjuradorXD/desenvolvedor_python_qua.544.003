
import os
import math

# 1 - Limpa o terminal:

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def somar(x, y):
    return x+y

def subtrair(x, y):
    return x-y

def multiplicar(x, y):
    return x*y

def dividir(x, y):
    return x/y


# 2 - Faça um programa que o usuário escolha executar uma dessas funções ou sair do programa.

limpar()

while True:
    print(" ")
    print(f"{'-'*9} Módulos: {'-'*11}")
    print("")
    print("Lista de opções:")
    print("")
    print("1 - Calcular um número elevado por outro.")
    print("2 - Calcular a raiz quadrada de um número.")
    print("3 - Calcular um valor de um recipiente paralelepípidico.")
    print("4 - Calcular um valor de um recipiente cilindrico.")
    print("5 - Sair do programa")
    print("")
    print(f"{'-'*39}")
    print("")
    opcao = input("Informe a opção desejada: ").strip()
    limpar()

    match opcao:
        case "1":
          limpar()
          x = int(input("Informe o valor de 'X': ").replace(",","."))
          y = int(input("Informe o valor de 'Y': ").replace(",","."))
          limpar()

          x = multiplicar(x,y)

          limpar()
          print(f"O valor da exponenciação é : {multiplicar(x, y)}")

        case "2":
          pass
        case "3":
          pass
        case "4":
          pass
        case "5":
          break
        case _:
          print("Opção inválida.")
          continue


#TODO: Atividade 04
# Utilizando o conceito de módulo, crie um módulo com funções que faça as seguintes ações:
# 1 - Limpa o terminal.
# 2 - Calcula a poténcia de um número informado pelo usuário elevado outro número informado pelo usúario.
# 3 - Calcula a raiz quadrada de um número inforamdo pelo usuário.
# 4 - Calcula o valor de um recipiente paralelepípidico.
# 5 - Calcula o valor de um recipiente cilindrico.
# 6 - Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa.