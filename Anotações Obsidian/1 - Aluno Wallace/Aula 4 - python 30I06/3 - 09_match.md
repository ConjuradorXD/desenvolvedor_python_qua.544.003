1 - criar uma nova pasta com o nome: 09_match.
2 - novo arquivo chamado: main.py.
3 - objetivo do aplicativo: o mesmo cliente do 08, criar uma mini calculadora básica, o usuário vai informar 2 números e ele vai escolher algumas opções.
4 - comando .strip(), serve para eliminar espaços de sobra antes ou depois de um comando resposta do usuário. 
5 - o usuário vai informar o numero de x:
6 - quando tem muitas opções, usar match para string,

-----

- declaração de variáveis

x = float(input("Informe o valor de x: ").replace(",","."))
y = float(input("Informe o valor de y: ").replace(",","."))

- menu

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Informe a opção desejada: ").strip()
match opcao:
    case "1":
        print(f"A soma é {x+y}.")
    case "2":
        print(f"A Subtração é {x-y}.")
    case "3":
        print(f"A Multiplicação é {x*y}.")
    case "4":
        print(f"A Divisão é {x/y}.")
    case _:
        print("Opção Inválida.")