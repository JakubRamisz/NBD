from db.db import get_collection
from models.account import SavingsAccount, PersonalAccount
from decorators.account_manager_decorator import AccountManagerDecorator


class AccountManager:
    @staticmethod
    @AccountManagerDecorator.add_account
    def add_savings_account(account_number, balance, owner, rate):
        collection = get_collection('accounts')
        account = collection.find_one({'account_number': account_number})
        if account is not None:
            print('Given account number already exists.')
            return create_from_json(account)

        account = SavingsAccount(account_number, balance, owner, rate=rate)
        collection.insert_one(account.dict())
        return account

    @staticmethod
    @AccountManagerDecorator.add_account
    def add_personal_account(account_number, balance, owner):
        collection = get_collection('accounts')
        account = collection.find_one({'account_number': account_number})
        if account is not None:
            print('Given account number already exists.')
            return create_from_json(account)

        account = PersonalAccount(account_number, balance, owner)
        collection.insert_one(account.dict())
        return account

    @staticmethod
    @AccountManagerDecorator.get_account
    def get_account(id):
        collection = get_collection('accounts')
        result = collection.find_one({'_id': str(id)})
        if result is not None:
            return create_from_json(result)

    @staticmethod
    @AccountManagerDecorator.get_all_accounts
    def get_all_accounts():
        result = []
        collection = get_collection('accounts')
        for account in collection.find({}):
            result.append(create_from_json(account))
        return result

    @staticmethod
    def delete_account(id):
        collection = get_collection('accounts')
        result = collection.find_one({'_id': str(id)})
        if result is not None:
            collection.delete_one({'_id': str(id)})


    @staticmethod
    def update_account(account, values):
        collection = get_collection('accounts')
        collection.update_one({'_id': str(account._id)}, {'$set': values})

    @staticmethod
    def update_account_balance(account):
        account.update_balance()
        if account.type == 'savings_account':
            AccountManager.update_account(account, {'balance': account.balance,
                                    'last_update_date': account.last_update_date})
        else:
            AccountManager.update_account(account, {'balance': account.balance})

    @staticmethod
    def update_all_accounts():
        for account in AccountManager.get_all_accounts():
            AccountManager.update_account_balance(account)

    @staticmethod
    @AccountManagerDecorator.invalidate_cache
    def invalidate_cache():
        pass


def create_from_json(account):
    if account['type'] == 'savings_account':
        return SavingsAccount(**account)
    return PersonalAccount(**account)
