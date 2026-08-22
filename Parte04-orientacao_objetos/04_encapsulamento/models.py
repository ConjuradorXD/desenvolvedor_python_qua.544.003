# Encapsulamento de dados:

class Pessoa:
    def __init__(self,nome,cpf,email,telefone):

        # Informações protegidos com : __
        self.__nome = nome
        self.__cfp = cpf 
        self.__email = email
        self.__telefone = telefone

        # Métodos de acesso:

        # get acessa o valor do atributo:
        @property
        def nome(self):
            return self.__nome
        
        @nome.setter
        def nome(self, nome):
            self.__nome = nome

        @property
        def nome(self):
            return self.__cpf
        
        @nome.setter
        def nome(self, cpf):
            self.__nome = cpf

        @property
        def nome(self):
            return self.__email
        
        @nome.setter
        def nome(self, email):
            self.__nome = email

        @property
        def nome(self):
            return self.__telefone

        @nome.setter
        def nome(self, telefone):
            self.__nome = telefone

        # set dedinir o valor do atributo:


            
