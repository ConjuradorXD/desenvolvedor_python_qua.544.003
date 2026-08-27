class Pessoa:
    def __init__(self,email,telefone):
        self.__email = email
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @email.setter
    def email(self,telefone):
        self.__email = telefone

class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,email,telefone):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(email=email,telefone=telefone)

@property
def nome(self):
    return self.__nome

@nome.setter
def nome(self,nome):
    self.__nome = nome

@property
def telefone(self):
    return self.__telefone

@nome.setter
def telefone(self,telefone):
    self.__telefone = telefone

class PessoaJuridica(Pessoa):
    def __init__(self,nome_fantasia,cnpj,email,telefone):
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        super().__init__(email=email,telefone=telefone)

@property
def nome_fantasia(self):
    return self.__nome_fantasia

@nome_fantasia.setter
def nome_fantasia(self,nome_fantasia):
    self.__nome_fantasia = nome_fantasia

@property
def ncnpj(self):
    return self.__cnpj

@nome_fantasia.setter
def nome_cnpj(self,cnpj):
    self.__cnpj = cnpj


