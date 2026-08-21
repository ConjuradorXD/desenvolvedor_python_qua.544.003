# Herança

import os

from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(razao_social="",nome_fantasia="",cnpj="",email="",telefone="",endereco="")

    limpar()

    # Informa os valores do usuário:
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o cpf do usuário: ").strip()
    usuario.email = input("Informe o E-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o Telefone do usuário: ").strip()
    usuario.endereco = input("Informe o Endereço do usuário: ")

    limpar()

    # Informa os valore da empresa
    empresa.razao_social = input("Informe o nome jurírico da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail da espresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ")

    # saída de dados:
    usuario.exibir_dados()
    empresa.exibir_dados()

if __name__ == "__main__":
    main()