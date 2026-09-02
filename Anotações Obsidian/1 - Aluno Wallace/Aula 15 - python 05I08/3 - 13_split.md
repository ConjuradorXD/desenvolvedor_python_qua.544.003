1 - criar uma nova pasta com o nome: 13_split.
2 - dentro dela o arquivo main.py
3 - o comando .split() é o contrario do comando .join(), agora vamos pegar uma variável e separar em uma lista, para isso vamos precisar de uma variável, vamos chamar ela de localidade e depois criar outra variável chamada lista e depois usar o comando .split() assim:

```python
# Variável:
localidade = "Brasília - DF"

# Separa os valores em uma lista:
lista = localidade.split(" - ")

# Exibe a lista
for item in lista:
    print(item)
```
