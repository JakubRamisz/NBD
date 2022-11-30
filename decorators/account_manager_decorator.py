import json
from db.db import redis_db, hash_prefix
from redis import ConnectionError
from models.account import SavingsAccount, PersonalAccount


class AccountManagerDecorator():
    prefix = hash_prefix['account']

    @staticmethod
    def add_account(func):
        def wrapper(*args, **kwargs):
            account = func(*args, **kwargs)
            cached = get_cached()
            for cached_account in cached:
                if cached_account ['account_number'] == account.account_number:
                    return account

            redis_db.set(hash_prefix['account'] + str(account._id), json.dumps(account.dict()))
            return account
        return wrapper

    @staticmethod
    def get_account(func):
        def wrapper(*args, **kwargs):
            try:
                redis_db.ping()
                account = json.loads(redis_db.get(f'{AccountManagerDecorator.prefix}{args[0]}'))
                if account['type'] == 'savings_account':
                    return SavingsAccount(**account)
                return PersonalAccount(**account)
            except ConnectionError:
                return func(*args, **kwargs)
        return wrapper


    @staticmethod
    def get_all_accounts(func):
        def wrapper(*args, **kwargs):
            try:
                redis_db.ping()
                accounts = []
                cached = get_cached()
                for account in cached:
                    if account['type'] == 'savings_account':
                        accounts.append(SavingsAccount(**account))
                    else:
                        accounts.append(PersonalAccount(**account))
                return accounts
            except ConnectionError:
                return func(*args, **kwargs)
        return wrapper


    @staticmethod
    def delete_account(func):
        def wrapper(*args, **kwargs):
            redis_db.delete(f'{AccountManagerDecorator.prefix}{args[0]}')
            func(*args, **kwargs)
        return wrapper

    @staticmethod
    def update_account(func):
        def wrapper(*args, **kwargs):
            account_dict = args[0].dict()
            account_dict.update(args[1])
            redis_db.set(hash_prefix['account'] + str(account_dict['_id']),
                         json.dumps(account_dict))
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def invalidate_cache(func):
        def wrapper():
            redis_db.flushdb()
            return func
        return wrapper


def get_cached():
    keys = redis_db.keys(f'{AccountManagerDecorator.prefix}*')
    accounts = [json.loads(redis_db.get(key)) for key in keys]
    return accounts
