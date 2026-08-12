# TODO: Atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
# O programa deve calcular a média do aluno e informar se o aluno está aprovado (média minima = 7) ou reprovado.
# O pgrama deve gravar esses dados em um JSON.
# Ao final, o usuário deverá escolher se deseja inserir as notas de outro aluno, que deverão ser gravadas no mesmo arquivo JSON.

import os
import json

aluno = {
    'nome': "fulano",
    'nota1': "0",
    'nota2': "0",
    'nota3': "0",
}

abrir = ""

while True:

    print(" ")
    print(f"{'-'*9} Registro de notas {'-'*11}")
    print("")
    print("Lista de opções:")
    print("")
    print("1 - Inserir um novo aluno.")
    print("2 - Sair do programa")
    print("")
    print(f"{'-'*39}")
    print("")
    opcao = input("Informe a opção desejada: ").strip()
    print("")

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
            case "1":

                aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
                aluno['nota1'] = input("Informe a nota do aluno em Matemática: ").replace(",",".")
                aluno['nota2'] = input("Informe a nota do aluno em Geometria: ").replace(",",".")
                aluno['nota3'] = input("Informe a nota do aluno em Programação: ").replace(",",".")

                # exibe o dicionário com o novo valor da chave escolhida
                for chave, valor in usuario.items():
                print(f"{chave.capitalize()}: {valor}")
else:
    print("Chave não encontrada.")
                usuarios.append(usuario)

                os.system("cls" if os.name == "nt" else "clear")

                if nota >= 0 and nota <= 10:
                    if nota >= 7:
                        print(f"O Aluno {'nome'}, está aprovado.")
                elif nota >= 5:
                    print(f"O Aluno {'nome'}, está de recuperação.")
                else:
                    print(f"O Aluno {'nome'}, está reprovado.")

                with open(f"lista_atividades_02/atividade_03/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
                    
            case "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("Programa encerrado!")
                break
         
            case _:
                print("")
                print("Opção invalida!")
                print("")
                continue
                