from sqlalchemy import select
from models.account import Account
from models.base import Session
from models.transaction import Transaction, TransactionTypes


def transfer(account_id_from, account_id_to, amount):
    with Session() as session:
        account_from = find_account_by_id(session, account_id_from)
        account_to = find_account_by_id(session, account_id_to)
        if account_from.balance - amount >= 0:
            account_from.balance -= amount
            account_to.balance += amount
            account_from.update_account()
            account_to.update_account()
        session.commit()

    add_transaction(session, amount, TransactionTypes.transfer_from, account_from)
    add_transaction(session, amount, TransactionTypes.transfer_to, account_to)


def withdraw(account_id, amount):
    with Session() as session:
        account = find_account_by_id(session, account_id)
        if account.balance - amount >= 0:
            account.balance -= amount
            account.update_account()
        session.commit()

    add_transaction(session, amount, TransactionTypes.withdrawal, account)


def deposit(account_id, amount):
    with Session() as session:
        account = find_account_by_id(session, account_id)
        account.balance += amount
        account.update_account()
        add_transaction(session, amount, TransactionTypes.deposit, account)
        session.commit()


def add_transaction(session, amount, transaction_type, account, date=None):
    transaction = Transaction(amount, transaction_type, account, date)
    session.add(transaction)
    return transaction


def find_account_by_id(session, acc_id):
    stmt = select(Account).where(Account.id == acc_id)
    return session.scalars(stmt).one()
