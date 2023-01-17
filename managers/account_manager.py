from db.session import session
from uuid import uuid4, UUID
from models.account import SavingsAccount, PersonalAccount
from managers.client_manager import ClientManager


class AccountManager:
    @staticmethod
    def create_savings_account(balance, owner, rate):
        account = SavingsAccount(balance, owner, rate=rate)
        session.execute(
            f"""
            INSERT INTO accounts(account_id, balance, owner_id, type, rate,
            last_update_date) VALUES ({account.id}, {account.balance}, {account.owner.id},
            '{account.type}', {account.rate},'{account.last_update_date}');
            """
        )
        return account


    @staticmethod
    def create_personal_account(balance, owner):
        account = PersonalAccount(balance, owner)
        session.execute(
            f"""
            INSERT INTO accounts(account_id, balance, owner_id, type)
            VALUES ({account.id}, {account.balance},
            {account.owner.id}, '{account.type}');
            """
        )
        return account


    @staticmethod
    def get_account(id):
        result = session.execute(f"SELECT * FROM accounts WHERE account_id = {UUID(id)};")[0]
        account = create_from_row(result)
        return account


    @staticmethod
    def get_all_accounts():
        results = session.execute("SELECT * FROM accounts;")
        accounts = [create_from_row(result) for result in results]
        return accounts


    @staticmethod
    def delete_account(id):
        session.execute(f"DELETE FROM accounts WHERE account_id = {id};")


    @staticmethod
    def update_account(account):
        if account.type == 'savings_account':
            session.execute(
                f"""
                UPDATE accounts SET balance = {account.balance}, owner_id = {account.owner.id},
                type = '{account.type}', rate = {account.rate},
                last_update_date = '{account.last_update_date}' WHERE account_id = {account.id};
                """
            )
        else:
            session.execute(
                f"""
                UPDATE accounts SET balance = {account.balance}, owner_id = {account.owner.id},
                type = {account.type} WHERE account_id = {account.id};
                """
            )


    @staticmethod
    def update_account_balance(account):
        account.update_balance()
        if account.type == 'savings_account':
            AccountManager.update_account(account)

    @staticmethod
    def update_all_accounts():
        for account in AccountManager.get_all_accounts():
            AccountManager.update_account_balance(account)


def create_from_row(account):
    owner = ClientManager.get_client(account.owner_id)

    if account.type == 'savings_account':
        return SavingsAccount(account.balance, owner, account.rate, id=account.account_id)
    return PersonalAccount(account.balance, owner, id=account.account_id)
