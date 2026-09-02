1 - criar uma nova pasta com o nome: 13_while_true.
2 - novo arquivo chamado: main.py.
3 - O programa é para ser usado em um brinquedo de parque de diversão, um trem fantasma, existem algumas especificações para usar o brinquedo, não pode ser a baixo de uma altura mínima de 1,25 e 12 anos de idade, e o programa não pode ser fechado depois que foi executado antes de encerrar. apenas quando o usuário informar que o programa precisa encerrar.
4 - while true: roda em quanto o loop estiver ligado.
5 - o programa precisa verificar durante a excecução a altura e a idade com if e else.
6 - f junto da string, para mostrar duas informações juntas com variável. 

ex: print(f"Entrada de {nome} proibida.")

7 - comando: continue , faz com que interrompa o laço de repetição e retorna pro inicio.
8 - comando: break , faz com que interrompa o laço de repetição e saia do programa.

------
- tratamento de execução

while True:
        nome = input("Informe o nome: ").strip().title()
        idade = int(input("Informe a idade: "))
        altura = float(input("Informe a altura em metros: ").replace(",","."))
  
        if idade>= 12 and altura >= 1.25:
            print(f"{nome} está liberado.")
        else:
            print(f"Entrada de {nome} proibida.")
        print("1 - Passar novo pagante.")
        print("2 - Encessar programa.")

        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

except:
    print("Não foi possível registrar a entrada do pagante.")