from models.client import Client
from models.account import PersonalAccount, SavingsAccount
from models.transaction import Transaction, TransactionTypes
from managers.account_manager import AccountManager
from db.db import redis_db, hash_prefix
import json


def main():
    AccountManager.delete_account("a7314dc8-7b52-4e41-9bb0-0e4b4df6736f")
    client = Client(first_name='Jan', last_name='Kowalski')
    acc1 = AccountManager.add_personal_account('457', 0, client)
    t1 = Transaction(10, TransactionTypes.deposit, acc1)
    acc2 = AccountManager.add_savings_account('456', 0, client, 1)
    # deposit(acc1, 100)
    # transfer(acc1, acc2, 50)
    print(AccountManager.get_account("261947f5-40be-4d8e-a38b-b2318e68cfe5"))
    # for trs in get_all_transactions():
    #     print(trs)
    # redis_db.set(hash_prefix['account'] + str(acc1._id), json.dumps(acc1.dict()))

    # redis_db.set(hash_prefix['account'] + str(acc2._id), json.dumps(acc2.dict()))

if __name__ == '__main__':
    main()
