1 - criar uma nova pasta com o nome: 19_lista_de_dicionarios.
2 - dentro dela o arquivo main.py
3 - uma lista de dicionários, cada item dessa lista vai ser um dicionário. separado por [ { } ]

```python
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

```

4 - Para percorrer a lista de dicionários:

5 - Como cada item dessa lista é uma item, então para percorrer ela precisamos colocar um laço for dentro de outro laço for e separar por print.

```python
# Percorre a lita de dicionários:
for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.captalize()}: {valor}")
    print(f"{'-'+40}")

```

