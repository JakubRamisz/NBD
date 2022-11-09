from managers.account_management import add_personal_account, add_savings_account, get_account
from models.client import Client


def main():

    client = Client('Jan', 'Kowalski')
    add_personal_account('123', client)
    add_savings_account('456', client, 0.1)
    print(get_account('123'))


if __name__ == '__main__':
    main()
