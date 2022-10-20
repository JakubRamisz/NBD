from models.base import Base, engine
from managers.account_management import add_personal_account, add_savings_account
from managers.transaction_management import deposit, transfer
from managers.client_management import add_client


def main():
    Base.metadata.create_all(engine)

    client_id = add_client('Jan', 'Kowalski')
    acc_id1 = add_personal_account('123', client_id)
    acc_id2 = add_savings_account('456', client_id, 0.1)


    deposit(acc_id1, 200)

    transfer(acc_id1, acc_id2, 50)


if __name__ == '__main__':
    main()
