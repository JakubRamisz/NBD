from models.client import Client
from managers.account_manager import AccountManager
from managers.transaction_manager import TransactionManager


def main():    
    for acc in AccountManager.get_all_accounts():
        AccountManager.delete_account(acc._id)

    for trs in TransactionManager.get_all_transactions():
        TransactionManager.delete_transaction(trs._id)

    client = Client('Jan', 'Kowalski')
    acc1 = AccountManager.add_personal_account('123', client)

    TransactionManager.deposit(acc1, 100)
    TransactionManager.deposit(acc1, 100)
    TransactionManager.deposit(acc1, 100)




if __name__ == '__main__':
    main()
