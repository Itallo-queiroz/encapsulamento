 #NOTE: protected =  para adicionar eu coloco o ( _ ) " È visivelapenas para subclasse"
 #NOTE: private = para adicionar eu coloco o ( __ )
# classe
class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome 
        self.__idade = idade
        self.__email = email

    # metodos de acesso 1 FORMUULA "ELA TEM UMA BREXA"
    # def get_nome(self): # NOTE: NOME
    #     return self.__nome
    
    # def set_nome(self, nome):
    #     self.__nome = nome
    
    # def get_idade(self): # NOTE: IDADE
    #     return self.__idade
    
    # def set_idade(self, idade):
    #     self.__idade = idade

    # def get_email(self):  # NOTE: E-MAIL
    #     return self.__email
    
    # def set_idade(self, email):
    #     self.__email = email

    # metodos de acesso 
    ## metodo GET NOME

    @property
    def nome(self):
        return self.__nome
    
    ## metodo SET NOME
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__idade = email



    
    


