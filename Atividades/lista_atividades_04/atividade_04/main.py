
from modulo import limpar,potencia,raiz,volume_cubico,volume_cilindro

# 1 - Limpa o terminal:

def main():

 while True:
    limpar()
    print("")
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
          # 2 - Calcula a poténcia de um número informado pelo usuário elevado outro número informado pelo usúario.
          limpar()
          print("")
          x = int(input("Informe o valor de X: ").replace(",","."))
          y = int(input("Informe o valor de Y: ").replace(",","."))
          limpar()
          print("")
          print(f"{'-'*14} Resultado: {'-'*14}")
          print("")
          print(f"{x} elevado a {y} = {potencia(x , y)}")
          print("")
          print("")
          print("1 - Deseja fazer outra operação?.")
          print("2 - Sair do programa.")
          print("")
          print(f"{'-'*39}")
          print("")
          opcao = input("Informe sua opção: ").strip()

          match opcao:
            case "1":
              continue
            case "2":
              break
            case _:
              print("Opção inválida.")
              continue

        case "2":
          # 3 - Calcula a raiz quadrada de um número inforamdo pelo usuário.
          limpar()
          x = int(input("Informe um número inteiro: ").replace(",","."))
          limpar()
          print("")
          print(f"{'-'*14} Resultado: {'-'*14}")
          print("")
          print(f"Raiz quadrada de {x} = {raiz(x)}")
          print("")
          print("")
          print("1 - Deseja fazer outra operação?.")
          print("2 - Sair do programa.")
          print("")
          print(f"{'-'*39}")
          print("")
          opcao = input("Informe sua opção: ").strip()

          match opcao:
            case "1":
              continue
            case "2":
              break
            case _:
              print("Opção inválida.")
              continue

        case "3":
          limpar()
          print("")
          b = int(input("Informe o valor da Base: ").replace(",","."))
          l = int(input("Informe o valor da Largura: ").replace(",","."))
          h = int(input("Informe o valor da altura: ").replace(",","."))
          
          limpar()
          print("")
          print(f"{'-'*14} Resultado: {'-'*14}")
          print("")
          print(f"(Volume cúbico é {volume_cubico})")
          print("")
          print("")
          print("1 - Deseja fazer outra operação?.")
          print("2 - Sair do programa.")
          print("")
          print(f"{'-'*39}")
          print("")
          opcao = input("Informe sua opção: ").strip()

          match opcao:
            case "1":
              continue
            case "2":
              break
            case _:
              print("Opção inválida.")
              continue
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