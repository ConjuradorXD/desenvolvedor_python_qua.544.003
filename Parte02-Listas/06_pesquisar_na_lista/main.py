cidade = [
    "Brasília"
    "Rio de janeiro"
    "Manaus"
    "Fortaleza"
    "Florianopolis"
]

# Informa o nome da cidade a ser pesquisada
cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

# retorna resultado
print(f"{cidade_pesquisada} encontrada." if cidade_pesquisada in cidade_pesquisada else f"Cidade não encontrada.")