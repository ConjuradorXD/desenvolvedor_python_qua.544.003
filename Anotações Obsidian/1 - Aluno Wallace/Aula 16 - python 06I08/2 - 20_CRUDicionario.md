1 - criar uma nova pasta com o nome: 19_lista_de_dicionarios.
2 - dentro dela o arquivo main.py
3 - O que é um CRUD:

```python
CRUD é a junção em um programa dessas 4 funções:

C = Create (cadastrar)
R = Read (Listar)
U = update (Atualizar)
D = delet (Deletar)

Ele realiza essas 4 funções antes do programa se encerrar.
```

4 - esse programa precisa fazer essas 4 operações, vamos ter que fazer um laço de repetição, após ele limpar a tela vamos aplicar um while True e criar um menu para o usuário escolher. 
 ```python
 match opcao:
        case "1":
            # cria novo dicionário:

            usuario = {}
            usuario['nome'] = input("Informe o nome: ").strip.title()
            usuario['cpf'] = input("Informe o CPF: ").strip
            usuario['email'] = input("Informe o email: ").strip.lowe()

            # Adiciona dicionário na lista

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            continue
 ```

5 - Para adicionar esses dados na lista, basta chamar a lista com o comando: usuarios.append(usuario)