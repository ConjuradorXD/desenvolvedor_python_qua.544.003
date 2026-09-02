1 - criar uma nova pasta com o nome: 06_estrutura_decisao_01.
2 - novo arquivo chamado: main.py.
3 - esse programa serve para verificar se o usuário é maior ou menor de idade.
4 - Condições, se a ação for atendida ou não.
5 - isso só funciona se tiver um int, pois em string não funciona.
6 - identação, é necessário para fazer com que o comando funcione, manualmente apertando o tab, ou 4 vezes o espaço.

if = se for ou tiver.
else = se não for ou não tiver

-------

ficando assim o código:

- Declaração de variáveis

nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))

- Estrutura de decisões

if idade >= 18:
    print(f"{nome} é maior de idade.")
    
else:
    print(f"{nome} é menor de idade.")
    
