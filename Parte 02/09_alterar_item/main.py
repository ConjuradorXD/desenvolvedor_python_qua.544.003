import os

os.system("cls" if os.name == "nt" else "clear")

#Alterar nomes
nomes = [
    "Fulano",
    "Cicrano",
    "Beltrano",
    "Juliano",
    "Juleide",
    "Jasildy",
]

print("Nomes disponiveis:")
print("")
print("------------------")
print("")
for nome in nomes:
        print(nome)
print("")
print("------------------")
print("")
# O usuário informa o nome que deseja alterar:
nome_antigo = input("Informe o nome que deseja alterar: ").strip().title()

# Armazena a posição do nome na lista caso exista:
if nome_antigo in nomes:
    indice = nomes.index(nome_antigo)
    nomes[indice] = input("Informe o novo nome: ").strip().title()
    os.system("cls" if os.name == "nt" else "clear")
    print("Nome alterado com sucesso!")
    print("")
    print("------------------")
    print("")
    for nome in nomes:
        print(nome)
else:
    print("Nme não encontrado.")