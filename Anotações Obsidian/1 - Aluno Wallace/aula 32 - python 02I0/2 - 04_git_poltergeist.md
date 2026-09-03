1 - Esse programa você cria um executável para área de trabalho, 
2 - para gerar um executavel, primeiro precisamos colocar uma imagem .ico dentro do progeto, com isso vamos colocar o comando:

```python
yinstaller --onefile --name "Git Poltergeist v1.0" --icon "icone1.ico" main.py
```

depois de fazer isso gerar o comando: 

```python
pip freeze > requirements.txt
```

os arquivos gerados para criar o arquivo executavel, vamos tirar do commit com o arquivo:

```python
.gitignore
```