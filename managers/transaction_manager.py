from models.transaction import Transaction, TransactionTypes
from managers.account_manager import AccountManager
from db.db import get_collection

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
            TransactionManager.add_transaction(amount, TransactionTypes.transfer_from, account_from)
            TransactionManager.add_transaction(amount, TransactionTypes.transfer_to, account_to)

    @staticmethod
    def withdraw(account, amount):
        if account.balance - amount >= 0:
            account.balance -= amount
            account.update_account()
            AccountManager.update_account_balance(account)
            TransactionManager.add_transaction(amount, TransactionTypes.withdrawal, account)

    @staticmethod
    def deposit(account, amount):
        account.balance += amount
        account.update_account()
        AccountManager.update_account_balance(account)
        TransactionManager.add_transaction(amount, TransactionTypes.deposit, account)

    @staticmethod
    def add_transaction(amount, transaction_type, account):
        collection = get_collection('transactions')
        transaction = Transaction(amount, transaction_type, account)
        collection.insert_one(transaction.dict())
        return transaction._id

    @staticmethod
    def get_transaction(id):
        collection = get_collection('transactions')
        result = collection.find_one({'_id': str(id)})
        if result is not None:
            return Transaction(**result)   

    @staticmethod
    def get_all_transactions():
        result = []
        collection = get_collection('transactions')
        for transaction in collection.find({}):
            result.append(Transaction(**transaction))
        return result

    @staticmethod
    def delete_transaction(id):
        collection = get_collection('transactions')
        result = collection.find_one({'_id': str(id)})
        if result is not None:
            collection.delete_one({'_id': str(id)})

    @staticmethod
    def update_transaction(transaction, values):
        collection = get_collection('transactions')
        collection.update_one({'_id': str(transaction._id)}, {'$set': values})
