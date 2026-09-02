1 - git = programa de versionamento
2 - GitHub = plataforma de repositórios
3 - criar uma conta no github com um email profissional, 
4 - clicar em repositors, depois em new e criar um repositório para o curso.
5 - colocar o nome desenvolvedor_python_qua.544.003.
6 - na descrição: Repositório do curso de desenvolvimento Python.
7 - colocar em publico para servir de portfolio, e depois criar o repositório.
8 - Já criamos o repositório no github, agora vamos criar o repositório local na pasta parte01_Logica_de_programacao. 
9 - abrir o terminal com ctrl + J , escrever o comando: git init, se ficar todas as pastas verdes, é por que deu certo.
10 - commit é salvar uma versão dos arquivos, um backup anterior.
11 - Agora vamos setar nossas credencias no repositório, mas primeiro precisamos tirar as credenciais de outras pessoas do VScode,
12 - vamos retirar todas as credencias de outros usuários com o comando: 

git config --unset-all user.name
git config --global --unset-all user.name

13 - Agora vamos repetir o mesmo comando mas alterar o final de name para email: 

git config --unset-all user.email
git config --global --unset-all user.email

14 - depois de tirar todos os users e email da maquina, vamos setar o nosso igual do Github com nome e email com os comandos:

git config user.name "ConjuradorXD"
git config user.email "wallace.vinicius.alves@live.com"

15 - Para ver se deu certo use o comando: 

git config --list

16 - aperta tecla k




