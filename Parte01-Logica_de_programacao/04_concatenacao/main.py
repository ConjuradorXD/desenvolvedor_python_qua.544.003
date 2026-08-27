# declaração de variaveis 
nome = input("Informe seu nome: ")
telefone = input("Informe a data da sua morte: ")

# saída de dados Forma 1
print("Olá ", nome, ", e a data da sua morte é ", telefone, ".")

# saída de dados Forma 2
print("Olá " + nome + ", e a data da sua morte é " + telefone + ".")

# sáida de dados forma 3
print("Olá {}, e a data da sua morte é {}." .format(nome,telefone))

# sáida de dados forma 4
print(f"Olá {nome}, e a data da sua morte é {telefone}.")