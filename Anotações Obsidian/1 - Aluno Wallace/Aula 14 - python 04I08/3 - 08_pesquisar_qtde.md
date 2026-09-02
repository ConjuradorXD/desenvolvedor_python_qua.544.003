1 - criar uma nova pasta com o nome: 08_pesquisar_qtde.
2 - dentro dela o arquivo main.py
3 - Esse programa serve para contar quantas vezes o item na lista aparece repetido.
4 - O usuário vai informar o nome do pais, e o programa vai devolver a quantidade de vezes que o nome aparece na lista.
5 - O comando: .count() serve para mostrar a quantidade de vezes, ficando assim:

```python

qtde = paises.count(pais)

```

6 - ficando assim o programa:

```python
paises = [

    "Brasil",
    "Estados Unidos",
    "México",
    "Argentina",
    "Brasil",
    "Argentina",
    "Arábia Saudita",
    "Irã",
    "Brasil",
    "México",
    "Estados Unidos",
    "Brasil"
]

pais = input("Informe o país a ser pesquisado: ").strip().tilte()

# Armazena a quantidade de ocorrências na lista

qtde = paises.count(pais)
  
print(f"{pais} foi encontrado {qtde} vezes na lista.")

```