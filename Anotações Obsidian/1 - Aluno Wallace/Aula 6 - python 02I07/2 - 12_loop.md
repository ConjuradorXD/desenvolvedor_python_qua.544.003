1 - criar uma nova pasta com o nome: 12_loop.
2 - novo arquivo chamado: main.py.
3 - Loop é quando a gente pede para um programa rodar depois que terminar varias vezes.
4 - Nesse programa, o usuário vai informar a quantidade de vezes que o print vai rodar com um número com uma contagem regressiva. 
5 - o comando: try: , vai fazer com que o usuário não informe errado o número. 
6 - o comando: while , quando for verdadeiro, ele vai continuar o loop, ele faz com que sempre que o numero for informado ele volte para o comando: ex: se for colocado o numero 10, sempre for 10 ele vai continuar rodando até que seja especificado um numero para o loop parar, sem isso ele vai ficar em loop infinito e pode ser perigoso.
7 - decremento, é um comando que usa para o valor da variável seja diminuído. ex: n -= 1
8 - 

--------
- tratamento de exceção

try:
    # Usuario informa número inteiro
    n = int(input("Informe um número inteiro "))
    
    # Laço de repetição
    while n >= 0:
        print(n)
        n -= 1
except:
    print("Não foi possível exibir a contagem.")