1 - criar uma nova pasta com o nome: 14_importacao_os.
2 - novo arquivo chamado: main.py.
3 - Nesse programa vamos criar uma contagem regressiva, depois do usuário informar um numero, vai iniciar uma contagem numérica.
4 - Quando o programa for executado, e o usuário digitar um numero, o
5 - vamos precisar importar duas bibliotecas, os , time.
6 - tratamento de exceção, colocar junto de except Exception, a vantagem de colocar esse comando e que aparece uma mensagem junto do erro e mostra exatamente o erro que deu;

------

- Importação de bibliotecas
import os
import time

- tratamento de exceção
try:
    # Entrada de dados:
    n = int(input("Informe um número inteiro:"))

    # limpa a tela
    os.system("cls" if os.name == "nt" else "clear")

    # contagem
    while n >= 0:
        print(f"{n} ...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        n -= 1
  
    print("EXPLODIU!🤑")

except Exception as e:
    print(f"Não foi possível iniciar a contagem. {e}.")