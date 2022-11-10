import unittest
import pymongo
import mongomock
import sys
sys.path.append('../')

from models.client import Client
from managers.account_management import update_account, delete_account_by_account_number, get_account_by_account_number,get_account,add_personal_account, add_savings_account, get_all_accounts, delete_account


class TestAccountManager(unittest.TestCase):
    def test_get_account(self):
        collection = mongomock.MongoClient().db.collection
        result = '62e5195f-519d-498e-9ed9-1eec39fec633'
        self.assertEqual(get_account(result)._id, result)

    def test_add_account(self):
        collection = mongomock.MongoClient().db.collection
        client = Client('Jerry', 'Tromba')
        self.assertIsNone(get_account_by_account_number('test_account_number'))
        add_savings_account('test_account_number', client, 0.2)
        self.assertEqual(get_account_by_account_number('test_account_number').account_number, 'test_account_number')
        self.assertEqual(get_account_by_account_number('test_account_number').owner.first_name, 'Jerry')
        self.assertEqual(get_account_by_account_number('test_account_number').owner.last_name, 'Tromba')
        delete_account_by_account_number('test_account_number')

    def test_delete_account(self):
        collection = mongomock.MongoClient().db.collection
        client = Client('John', 'Johnowski')
        add_savings_account('test_account_number2', client, 0.2)
        self.assertEqual(get_account_by_account_number('test_account_number2').account_number, 'test_account_number2')
        delete_account_by_account_number('test_account_number2')
        self.assertIsNone(get_account_by_account_number('test_account_number2'))

    # def test_update_account_by_account_by_number(self):
    #     collection = mongomock.MongoClient().db.collection
    #     client = Client('John', 'Johnowski')
    #     test_acc = add_personal_account('test_account_number3', client)
    #     self.assertNotEqual(test_acc.account_number, 'test_account_number4')
    #     update_account(test_acc, account_number = 'test_account_number4')
    #     self.assertEqual(test_acc.account_number, 'test_account_number4')

if __name__ == '__main__':
    unittest.main()