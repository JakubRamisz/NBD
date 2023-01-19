from db.session import session
from db.config import TABLENAMES
from models.client import Client
from managers.client_manager import ClientManager
import unittest


clients_table = TABLENAMES["CLIENT"]

class TestClientManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        session.execute(f"""
            CREATE TABLE IF NOT EXISTS {clients_table} (
                client_id uuid PRIMARY KEY,
                first_name text,
                last_name text
            );
        """)
        session.execute(f"TRUNCATE {clients_table}")

    def test_create_client(self):
        client = ClientManager.create_client('Stefan', 'Stefaniak')
        self.assertIsInstance(client, Client)
        self.assertEqual(client.first_name, 'Stefan')
        self.assertEqual(client.last_name, 'Stefaniak')

    def test_get_client(self):
        client = ClientManager.create_client('Wieslaw', 'Wieslawski')
        returned_client = ClientManager.get_client(client.id)
        self.assertEqual(returned_client.id, client.id)
        self.assertEqual(returned_client.first_name, client.first_name)
        self.assertEqual(returned_client.last_name, client.last_name)

    def test_get_all_clients(self):
        client1 = ClientManager.create_client('Franciszek', 'Franciszkanski')
        client2 = ClientManager.create_client('Zbyszek', 'Zbyszkowski')
        client_ids = [client.id for client in ClientManager.get_all_clients()]
        self.assertIn(client1.id, client_ids)
        self.assertIn(client2.id, client_ids)

    def test_delete_client(self):
        client = ClientManager.create_client('Wanda', 'Wandachowicz')
        ClientManager.delete_client(client.id)
        try:
            self.assertRaises(IndexError, ClientManager.get_client(client.id))
        except IndexError:
            pass

    def test_update_client(self):
        client = ClientManager.create_client('Jessica', 'Jones')
        client.first_name = 'Jessica'
        client.last_name = 'Smith'
        ClientManager.update_client(client)
        returned_client = ClientManager.get_client(client.id)
        self.assertEqual(returned_client.first_name, 'Jessica')
        self.assertEqual(returned_client.last_name, 'Smith')
