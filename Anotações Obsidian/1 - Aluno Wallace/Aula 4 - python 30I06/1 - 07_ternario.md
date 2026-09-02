1 - criar uma nova pasta com o nome: 07_ternario.
2 - novo arquivo chamado: main.py.
3 - operador ternário, é a mesma coisa do if e else mas é simplificado, serve para deixar mais otimizado e fica mais elegante o código.
4 - vamos usar o mesmo exemplo do ultimo programa com nome e idade:

-----

- Declaração de variáveis

nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))

- Saída de dados com operador ternário:

print(f"{nome} é maior de idade," if idade >= 18 else f"{nome} é menor de idade.")

