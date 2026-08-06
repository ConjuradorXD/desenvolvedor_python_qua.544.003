# Deletar itens:

nomes = [
    "Fulano",
    "Cicrano",
    "Beltrano",
    "Juliano",
    "Juleide",
    "Jasildy",
]

nome = input("Informe o nome a ser deletado: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)

    # Apaga item da lista:
    del(nomes[indice])

    #Exibe a nova lista sem o item deletado
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrando.")