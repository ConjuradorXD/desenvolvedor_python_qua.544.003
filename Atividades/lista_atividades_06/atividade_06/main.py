
import os
import datetime
from datetime import date
from models import Conta

# -------------------- Classes ------------------------

# limpar terminal:
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Mostrar data formatada para pt br:
def hoje():
	return date.today().strftime("%d/%m/%y")

# Mostrar hora formatada:
def agora():
     return datetime.datetime.now().strtime("%H:%M:%S")

# -------------------- Estrutura ----------------------

def main():
    cc = Conta(titular="",cpf="",agencia="1234-5",n_conta="10123-4",saldo=0.0)

    limpar()

    print("")
    print(f"{'-'*9} Banco Tigrinho: {'-'*11}")
    print("")
    cc.titular = input("Informe o nome do titular da conta: ").strip().title()
    cc.cpf = input("Informe o CPF do titular da conta: ").strip()
    
    limpar()
    print(f"Conta criada no dia {hoje()} ás {agora()}.")

while True:
        print(f"\n{'-'*10} Opções: {'-'*10}")
        print("Lista de opções:")
        print("")
        print("1 - Consultar conta.")
        print("2 - Fazer depósito.")
        print("3 - Fazer saque.")
        print("4 - Gerar extrato.")
        print("5 - Sair do programa.")
        print(f"\n{'-'*39}")

        opcao = input("Informe a opção desejada: ").strip()

        limpar()

        match opcao:
            case "1":
                print(f"Data da consulta: {hoje()}")
                print(f"Hora da consulta: {agora()}")
                cc.consultar_conta()
                continue


# -----------------------------------

            case "2":
                valor = float(input("Informe o valor a ser depositado: R$ ").replace(",","."))
                if valor >= 0:
                    print(f"\n{'-'*10} Nota: {'-'*10}")
                    print(f"Depósito efetuado com sucesso, ás {agora} do dia {hoje}.")
                    print(f"Saldo atual: R$ {cc.fazer_deposito(valor):.2f}")
                    print(f"\n{'-'*39}")
                    print(f"Deseja fazer outra operação? ")
                    print("")
                    print("1 - Sim.")
                    print("2 - Não.")
                    print("")

                    opcao = input("Informe a opção desejada: ").strip()

                    match opcao:
                        case "1":
                                continue
                        case "2":
                                break

                else:
                    print("Depósito não pode ser efetuado.")
                    continue

 # -----------------------------------

            case "3":
                  valor = float(input("Informe o valor do saque: R$ ").replace(",","."))
                  if valor >= 0:
                    if valor <= cc.saldo:
                         print(f"Saque efetuado com sucesso ás {agora()} do dia {hoje()}.")
                         print(f"Saldo atual: R$ {cc.fazer_saque(valor):.2f}")

                  else:
                       print("Valor não pode ser sacado.")
                       continue

# -----------------------------------

            case "4":
            # Gerar extrato:
                cc.gerar_extrato()
                continue

# -----------------------------------

            case "5":
                  break
             
            case _:
                print("Opção inválida.")
                continue
             
# -----------------------------------------------------


if __name__ == "__main__":
    main()