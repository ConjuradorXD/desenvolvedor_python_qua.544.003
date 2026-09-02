1 - criar uma nova pasta com o nome: 11_separando_item.
2 - dentro dela o arquivo main.py
3 - Vamos criar uma lista, e vamos eliminar um item da lista, mas agora tem uma diferença, ele vai ficar armazenado em uma variável.
4 - o usuário vai informar o Nome que ele quer retirar.
5 - se o nome existir:

```python
if nome in nomes:
	indice = nomes.index(nome)

else:
	print("Nome não encontrado.")
```

6 - Agora vamos separar o nome da lista, por isso colocamos a variavel indice ali.

```python
# Separando itens e salvando eles em uma variavel:

nomes = ["Fulano","Alex","Eduardo","Cicrano","Beltrano","Lorindinalvety"]

for nome in nomes:
    print(nome)

nome = input("Informe o nome a ser separado: ").strip().title()

if nome in nomes: 
    indice = nomes.index(nome)
    
    # separar o nome da lista:

    nome_separado = nomes.pop(indice)
    os.system("cls" if os.name == "nt" else "clear")

    # exibe a lista:
    
    for nome in nomes:
        print(nome)
        
    print(f"O nome ({nome_separado}) foi separado da lista.")

else:
    print("Nome não encontrado.")

```
