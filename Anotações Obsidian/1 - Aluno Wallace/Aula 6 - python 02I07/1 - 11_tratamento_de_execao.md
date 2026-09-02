1 - abrir a pasta: desenvolvedor_python_qua.544.003/Parte01-Logica_de_programacao.
2 - criar uma nova pasta com o nome: 11_tratamento_de_execao.
3 - novo arquivo chamado: main.py.
4 - Esse programa vai servir para o usuário informar um numero inteiro,
5 - tratamento de exceção, é como o if e else, mas diferente, ele entra no primeiro bloco sempre, se algo acontecer no primeiro bloco, ele segue para o próximo bloco.
6 - sempre colocar o comando try: antes do código, o comando try vai ser sempre acompanhado do comando except:
7 - o comando expept: , serve para colocar a exceção se aquilo não aparecer.
8 - TODO = TIUDU, significa código para fazer, sempre acompanhado do comando: pass , significa que vai ser apagado depois para ser feito um código no mesmo lugar.

-------

- Tratamento de exceção
try:
    n = int(input("Informe um número inteiro: "))
    print(f"Número informado: (n).")
except:
    print("Código não pôde ser executado.")
