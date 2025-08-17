from datetime import date, datetime
from app.repository.sessao_repository import SessaoRepository
from app.models.sessao_model import SessaoModel 

class SessaoService:
    def __init__(self):
        self.sessao_repository = SessaoRepository()

    def get_all_sessoes(self):
        return self.sessao_repository.get_all_sessoes()

    def create_sessao(self, sessao: SessaoModel):
        self._validar_sessao(sessao, criando=True)
        self.sessao_repository.create_sessao(sessao)
        
    def get_sessao_by_id(self, id):
        if id is None:
            raise ValueError("ID não pode ser None.")
        return self.sessao_repository.get_sessao_by_id(id)
    
    def update_sessao(self, sessao):
        self._validar_sessao(sessao, criando=False)
        self.sessao_repository.update_sessao(sessao)
        
    def delete_sessao(self, id):
        if id is None:
            raise ValueError("ID não pode ser None para exclusão de sessão.")
        self.sessao_repository.delete_sessao(id)
        
    def _validar_sessao(self, sessao: SessaoModel, criando: bool):
        if criando and sessao.get_id() is not None:
            raise ValueError("ID deve ser None para criação de sessão.")
        if not criando and sessao.get_id() is None:
            raise ValueError("ID não pode ser None para atualização de sessão.")
        if not sessao.get_id_cliente():
            raise ValueError("ID do cliente é obrigatório.")
        if not sessao.get_data_sessao():
            raise ValueError("Data da sessão é obrigatória.")
        if not sessao.get_tipo_sessao():
            raise ValueError("Tipo de sessão é obrigatório.")
        if not sessao.get_local():
            raise ValueError("Local da sessão é obrigatório.")

        data_sessao = sessao.get_data_sessao()
        if isinstance(data_sessao, str):
            data_sessao = datetime.strptime(data_sessao, "%Y-%m-%d").date()
        if sessao.get_status() == "Concluída" and data_sessao > date.today():
            raise ValueError("Não é possível concluir uma sessão que ainda não aconteceu.")
        if sessao.get_status() == "Agendada" and data_sessao < date.today():
            raise ValueError("Não é possível deixar como 'Agendada' uma sessão que já passou.")
