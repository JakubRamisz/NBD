import redis
import unittest
from db.config import REDIS_HOST, REDIS_PORT, REDIS_DB
from db.db import hash_prefix
from managers.account_manager import AccountManager
from models.client import Client

redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

test_client = Client('Test', 'Client')
prefix  = hash_prefix['account']

class RedisTest(unittest.TestCase):
    def __post_init__(self):
        redis_db.flushdb()

    def test_invalidate_cache(self):
        redis_db.flushdb()
        AccountManager.add_personal_account('testacc3', 0, test_client)
        self.assertEqual(len(redis_db.keys(f'{prefix}*')), 1)
        AccountManager.invalidate_cache()
        self.assertEqual(len(redis_db.keys(f'{prefix}*')), 0)

    def test_add_account(self):
        test_acc1 = AccountManager.add_personal_account('testacc1', 0, test_client)
        test_acc2 = AccountManager.add_savings_account('testacc2', 0, test_client, 0.1)
        self.assertIsNotNone(redis_db.get(f'{prefix}{test_acc1._id}'))
        self.assertIsNotNone(redis_db.get(f'{prefix}{test_acc2._id}'))

    def test_redis_connection_error(self):
        test_acc4 = AccountManager.add_personal_account('testacc4', 0, test_client)
        redis_db.flushdb()
        self.assertIsNone(redis_db.get(f'{prefix}{test_acc4._id}'))
        db = redis.Redis(host=REDIS_HOST, port=6380, db=REDIS_DB)
        self.assertEqual(test_acc4, AccountManager.get_account(test_acc4._id, db))
        self.assertTrue(len(AccountManager.get_all_accounts( db)) > 0)
