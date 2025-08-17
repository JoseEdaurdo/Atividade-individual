class ClienteModel:
    def __init__(self, id, nome, email, telefone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_telefone(self):
        return self.__telefone
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_telefone(self, telefone):
        self.__telefone = telefone
    