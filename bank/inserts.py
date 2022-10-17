from models.base import Base, engine, Session
from models.client import Client
from models.transaction import Transaction, TransactionTypes
from models.account import SavingsAccount, PersonalAccount


Base.metadata.create_all(engine)

session = Session()


client1 = Client('Jan', 'Kowalski')
account = SavingsAccount('123', client1, 10, 0.1)
a2= PersonalAccount('22',client1, 12 )

t1 = Transaction(100, TransactionTypes.withdrawal, account)
t2 = Transaction(120, TransactionTypes.withdrawal, a2)


session.add(t1)
session.add(t2)

session.commit()

session.close()
