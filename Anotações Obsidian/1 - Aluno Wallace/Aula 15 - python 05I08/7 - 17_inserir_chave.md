1 - criar uma nova pasta com o nome: 17_inserir_chave.
2 - dentro dela o arquivo main.py
3 - Nesse programa vamos usar a chave do outro programa, nesse programa o usuário vai adicionar o telefone.
4 - ficando dessa forma:

```python
# Inserir chave

usuario = {
    'nome': "Fulano de tal",
    'idade': 35,
    'email': "fulanodetal@gmail.com",
    'cpf': "123,456,789-12",
    }

# Adiciona a chave telefone ao dicionário:

usuario['telefone'] = input(f"Informe o telefone de {usuario.get('nome')}: ").strip()

# Exibe o dicionário:

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
    
```



