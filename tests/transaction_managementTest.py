import unittest
import pymongo
import mongomock
import sys
sys.path.append('../')

from models.client import Client
from managers.transaction_management import add_transaction,deposit, transfer, get_transaction, get_all_transactions, delete_transaction
from managers.account_management import add_personal_account

class TestAccountManager(unittest.TestCase):
    def test_get_account(self):
        collection = mongomock.MongoClient().db.collection
        result = '57456a2c-1d1c-438d-94d0-28933162003a'
        self.assertEqual(get_transaction(result)._id, result)

    # def test_add_transaction(self):
    #     collection = mongomock.MongoClient().db.collection
    #     client = Client('Will', 'Nowak')
    #     test_acc = add_personal_account('test_trs_acc', client)
    #     test_id = add_transaction(200, 2, client)
    #     self.assertEqual(get_transaction(test_id).amount, 200)
    #     self.assertEqual(get_transaction(test_id).transaction_type, 2)
    #     delete_transaction(test_id)

    # def test_delete_transaction(self):
    #     collection = mongomock.MongoClient().db.collection


if __name__ == '__main__':
    unittest.main()