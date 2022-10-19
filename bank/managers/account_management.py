from models.client import Client
from sqlalchemy import select
from models.base import Base, engine, Session
from models.account import SavingsAccount, PersonalAccount, Account

def add_savings_account(account_number, owner_id, rate):
    with Session() as session:
        owner = find_owner_by_id(session, owner_id)
        account = SavingsAccount(account_number, owner, rate)
        session.add(account)
        session.commit()
        account_id = account.id
    return account_id


def add_personal_account(account_number, owner_id):
    with Session() as session:
        owner = find_owner_by_id(session, owner_id)
        account = PersonalAccount(account_number, owner)
        session.add(account)
        session.commit()
        account_id = account.id
    return account_id


def update_account_balance(account):
    with Session() as session:
        account.update_balance()
        session.commit()


def update_all_accounts():
    with Session() as session:
        stmt = select(Account)
        for account in session.scalars(stmt):
            update_account_balance(account)
        session.commit()


def find_owner_by_id(session, owner_id):
    stmt = select(Client).where(Client.id == owner_id)
    return session.scalars(stmt).one()
