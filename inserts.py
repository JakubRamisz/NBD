from models.client import Client
from models.account import PersonalAccount, SavingsAccount
from models.transaction import Transaction, TransactionTypes
from managers.account_manager import AccountManager
from db.db import redis_db, hash_prefix, get_collection
import json


def main():

    client = Client('Jan', 'Kowalski')
    print()
    print(AccountManager.get_all_accounts())

if __name__ == '__main__':
    main()
