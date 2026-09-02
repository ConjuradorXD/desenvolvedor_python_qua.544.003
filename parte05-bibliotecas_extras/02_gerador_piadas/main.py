import pyjokes
from deep_translator import GoogleTranslator

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_piada():
    tradutor = GoogleTranslator(source="auto", target="pt")
    piada = pyjokes.get_joke()
    return tradutor.translate(piada)


def main():
    limpar()
    while True:
        print("1 - Gerar nova piada.")
        print("2 - Sair do Programa.")
        opcao = input("Informe a opção desejada: ").strip()

        if opcao == "1":
            nova_piada = gerar_piada()
            print(nova_piada)
            continue
    
        elif opcao == "2":
            break


if __name__ == "__main__":
    main()