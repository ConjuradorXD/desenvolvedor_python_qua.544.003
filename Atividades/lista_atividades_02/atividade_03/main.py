# TODO: Atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
# O programa deve calcular a média do aluno e informar se o aluno está aprovado (média minima = 7) ou reprovado.
# O pgrama deve gravar esses dados em um JSON.
# Ao final, o usuário deverá escolher se deseja inserir as notas de outro aluno, que deverão ser gravadas no mesmo arquivo JSON.

import os
import json

os.system("cls" if os.name == "nt" else "clear")

alunos = []

alunos = {
    'nome': "fulano",
    'nota1': "0",
    'nota2': "0",
    'nota3': "0",
    'resultado': "0",
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
                aluno = {}
                notas = [0,0,0]

                aluno['nome'] = input("Informe a nome do aluno: ").strip().title()
                for i in range(len(notas)):
                    notas[1] = float(input(f"Informe a (i+1)ª nota: ").replace(",","."))

                aluno['notas'] = notas
                aluno['média'] = sum(notas)/len(notas)
                aluno['resultado'] = "aprovado" if aluno['media'] >= 7 else "reprovado"
                alunos.append(aluno)

                with open("atividade_03/arquivo.json","w")encoding="utf-8") as f:
                    json.dump(alunos, f)

                print("Dados do aluno gravados com sucesso")
                continue
        
            case "2":
                break
            case _:
              print("Opção Inválida.")
              continue

                
