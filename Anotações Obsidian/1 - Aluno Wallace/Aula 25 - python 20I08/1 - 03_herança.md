1 - criar uma nova pasta com o nome: 03_herança.
2 - dentro dela o arquivo main.py e models.py
3 - herança herda algumas das características e atribulo de outra classe
4 - entre parênteses coloca a classe que vai ser herdada.

```python
class PessoaFisica(Pessoa)
```
5 - consultor da classe tem que repassar os atributos também:

```python
class PessoaFisica(Pessoa)
	def __init__(self,nome,cpf,email,telefone,endereço):
	self.nome = nome
	self.cpf = cpf
```

6 - para que ele possa herdar os atributos:

```python
super.__init__(email=email,telefone=telefone,endereço=endereço)
```

7 - a orientação a objetos é baseada em 4 pilares, são eles:

- herança
- polimorfismo
- abstração
- encapsulamento

8 - o polimorfismo é o nome que a gente da a uma classe que tem o mesmo método mas com a mesma ação de formas diferentes.
9 - dois animais diferentes na mesma classe, humano e cavalo, os dois fazem barulho com a boca mas sons diferentes.
10 - mesma analogia de dois humanos falando, mas não o mesmo idioma.
