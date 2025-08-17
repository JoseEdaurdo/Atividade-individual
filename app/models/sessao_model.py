class SessaoModel:
    def __init__(self, id, id_cliente, data_sessao, tipo_sessao, local, status):
        self.__id = id
        self.__id_cliente = id_cliente
        self.__data_sessao = data_sessao
        self.__tipo_sessao = tipo_sessao
        self.__local = local
        self.__status = status
        
    def get_id(self):
        return self.__id
    def get_id_cliente(self):
        return self.__id_cliente
    def get_data_sessao(self):
        return self.__data_sessao
    def get_tipo_sessao(self):
        return self.__tipo_sessao
    def get_local(self):
        return self.__local
    def get_status(self):
        return self.__status
    
    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente
    def set_data_sessao(self, data_sessao):
        self.__data_sessao = data_sessao
    def set_tipo_sessao(self, tipo_sessao):
        self.__tipo_sessao = tipo_sessao
    def set_local(self, local):
        self.__local = local
    def set_status(self, status):
        self.__status = status
    