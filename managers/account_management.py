from db import get_collection
from models.account import SavingsAccount, PersonalAccount, Account


def add_savings_account(account_number, owner, rate):
    collection = get_collection('accounts')
    if collection.find_one({'account_number': account_number}) is not None:
        print('Given account number already exists.')
        return

    account = SavingsAccount(account_number, 0, owner, rate=rate)
    collection.insert_one(account.get_dictionary())
    return account


def add_personal_account(account_number, owner):
    collection = get_collection('accounts')
    if collection.find_one({'account_number': account_number}) is not None:
        print('Given account number already exists.')
        return

    account = PersonalAccount(account_number, 0, owner)
    collection.insert_one(account.get_dictionary())
    return account


def get_account(id):
    collection = get_collection('accounts')
    result = collection.find_one({'_id': id})
    if result is not None:
        return Account(**result)


def get_all_accounts():
    result = []
    collection = get_collection('accounts')
    for account in collection.find({}):
        result.append(Account(**account))
    return result


def delete_account(id):
    collection = get_collection('accounts')
    result = collection.find_one({'_id': id})
    if result is not None:
        collection.delete_one({'_id': id})


def update_account(account, values):
    collection = get_collection('accounts')
    collection.update_one({'_id': str(account._id)}, {'$set': values})


def update_account_balance(account):
    account.update_balance()
    update_account(account, {'balance': account.balance,
                             'last_update_date': account.last_update_date})


def update_all_accounts():
    for account in get_all_accounts():
        update_account_balance(account)
