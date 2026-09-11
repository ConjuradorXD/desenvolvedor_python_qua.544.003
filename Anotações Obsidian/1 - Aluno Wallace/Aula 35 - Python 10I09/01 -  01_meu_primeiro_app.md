0 - criar uma nova pasta 07-Flask.
1 - Flask é um framework web, usado para desenvolver aplicativos pequenos e rápidos para pouco poder de funcionamento.
2 - Flask é para apps pequenos.
3 - são sistemas estático e sistema dinâmico:

- site estático: os dados que são mostrados e trabalham, não saem daquela pagina, não há uma troca de dados entre o aplicativo e o cliente, se tiver apenas front and, ele é um sistema estático, apenas com HTML, CSS, Javascript.

- Sistema dinâmico existe troca de dados entre uma pagina e outra, e entre o cliente e o servidor, qualquer sistema com back and é um sistema dinâmico.

4 - Flask vai criar um servidor vai abrir a pagina html e vai usar o python para transferir alguns dados, nem todos usam dados, mas eles podem transferir informações também, para transferir dados entre o servidor e o site em html.

5 - primeiro vamos instalar o flask, sempre instalando um por projeto com o comando:

```python
pip install Flask
```

6 - letra maiúsculas  e minúscula influencia aqui.
7 - vamos trabalhar com rotas.
8 - Para executar o programa:
alt + f5 
9 - primeiro precisamos criar a pagina em html, ela precisa estar na raiz do projeto com o nome:

```python
templates
```
10 - depois:

```python
index.html
```

11 - Para criar um template do texto html:

```html
<marquee><marquee>
<h1>Titulo<h1>
```

12 - atalho para o navegador: 

```python
ctrl + alt + ;
```

13 - jinja é um codigo python que é inserido dentro do html para trazer as variaveis do python para dentro do html, se eu quiser meu html exiba ou altere dados no meu arquivo html, eu preciso do jinja, 

14 - jinja é uma biblioteca que já vem com o flask

15 - fazer os imports:
```python
from flask import Flask, render_template, request
```
