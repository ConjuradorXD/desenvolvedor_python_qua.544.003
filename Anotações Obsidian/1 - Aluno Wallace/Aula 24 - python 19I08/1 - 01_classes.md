1 - criar uma nova pasta com o nome: 01_classes.
2 - dentro dela o arquivo main.py
3 - ela foi criada com o objetivo de você programar com alinha de programar como 
no mundo real ele contem objetos, ele é separado por categorias que chamamos de classes,
4 - classe veiculo, subclasse/ compartilham a mesmas características físicas, mas compartilham semelhanças
5 - a classe é dividida em duas partes, são: atributos que definem aquela classe, 
6 - em vez de criar uma variável, criamos um objeto, que fazendo isso vamos ganhar uma facilidade de manutenção do código.
7 - você centraliza o código em classes, para fazer manutenção mais fácil.
8 - nesse programa vamos fazer uma pessoa, que possa dar oi.
9 - vamos criar uma classe que essa pessoa vai representar, vamos criar uma nova classe chamada pessoa e vamos criar um usuário com a classe pessoa.
10 - mesmas regras, nomeando uma variável, e uma classe, ela precisa obrigatoriamente começar com uma letra maiúscula, por exemplo em uma classe chamada pessoas, o p precisa ser maiúsculo:

```python
class Pessoa
```

11 - snake case que significa nome com nome_teste , isso serve para nomear tabelas de banco de dados, ou separar nomes compostos, nome das classes não usamos isso, ao invés disso,  usamos o passocase, precisa ser assim: NomeTeste.

12 - ela é dividida em dois elementos que são valores que definem aquela classe e ações que é oque aquela classe vai fazer
13 - método construtor, é uma ação que a classe vai fazer, Python é obrigatório.
ele funciona assim: ele é como se fosse uma função:

```python
def__init__()
```
14 - existe uma diferença diferente entre método função de um: método sempre recebem um argumento, a função pode receber um argumento ou não, sempre que existir um método precisa de um self:

```python
def__init__(self)
```
15 - ao lado do self, colocar os atributos daquele método:

```python
def__init__(self,nome,idade,email,altura):
```
16 - precisamos repassar para a classe todos esses atributos depois :

```python
def__init__(self,nome,idade,email,altura):
self.nome = nome
self.idade = idade
self.email = email
self.altura = altura
```
17 - vamos criar um método para exibir os dados, lembrando que aqui não é um novo objeto, e sim os atributos

```python
def exibir_dados(self):
	print(f"Nome: {self.nome})
	print(f"Idade: {self.idade}anos.)
	print(f"E-mail: {self.email})
	print(f"Altura: {self.altura}metros.)
```
18 - criar é a mesma coisa que instaciar, um objeto, para criar um objeto.
