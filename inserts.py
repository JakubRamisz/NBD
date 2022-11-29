from models.client import Client
from models.account import PersonalAccount, SavingsAccount
from models.transaction import Transaction, TransactionTypes


def main():    
    # for acc in get_all_accounts():
    #     delete_account(acc._id)

    # for trs in get_all_transactions():
    #     delete_transaction(trs._id)

    cl = Client(first_name='Jan', last_name='Kowalski')
    acc1 = PersonalAccount(account_number='123', client_id=cl.pk)
    t1 = Transaction(amount=10, transaction_type=TransactionTypes.deposit, account_id=acc1.pk)
    acc2 = SavingsAccount(account_number='456', client_id=cl.pk, rate=0.1)
    # deposit(acc1, 100)
    # transfer(acc1, acc2, 50)
    # for acc in get_all_accounts():
    #     print(acc)

    # for trs in get_all_transactions():
    #     print(trs)

    cl.save()
    acc1.save()
    acc2.save()
    t1.save()


if __name__ == '__main__':
    main()
