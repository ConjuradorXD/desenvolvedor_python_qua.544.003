# Declaração de variaveis
nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))

# Estrutura de decisões
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")