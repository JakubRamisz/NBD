from db.session import session
from models.client import Client


class ClientManager:
    @staticmethod
    def create_client(first_name, last_name):
        client = Client(first_name, last_name)
        session.execute(f"""INSERT INTO {client.tablename}(client_id, first_name, last_name)
                        VALUES ({client.id}, '{client.first_name}', '{client.last_name}');""")
        return client

    @staticmethod
    def get_all_clients():
        results = session.execute("SELECT * FROM clients;")
        clients = [Client(result.first_name, result.last_name, id=result.client_id) for result in results]
        return clients

    @staticmethod
    def delete_client(client_id):
        session.execute(f"DELETE FROM clients WHERE client_id = {client_id};")
