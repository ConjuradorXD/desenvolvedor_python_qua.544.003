
3 - métodos especiais, também conhecidos como métodos mágicos ou dander, são métodos que definem como 

4 - métodos especiais são um método que a gente cria que define um método para uma classe,.
5 - para diferenciar um metodo comum de um especial é facil pois tem sempre um padrão com dois __.

6 - Essa função é um método especial, consultor da classe,

```python
__init__
```

```python
def __str__(self):
	return f"Olá, meu nome é {self.nome} X" 
```

essa função str é uma função que obrigatoriamente retorna uma string, toda vez que se chama um objeto, se não chamar nenhum atributo de um objeto, 

o método len nunca vai voltar como string.

sempre por o método: 

```python
class Pessoa:
    # construtor 
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return f"Olá, meu nome é {self.nome}e tenho {len(self)}anos de idade e {float(self) metros de altura.}."
    
    def __len__(self):
        return self.idade
```

metodo destrutor, é o metodo que mata o objeto,
podemos organizar melhor a memoria do nosso computador.
para programar o metodo destrutor não retorna valores, é um metodo void, mas pode voltar com um print ficando assim:

```python
    def __del__(self):
        print(f"Objeto {self} destruido com sucesso! 😘")
```