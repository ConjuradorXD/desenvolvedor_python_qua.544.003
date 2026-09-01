
# Crie um programa a partir do diagrama de classes abaixo:

from dataclasses import dataclass
from abc import ABC, abstractmethod

# -------------------- Classes ------------------------

class Iconta(ABC):
	@abstractmethod
	def consultar_conta():
		pass
	
	@abstractmethod
	def fazer_deposito(valor):
		pass
		
	@abstractmethod
	def fazer_saque(valor):
		pass
	
	@abstractmethod
	def gerar_extrato():
		pass


@dataclass
class Conta(Iconta):
    titular: str
    agencia: str
    n_conta: str
    saldo: float

    def __str__(self):
        return f"Titular da conta: {self.titular}\nAgencia: {self.agencia}\nNúmero da conta: {self.profissao}\nSaldo: {self.saldo}"

    def __float__(self):
        return self.saldo

    def __del__(self):
            print(f"Objeto {self} destruido com sucesso!")

@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}"

# ---------------Métodos da interface -----------------

    # Coltua os dados da conta:

    def consultar_conta(self):
        print(f"Nome do titular da conta: {self.__titular}")
        print(f"CPF do titular da conta: {self.__cpf}")
        print(f"Agencia da conta: {self.__agencia}")
        print(f"Número da conta: {self.__n_conta}")
        print(f"Saldo da conta: R${self.__saldo:.2f}")

    # Faz o deposito:

    def fazer_deposito(self,valor):
        self.saldo += valor
        return self.__saldo

    # Faz o saque:

    def fazer_saque(self,valor):
        self.__saldo -= valor
        return self.__saldo

    # grava o extrado em um arquivo:

    def gerar_extrato(self,valor):
        return print("Extrato gerado com sucesso!")

    # imprime a mensagem de sucesso
    print("Ingresso comprado com sucesso! Tenha um bom filme!")

    # grava o ingresso em arquivo
    ingresso = f"Extrato saiu"
    with open("atividade_06/ingresso.txt", "w", encoding="utf-8") as f:
        f.write(ingresso)
    

     
      
         


