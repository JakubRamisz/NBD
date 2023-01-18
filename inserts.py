from managers.transaction_manager import TransactionManager
from managers.account_manager import AccountManager
from managers.client_manager import ClientManager

def main():
    for t in TransactionManager.get_all_transactions():
        t.amount = 1000
        TransactionManager.update_transaction(t)
        TransactionManager.delete_transaction(t.id)

if __name__ == '__main__':
    main()
