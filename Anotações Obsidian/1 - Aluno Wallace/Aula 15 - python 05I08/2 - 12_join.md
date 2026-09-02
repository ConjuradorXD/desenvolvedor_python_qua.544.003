1 - criar uma nova pasta com o nome: 12_join.
2 - dentro dela o arquivo main.py
3 - O join no python é uma função que pega os valores da sua lista e junta numa variavel.
4 - a barra de espaço vai ser o separador, então vamos criar uma variavel com nome separar = " "
5 - o comando .join(nomes) serve para juntar ficando assim:

```python
# Separador
nomes = ["Juleidy","Lorindinalvety"]

# Valor que separa os itens na variável:
separador = " "

# Junta os valores em um único valor:
nomes_junto = separador.join(nomes)

# Exibe na tela
print(nomes_junto)

```