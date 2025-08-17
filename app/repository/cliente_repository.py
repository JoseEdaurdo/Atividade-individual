from app.database.connection import get_db
from app.models.cliente_model import ClienteModel

class ClienteRepository:
    
    def get_all_clientes(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        rows = cursor.fetchall()
        return [
            ClienteModel(id=row[0], nome=row[1], email=row[2], telefone=row[3]) for row in rows
        ]
        
    def get_cliente_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id = ?", (id,))
        row = cursor.fetchone()
        return ClienteModel(id=row[0], nome=row[1], email=row[2], telefone=row[3]) if row else None

    def create_cliente(self, cliente):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)",
            (cliente.get_nome(), cliente.get_email(), cliente.get_telefone())
        )
        connection.commit()
        
    def update_cliente(self, cliente):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE cliente SET nome = ?, email = ?, telefone = ? WHERE id = ?",
            (cliente.get_nome(), cliente.get_email(), cliente.get_telefone(), cliente.get_id())
        )
        connection.commit()
        
    def delete_cliente(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cliente WHERE id = ?", (id,))
        connection.commit()