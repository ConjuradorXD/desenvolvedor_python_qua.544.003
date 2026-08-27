# lista de dicionários:

usuarios = [
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulanodetal@outlook.com"
    
    },
    {
        'nome': "Cicrano",
        'idade': 128,
        'email': "cicranodasilvarocha@gmail.com"

    },
    {
        'nome': "Beltrany",
        'idade': 744,
        'email': "beltranyholmes@live.com"
    }
]

# Percorre a lita de dicionários:
for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")

