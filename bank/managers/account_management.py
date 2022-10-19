from sqlalchemy import select
from models.base import Base, engine, Session
from models.account import SavingsAccount, PersonalAccount, Account

Base.metadata.create_all(engine)


def add_savings_account(account_number, owner, rate):
    account = SavingsAccount(account_number, owner, rate)
    with Session() as session:
        session.add(account)
        session.commit()

def add_personal_account(account_number, owner):
    account = PersonalAccount(account_number, owner)
    with Session() as session:
        session.add(account)
        session.commit()

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
