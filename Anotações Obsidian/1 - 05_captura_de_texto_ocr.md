1 - Objetivo desse programa é tirar uma foto do texto e extrair o texto da foto.
2 - primeiro instalar a venv.
3 - depois criar as pastas:

```python
static / img / [css] / [estilo.css] /
templates / [includes] / [header.html] / [footer.html] /
/ base.html / index.html / extracao.html /
app.py

```

4 - depois instalar a biblioteca chamada Flask:

```python
pip install Flask
```

5 - entrar no site bootstrep e copiar em docs o segundo codigo em index.html:

```python
<!doctype html>
<html lang="pt-br">
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

```text
https://getbootstrap.com/docs/5.3/getting-started/introduction/
```

6 - Vamos pegar uma imagem para servir como logo no icon-icons para uma imagem .ico.

```text
https://icon-icons.com/
```

```text
https://icons8.com.br/icons/set/pixel
```

```text
https://www.flaticon.com/
```

7 - ocr significa extração de textos através de imagem.

```python
Instalar a extenção jinja 
```

8 - toda vez que eu criar um arquivo que vai servir de conteúdo para uma base o código de linha é sempre esse:

```python
{% extends 'vase.html' %}
{% block content %}

{% endblock %}
```

9 - 