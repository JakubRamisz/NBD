from models.base import Base, engine, Session
from models.transaction import Transaction, TransactionTypes

Base.metadata.create_all(engine)


def transfer(account_from, account_to, amount):
    if account_from.balance - amount >= 0:
        account_from.balance -= amount
        account_to += amount
        account_from.update_account()
        account_to.update_account()

        add_transaction(amount, TransactionTypes.transfer_from, account_from)
        add_transaction(amount, TransactionTypes.transfer_to, account_to)


def withdraw(account, amount):
    if account.balance - amount >= 0:
        account.balance -= amount
        account.update_account()

        add_transaction(amount, TransactionTypes.withdrawal, account)


def deposit(account, amount):
    account.balance += amount
    account.update_account()

    add_transaction(amount, TransactionTypes.deposit, account)


def add_transaction(amount, transaction_type, account, date=None):
    transaction = Transaction(amount, transaction_type, account, date)
    with Session() as session:
        session.add(transaction)
        session.commit()
