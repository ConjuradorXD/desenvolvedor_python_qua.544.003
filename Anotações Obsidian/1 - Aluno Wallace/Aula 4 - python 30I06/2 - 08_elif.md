1 - criar uma nova pasta com o nome: 08_elif.
2 - novo arquivo chamado: main.py.
3 - objetivo do aplicativo: o cliente quer um programa com o nome e a nota do aluno de 0 a 10, precisa saber se o aluno está aprovado, reprovado ou de recuperação.
4 - elif é implementado dentro do if e else para declarar mais uma saída ou condição.
5 - pass serve para ignorar o bloco de programação para não dar erro.
6 - Péssima pratica colocar muitos elifs.
6 - operador poliano:

- and: precisa de 2 saídas verdadeiras para retornar.
- or: precisa de 1 das saídas verdadeiras para retornar.
- not: precisa ter 1 negativa.

-----

- declaração de variáveis

nome = input("Informe o nome do aluno: ").title()
nota = float(input("Informe a nota do aluno: ").replace(",","."))

- Verificação se a nota é valida:

if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} está aprovado.")
    elif nota >= 5:
        print(f"{nome} está de recuperação.")
    else:
        print(f"{nome} está reprovado.")

else:
    print(f"Nota de {nome} Invalida.")

