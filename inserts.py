from models.client import Client
from models.account import PersonalAccount, SavingsAccount
from models.transaction import Transaction, TransactionTypes
from managers.account_manager import AccountManager
import json


def main():
    print(AccountManager.get_all_accounts())

if __name__ == '__main__':
    main()
