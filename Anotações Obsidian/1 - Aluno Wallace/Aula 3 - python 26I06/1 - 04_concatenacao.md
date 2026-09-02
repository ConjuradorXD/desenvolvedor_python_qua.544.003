1 - criar uma nova pasta com o nome: 04_concatenacao.
2 - novo arquivo chamado: main.py.
3 - concatenar é juntar um texto com variável,
3 - formas de concatenar são:

- 1 - Forma: print( "string" , variável, "." ) Não é bom usar essa forma pois ele adiciona um espaço depois do texto.
- 2 - Forma: print( "string" + variável + "." ) Em vez de usar , usar o +, fica com espaço normal.
- 3 - Forma: print("string {}. " .format(variável)) 
- 4 - Forma: print(f"Olá {nome}.") Essa é a forma mais usada, a principal.

-------------------------------

- forma de colocar varias variáveis no texto:

nome = input("Informe seu nome: ")
telefone = input("Informe a data da sua morte: ")

  
saída de dados Forma 1
print("Olá ", nome, ", e a data da sua morte é ", telefone, ".")

saída de dados Forma 2
print("Olá " + nome + ", e a data da sua morte é " + telefone + ".")

sáida de dados forma 3
print("Olá {}, e a data da sua morte é {}." .format(nome,telefone))

sáida de dados forma 4
print(f"Olá {nome}, e a data da sua morte é {telefone}.")

5 - para dar play apertar: ctrl + f5, escolher a opção: python debugger, se der certo aparece no terminal o que foi escrito.