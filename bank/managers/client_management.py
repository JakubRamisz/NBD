from models.base import Base, engine, Session
from models.client import Client


Base.metadata.create_all(engine)

def add_client(first_name, last_name):
	client = Client(first_name, last_name)
	with Session() as session:
		session.add(client)
		session.commit()
