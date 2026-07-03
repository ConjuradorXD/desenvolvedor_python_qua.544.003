#tratamento de exceção
try:
    # Usuario informa número inteiro
    n = int(input("Informe um número inteiro "))

    # Laço de repetição
    while n >= 0:
        print(n)
        n -= 1
except:
    print("Não foi possível exibir a contagem.")