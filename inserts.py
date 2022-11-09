from models.client import Client
from managers.account_management import add_personal_account, add_savings_account, get_all_accounts, delete_account
from managers.transaction_management import deposit, transfer, get_all_transactions, delete_transaction


def main():    
    for acc in get_all_accounts():
        delete_account(acc._id)

    for trs in get_all_transactions():
        delete_transaction(trs._id)

    client = Client('Jan', 'Kowalski')
    acc1 = add_personal_account('123', client)
    acc2 = add_savings_account('456', client, 0.1)
    deposit(acc1, 100)
    transfer(acc1, acc2, 50)
    for acc in get_all_accounts():
        print(acc)

    for trs in get_all_transactions():
        print(trs)


if __name__ == '__main__':
    main()
