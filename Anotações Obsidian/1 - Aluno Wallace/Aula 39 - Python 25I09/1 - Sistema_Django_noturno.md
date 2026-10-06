1 - instalar a extensão :
- database client

2 - instalar a biblioteca:
- pip install django

3 - criar uma venv. e ativar.

4 - depois colocar esse código: 
- django-admin startproject config .

5 - para a aplicação rodar precisa executar esse comando: 
- py manage.py runserver

6 - o significado de SGB - Sistema Gerenciador de Bando de dados
- MySQL
- Oracle
- Postgree
- DB2
- MariaDB
- SQLite

São sistemas de linhas e colunas.

7 - Vamos configurar o banco de dados e usar o SQLite, ele cria um arquivo que funciona como um servidor privado, python já vem com o SQLite junto, 

8 - CRUD =
- Create (cadastrat)
- Read (Listar)
- Update (Atualizar)
- Delete (Deletar)

 9 - abrir a extensão do cano > clicar no SQLite, > encontrar a pasta que o arquivo ta e depois entrar no arquivo com o nome : db_sistema_django.db

10 - Vamos implementar no banco de dados precisamos fazer um migrate para gerar a entidade administrador do sistema para depois criar um usuario a senha do adm, e criar depois a tela de login e painel de administrador do sistema.

11 - para fechar o servidor ctrl + C.
12 - sempre que eu fizer alguma mudança nos dados eu preciso executar o comando:

- py manage.py makemigrations
- py manage.py migrate

13 - no arquivo db_sistema_django.db, vamos criar um superuser com o comando:
- py manage.py createsuperuser
- 
14 - Depois de dar enter, vamos criar um usuário com o seguinte 
- nome: Admin
- email: admin@admin.com
- senha: admin 
15 - Depois fecha o vscode e abre de novo,

16 - criar a pasta apps depois colocar esse comando:
- py manage.py startapp crud ./apps/crud

17 - criar pasta dentro da pasta crud criar uma pasta chamada templates e depois um novo arquivo chamado index.htlm

18 - colocar dentro do arquivo app.py que está dentro de crud/app.py mudar para name = 'apps.crud'

19 - viwes.py vai servir como o app.py antigo, aqui vamos definir nossas funções.
- def index(request):
    return render(request, "index.html")

20 - dentro da pasta crud criar um arquivo chamado: urls.py, dentro desse arquivo vamos colocar:

21 - no arquivo settings.py, colocar 'apps.crud', na linha 40.

22 - em urls.py em config, na linha 22, colocar o código:
- path('', include('apps.crud.urls')),

23 - no arquivo index.html dentro de templates: 
<body> bem vindo ao crud!</body>

24 - Banco de dados relacional, nosso sistema é baseado nisso, o banco de dados em questão aqui é o SQLite, 

25 - Conceito de Pk, primaryKey ou chave primaria, é um campo é um atributo da entidade que nunca vai se repetir, é um campo de registro unico, por que para a tabela funcionar precisa de um indece que precisa se basear em valores unicos por isso precisamos de uma chave primaria,

26 - precisamos criar uma chave primaria, são dados que não vão se repetir como um cpf, vamos definir o código do paciente como chave primaria,

27 - autofield, define o

28 - charfiel é sempre uma string

29 - comando para preparar o sistema para o banco de dados:
py manage.py makemigrations

30 - comando usado depois:
py manage.py migrate

comando para limpar o terminal: cls

31 - terceiro comando:

py manage.py runserver