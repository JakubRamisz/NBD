from models.base import Session
from models.client import Client
from models.account import SavingsAccount, PersonalAccount, Account


def add_savings_account(account_number, owner_id, rate):
    with Session() as session:
        owner = session.query(Client).get(owner_id)
        account = SavingsAccount(account_number, owner, rate)
        session.add(account)
        session.commit()
        account_id = account.id
    return account_id


def add_personal_account(account_number, owner_id):
    with Session() as session:
        owner = session.query(Client).get(owner_id)
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
        for account in session.query(Account).all:
            update_account_balance(account)
        session.commit()
