from db import get_collection
from models.client import Client
from models.account import SavingsAccount, PersonalAccount, Account


def add_savings_account(account_number, owner, rate):
    collection = get_collection('accounts')
    if collection.find_one({'account_number': account_number}) is not None:
        print('Given account number already exists.')
        return

    account = SavingsAccount(account_number, owner, 0, rate)
    collection.insert_one(account.get_dictionary())


def add_personal_account(account_number, owner):
    collection = get_collection('accounts')
    if collection.find_one({'account_number': account_number}) is not None:
        print('Given account number already exists.')
        return

    account = PersonalAccount(account_number, owner, 0)
    collection.insert_one(account.get_dictionary())


def get_account(account_number):
    collection = get_collection('accounts')
    result = collection.find_one({'account_number': account_number})
    return Account(**result)


# def update_account_balance(account):
#     with Session() as session:
#         account.update_balance()
#         session.commit()


# def update_all_accounts():
#     with Session() as session:
#         for account in session.query(Account).all:
#             update_account_balance(account)
#         session.commit()
