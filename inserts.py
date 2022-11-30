from models.client import Client
from models.account import PersonalAccount, SavingsAccount
from models.transaction import Transaction, TransactionTypes
from managers.account_manager import AccountManager
from db.db import redis_db, hash_prefix, get_collection
import json


def main():
    acc = AccountManager.get_account("261947f5-40be-4d8e-a38b-b2318e68cfe5")
    print(acc)
    acc = AccountManager.update_account(acc, {'balance': 60})
    print(acc)

if __name__ == '__main__':
    main()
