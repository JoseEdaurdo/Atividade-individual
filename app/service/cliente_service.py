from app.repository.cliente_repository import ClienteRepository
from app.models.cliente_model import ClienteModel
from app.repository.sessao_repository import SessaoRepository

class ClienteService:
    def __init__(self):
        self.cliente_repository = ClienteRepository()
        self.sessao_repository = SessaoRepository()

    def get_all_clientes(self):
        return self.cliente_repository.get_all_clientes()

    def create_cliente(self, cliente: ClienteModel):
        if cliente.get_id() is not None:
            raise ValueError("ID deve ser None para criação de cliente.")
        if not cliente.get_nome() or not cliente.get_email():
            raise ValueError("Nome e email são obrigatórios.")
        if any(char.isdigit() for char in cliente.get_nome()):
            raise ValueError("Nome não deve conter números.")
        if not cliente.get_telefone().isdigit():
            raise ValueError("Telefone deve conter apenas números.")
        self.cliente_repository.create_cliente(cliente)
        
    def get_cliente_by_id(self, id):
        if id is None:
            raise ValueError("ID não pode ser None.")
        return self.cliente_repository.get_cliente_by_id(id)  
    
    def update_cliente(self, cliente):
        if cliente.get_id() is None:
            raise ValueError("ID não pode ser None para atualização de cliente.")
        if not cliente.get_nome() or not cliente.get_email():
            raise ValueError("Nome e email são obrigatórios.")
        if any(char.isdigit() for char in cliente.get_nome()):
            raise ValueError("Nome não deve conter números.")
        if not cliente.get_telefone().isdigit():
            raise ValueError("Telefone deve conter apenas números.")
        self.cliente_repository.update_cliente(cliente)
    
    def delete_cliente(self, id):
        if id is None:
            raise ValueError("ID não pode ser None para exclusão de cliente.")
        sessoes_do_cliente = self.sessao_repository.get_all_sessoes()
        for sessao in sessoes_do_cliente:
            if sessao.get_id_cliente() == id:
                raise ValueError("Não é possível excluir o cliente, pois existem sessões associadas a ele.")
        self.cliente_repository.delete_cliente(id)

        
        