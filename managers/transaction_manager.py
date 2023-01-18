from models.transaction import Transaction
from managers.account_manager import AccountManager
from db.session import session
from db.config import TABLENAMES
from uuid import UUID

_tablename = TABLENAMES["TRANSACTION"]

class TransactionManager:
    @staticmethod
    def transfer(account_from, account_to, amount):
        if account_from.balance - amount >= 0:
            account_from.balance -= amount
            account_to.balance += amount
            account_from.update_account()
            account_to.update_account()
            AccountManager.update_account_balance(account_from)
            AccountManager.update_account_balance(account_to)
            tr1 = TransactionManager.create_transaction(amount, 'transfer_from', account_from)
            tr2 = TransactionManager.create_transaction(amount, 'transfer_to', account_to)
            return tr1, tr2

    @staticmethod
    def withdraw(account, amount):
        if account.balance - amount >= 0:
            account.balance -= amount
            account.update_account()
            AccountManager.update_account_balance(account)
            transaction = TransactionManager.create_transaction(amount, 'withdrawal', account)
            return transaction


    @staticmethod
    def deposit(account, amount):
        account.balance += amount
        account.update_account()
        AccountManager.update_account_balance(account)
        transaction = TransactionManager.create_transaction(amount, 'deposit', account)
        return transaction

    @staticmethod
    def create_transaction(amount, transaction_type, account):
        transaction = Transaction(account, amount, transaction_type, )
        session.execute(
            f"""
            INSERT INTO {_tablename}(transaction_id, account_id, amount, transaction_type, date)
            VALUES ({transaction.id}, {transaction.account.id}, {transaction.amount},
            '{transaction.transaction_type}', '{transaction.date}');
            """)
        return transaction

    @staticmethod
    def get_transaction(id):
        result = session.execute(f"SELECT * FROM {_tablename} WHERE transaction_id = {UUID(id)};")[0]
        transaction = create_from_row(result)
        return transaction

    @staticmethod
    def get_all_transactions():
        results = session.execute(f"SELECT * FROM {_tablename};")
        transactions = [create_from_row(result) for result in results]
        return transactions

    @staticmethod
    def delete_transaction(id):
        session.execute(f"DELETE FROM {_tablename} WHERE transaction_id = {id};")

    @staticmethod
    def update_transaction(transaction):
        session.execute(
                f"""
                UPDATE {_tablename} SET account_id = {transaction.account.id},
                amount = {transaction.amount}, transaction_type = '{transaction.transaction_type}',
                date = '{transaction.date}' WHERE transaction_id = {transaction.id};
                """
            )


def create_from_row(transaction):
    account = AccountManager.get_account(str(transaction.account_id))
    return Transaction(account, transaction.amount, transaction.transaction_type,
                        transaction.date, transaction.transaction_id)
