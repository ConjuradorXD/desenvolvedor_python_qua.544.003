Esse programa serve para dar commit, escolher o repositório e criar um novo também.
1 - instalar e ativar a venv. 
2 - instalar a biblioteca flask.
3 - criar as pastas:

```python
static
css / fontes.css
img
fonts
templates / index.html
app.py
```

4 - baixar uma fonte no site: da font.
5 - baixar uma imagem para o ícone do app com a extensão .ico.
6 - colocar os arquivos nas respectivas pastas img e fonts.
7 - arquivos base do app.py:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
```

8 - ler documentação é o segredo da documentação.
9 - entrar no site bootstrep, ir em docs, depois copiar o segundo código dentro do arquivo index.html :

```python
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  </body>
</html>
```


