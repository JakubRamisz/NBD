from db.session import session
from db.config import TABLENAMES
from models.client import Client

_tablename = TABLENAMES["CLIENT"]

class ClientManager:
    @staticmethod
    def create_client(first_name, last_name):
        client = Client(first_name, last_name)
        session.execute(f"""INSERT INTO {_tablename}(client_id, first_name, last_name)
                        VALUES ({client.id}, '{client.first_name}', '{client.last_name}');""")
        return client

    @staticmethod
    def get_all_clients():
        results = session.execute(f"SELECT * FROM {_tablename};")
        clients = [Client(result.first_name, result.last_name, id=result.client_id) for result in results]
        return clients

    @staticmethod
    def get_client(id):
        result = session.execute(f"SELECT * FROM {_tablename} WHERE client_id = {id};")[0]
        client = Client(result.first_name, result.last_name, id=result.client_id)
        return client

    @staticmethod
    def delete_client(id):
        try:
            session.execute(f"DELETE FROM {_tablename} WHERE client_id = {id};")
        except IndexError as exc:
            raise IndexError from exc

    @staticmethod
    def update_client(client):
        session.execute(
            f"""
            UPDATE {_tablename} SET first_name = '{client.first_name}',
            last_name = '{client.last_name}'
            WHERE client_id = {client.id};
            """
        )
