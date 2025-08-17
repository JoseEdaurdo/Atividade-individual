from app.database.connection import get_db
from app.models.sessao_model import SessaoModel

class SessaoRepository:
    
    def get_all_sessoes(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" SELECT s.id, s.id_cliente, s.data_sessao, s.tipo_sessao, s.local, s.status, c.nome
                          FROM sessao s
                          JOIN cliente c ON s.id_cliente = c.id """)
        rows = cursor.fetchall()
        sessoes = []
        for row in rows:
            sessao = SessaoModel(
                id=row[0],
                id_cliente=row[1],
                data_sessao=row[2],
                tipo_sessao=row[3],
                local=row[4],
                status=row[5]
            )
            sessao.cliente_nome = row[6]
            sessoes.append(sessao)
        return sessoes
    
    def get_sessao_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" SELECT s.id, s.id_cliente, s.data_sessao, s.tipo_sessao, s.local, s.status, c.nome
                          FROM sessao s
                          JOIN cliente c ON s.id_cliente = c.id
                          WHERE s.id = ? """, (id,))
        row = cursor.fetchone()
        if row:
            sessao = SessaoModel(
                id=row[0],
                id_cliente=row[1],
                data_sessao=row[2],
                tipo_sessao=row[3],
                local=row[4],
                status=row[5]
            )
            sessao.cliente_nome = row[6]
            return sessao


    def create_sessao(self, sessao):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO sessao (id_cliente, data_sessao, tipo_sessao, local, status)
               VALUES (?, ?, ?, ?, ?)""",
            (sessao.get_id_cliente(), sessao.get_data_sessao(), sessao.get_tipo_sessao(),
             sessao.get_local(), sessao.get_status())
        )
        connection.commit()
        
    def update_sessao(self, sessao):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            """UPDATE sessao SET id_cliente = ?, data_sessao = ?, tipo_sessao = ?, local = ?, status = ?
               WHERE id = ?""",
            (sessao.get_id_cliente(), sessao.get_data_sessao(), sessao.get_tipo_sessao(),
             sessao.get_local(), sessao.get_status(), sessao.get_id())
        )
        connection.commit()
    
    def delete_sessao(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sessao WHERE id = ?", (id,))
        connection.commit()
        
    def get_sessoes_by_cliente_id(self, id_cliente):
        connetion = get_db()
        cursor = connetion.cursor()
        cursor.execute("SELECT * FROM sessao WHERE id_cliente = ?", (id_cliente,))
        return cursor.fetchall()