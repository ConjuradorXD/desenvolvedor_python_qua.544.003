1 - arquivos estaticos é tudo que cria a front end e não é 
tudo que for imagens html etc.
2 - não podemos salvar uma img em qualquer pasta, nem dentro da raiz e nem do template
3 - para reconhecer as imagens dentro do nosso projeto temos que criar uma nova pasta fora de templates com o exato nome: 

```python
static
```

folha de estilo em cascata css:

criar dentro dela as pastas:
```python
img
fonts
css / estilo.css / fonts.css
```

depois de baixar e extrair a font, mudar o nome dela para tirar os espaços, depois colocar dentro da pasta fontes

colocar a imagem dentro da pasta img

css / estilo.css:
```python
body {
    font-family: Hunterra, Helvetica, sans-serif; 
    background-color: rgb(39, 3, 6);
    color: #673639;
}

h1, h2 {
    text-align: center;
}
```

fonts.css:

```python
@font-face {
    font-family: 'Hunterra';
    src: url(../fonts/Hunterra.ttf) format('truetype');
    font-weight: normal;
    font-style: normal;
}
```

