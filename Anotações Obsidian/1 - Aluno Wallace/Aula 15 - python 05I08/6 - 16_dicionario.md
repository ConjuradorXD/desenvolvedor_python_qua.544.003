1 - criar uma nova pasta com o nome: 16_dicionario.
2 - dentro dela o arquivo main.py
3 - dicionário é o terceiro tipo de coleção, é algo mais difícil das outras coisas que a gente viu até agora.
4 - Nesse programa vamos fazer um dicionário,
5 - O que é um dicionário? é igual uma lista que vimos como a tupla, podemos listar, alterar. deletar, ordenar, a diferença de uma lista normal é que ela é ordenada por uma posição, o dicionário não é organizado por itens, e sim por chaves, são organizados por palavra chaves.
6 - no java o objeto chama jason, dicionário é quase idêntico ao jason, a estrutura é muito similar.
7 - O dicionário que vamos criar vai ser apenas para um usuário, vamos dar o nome para ele de dicionário, vamos entregar apenas os dados de um usuário,

```python
Lista - [ ] 
Tupla - ( ) 
Dicionario - { }
```

8 - aspas simples separam os nomes, e aspas duplas o conteúdo:
9 -para exibir os dados do dicionário:

10 - Forma 1:

```python
# Exibir os dados do dicionário:

print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"Email: {usuario['email']}")
print(f"CPF: {usuario['cpf']}")
```

11 - a forma dois é parecida com a forma um, só que ao invés de chamar o colchetes, coloca o comando.get:

12 - Forma 2:

```python
# Forma 2:

print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Email: {usuario.get('email')}")
print(f"CPF: {usuario.get('cpf')}")
```

13 - São formas diferente então é sempre bom saber os dois pois cada um tem formas diferentes de uso.

14 - Forma 1: existe uma possibilidade em ambos os casos de informar uma chave que não existe, mas se você pedir uma informação da forma 1, o programa ele cracha.
14 - a forma 2 ele não vai crashar, ele vai informar que o programa não tem aquele dado, 
15 - A desvantagem da 2 forma, você só consegue exibir os dados, mas você não consegue alterar os dados.

16 - Forma 3:

```python
# Forma 3:

for chave in usuario:
    print(f"{chave.capitalize()}:{usuario.get(chave)}")
```

17 - na forma 3, é possivel usar o for chave in usuario:

```python
# Dicionário:

usuario = {
    'nome': "Fulano de tal",
    'idade': 35,
    'email': "fulanodetal@gmail.com",
    'cpf': "123,456,789-12",
    }

# Exibir os dados do dicionário:

print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"Email: {usuario['email']}")
print(f"CPF: {usuario['cpf']}")

# Forma 2:

print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Email: {usuario.get('email')}")
print(f"CPF: {usuario.get('cpf')}")

# Forma 3:

for chave in usuario:
    print(f"{chave.capitalize()}:{usuario.get(chave)}")

```

o comando .capitalize serve para deixar a primeira letra maiúscula.


