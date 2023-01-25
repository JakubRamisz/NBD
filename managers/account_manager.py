from db.db import get_collection
from models.account import SavingsAccount, PersonalAccount

class AccountManager:
    @staticmethod
    def add_savings_account(account_number, owner, rate):
        collection = get_collection('accounts')
        if collection.find_one({'account_number': account_number}) is not None:
            print('Given account number already exists.')
            return

        account = SavingsAccount(account_number, 0, owner, rate=rate)
        collection.insert_one(account.get_dictionary())
        return account


    @staticmethod
    def add_personal_account(account_number, owner):
        collection = get_collection('accounts')
        if collection.find_one({'account_number': account_number}) is not None:
            print('Given account number already exists.')
            return

        account = PersonalAccount(account_number, 0, owner)
        collection.insert_one(account.get_dictionary())
        return account


    @staticmethod
    def get_account(id):
        collection = get_collection('accounts')
        result = collection.find_one({'_id': str(id)})
        if result is not None:
            if result['type'] == 'savings_account':
                return SavingsAccount(**result)
            else:
                return PersonalAccount(**result)


    @staticmethod
    def get_account_by_account_number(account_number):
        collection = get_collection('accounts')
        result = collection.find_one({'account_number': str(account_number)})
        if result is not None:
            if result['type'] == 'savings_account':
                return SavingsAccount(**result)
            else:
                return PersonalAccount(**result)


    @staticmethod
    def get_all_accounts():
        result = []
        collection = get_collection('accounts')
        for account in collection.find({}):
            if account['type'] == 'savings_account':
                result.append(SavingsAccount(**account))
            else:
                result.append(PersonalAccount(**account))
        return result


    @staticmethod
    def delete_account(id):
        collection = get_collection('accounts')
        result = collection.find_one({'_id': str(id)})
        if result is not None:
            collection.delete_one({'_id': str(id)})


    @staticmethod
    def delete_account_by_account_number(account_number):
        collection = get_collection('accounts')
        result = collection.find_one({'account_number': str(account_number)})
        if result is not None:
            collection.delete_one({'account_number': str(account_number)})


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
