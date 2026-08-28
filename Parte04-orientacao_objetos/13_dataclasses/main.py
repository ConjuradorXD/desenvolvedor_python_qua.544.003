import os

from models import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa(nome="",idade=0,altura=0.0)

    limpar()

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int("Informe a idade: ")
    usuario.nome = input("Informe o nome: ").replace(",",".")

    limpar()

    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade} anos.")
    print(f"Altura: {usuario.altura}")

if __name__ == "__main__":
    main()