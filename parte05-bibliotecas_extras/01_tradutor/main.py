from deep_translator import GoogleTranslator

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def traduzir(texto):
    tradutor = GoogleTranslator(source="auto",target="pt")
    return tradutor.translate(texto)

limpar()

def main():
    while True:
        print("--------Tradutor--------")
        print("")
        print("1 - Traduzir texto para o português.")
        print("2 - Sair do programa.")
        print("")
        opcao = input("Inform a opção desejada: ").strip()

        limpar()

        if opcao == "1":
            try:
                texto = input("Informe o texto a ser traduzido: ")
                limpar()
                print("Texto traduzido:\n----------------------")
                texto_traduzido = traduzir(texto)
                print(texto_traduzido)
                print("----------------------\n")
            except Exception as e:
                print(f"Não foi possivel traduzir.")
                continue

        elif opcao == "2":
            break

        else:
            print("Opção inválida.")



if __name__ == "__main__":
    main()