from managers.account_management import add_personal_account, add_savings_account, get_account
from models.client import Client
from managers.transaction_management import add_transaction
from models.transaction import *
import db


def main():
    client = Client('Jan', 'Kowalski')
    acc = add_personal_account('123', client)
    add_savings_account('456', client, 0.1)
    print(get_account('123'))
    col = db.get_collection('accounts')
    for cl in col.find({}):
        print(cl['_id'])
        # col.delete_one({'_id': cl['_id']})
    add_transaction(10, TransactionTypes.deposit, acc)



if __name__ == '__main__':
    main()
