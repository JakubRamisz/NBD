from models.base import Session
from models.client import Client


def add_client(first_name, last_name):
	client = Client(first_name, last_name)
	with Session() as session:
		session.add(client)
		session.commit()
		client_id = client.id
	return client_id
