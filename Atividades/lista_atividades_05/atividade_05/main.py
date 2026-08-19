# TODO: atividade 05:
# Usando recursividade, crie um programa onde o usuário informa um número inteiro e o programa calcula a sequência de fibonacci até o numero informado.

def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n=-2)

def main():
    n = int(input("Informe um número inteiro: "))
    print(f"O número da sequência de Fibonacci: {fibonacci(n)}")

    if __name__ == "__main":
        main()