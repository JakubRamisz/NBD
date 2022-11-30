import json
from db.db import redis_db, hash_prefix
from models.account import SavingsAccount, PersonalAccount

class AccountManagerDecorator():
    prefix = hash_prefix['account']

    @staticmethod
    def add_account(func):
        def wrapper(*args, **kwargs):
            account = func(*args, **kwargs)
            cached = AccountManagerDecorator.get_cached()
            for cached_account in cached:
                if cached_account ['account_number'] == account.account_number:
                    return account

            redis_db.set(hash_prefix['account'] + str(account._id), json.dumps(account.dict()))
            return account
        return wrapper

    @staticmethod
    def get_account(func):
        def wrapper(*args, **kwargs):
            account = redis_db.get(f'{AccountManagerDecorator.prefix}{args[0]}')
            if account is None:
                return func(*args, **kwargs)

            account = json.loads(account)
            if account['type'] == 'savings_account':
                return SavingsAccount(**account)
            return PersonalAccount(**account)
        return wrapper

    @staticmethod
    def get_all_accounts(func):
        def wrapper(*args, **kwargs):
            keys = redis_db.keys(f'{AccountManagerDecorator.prefix}*')
            if keys is None:
                return func(*args, **kwargs)

            accounts = []
            cached = AccountManagerDecorator.get_cached()
            for account in cached:
                if account['type'] == 'savings_account':
                    accounts.append(SavingsAccount(**account))
                else:
                    accounts.append(PersonalAccount(**account))
            return accounts
        return wrapper

    @staticmethod
    def delete_account(func):
        def wrapper(*args, **kwargs):
            redis_db.delete(f'{AccountManagerDecorator.prefix}{args[0]}')
            func(*args, **kwargs)
        return wrapper

    # @staticmethod
    # def update_account(account, values):
    #     collection = get_collection('accounts')
    #     collection.update_one({'_id': str(account._id)}, {'$set': values})

    # @staticmethod
    # def update_account_balance(account):
    #     account.update_balance()
    #     if account.type == 'savings_account':
    #         AccountManager.update_account(account, {'balance': account.balance,
    #                                 'last_update_date': account.last_update_date})
    #     else:
    #         AccountManager.update_account(account, {'balance': account.balance})

    # @staticmethod
    # def update_all_accounts():
    #     for account in AccountManager.get_all_accounts():
    #         AccountManager.update_account_balance(account)

    @staticmethod
    def invalidate_cache(func):
        redis_db.flushdb()
        return func

    @staticmethod
    def get_cached():
        keys = redis_db.keys(f'{AccountManagerDecorator.prefix}*')
        accounts = [json.loads(redis_db.get(key)) for key in keys]
        return accounts
