from models.client import Client
from models.account import PersonalAccount, SavingsAccount
from models.transaction import Transaction, TransactionTypes
from db.db import redis_db, hash_prefix
import json


def main():
    # for acc in get_all_accounts():
    #     delete_account(acc._id)

    # for trs in get_all_transactions():
    #     delete_transaction(trs._id)

    client = Client(first_name='Jan', last_name='Kowalski')
    acc1 = PersonalAccount('123', 0, client)
    t1 = Transaction(10, TransactionTypes.deposit, acc1)
    acc2 = SavingsAccount('456', 0, client)
    # deposit(acc1, 100)
    # transfer(acc1, acc2, 50)
    # for acc in get_all_accounts():
    #     print(acc)

    # for trs in get_all_transactions():
    #     print(trs)
    redis_db.set(hash_prefix['personal_account'] + str(acc1._id), json.dumps(acc1.__dict__()))

    redis_db.set(hash_prefix['savings_account'] + str(acc2._id), json.dumps(acc2.__dict__()))

if __name__ == '__main__':
    main()
