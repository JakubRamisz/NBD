from datetime import datetime, timedelta
from dataclasses import dataclass
from models.client import Client

@dataclass
class Account:
    _id: str
    account_number: str
    balance: float
    owner: Client

    def __init__(self, _id, account_number, owner, balance):
        self._id = _id
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def update_account(self):
        pass

    def update_balance(self):
        pass

    def get_dictionary(self):
        dict = {
            'account_number': self.account_number,
            'balance': self.balance,
            'owner': self.owner.get_dictionary()
        }
        return dict


@dataclass
class PersonalAccount(Account):
    def __init__(self, _id, account_number, owner, balance):
        super().__init__(_id, account_number, owner, balance)


@dataclass
class SavingsAccount(Account):
    rate: float
    last_update_date: datetime

    def __init__(self, _id, account_number, owner, balance, rate):
        super().__init__(_id, account_number, owner, balance)

        self.rate = rate
        self.last_update_date = self.date = datetime.now()

    def update_account(self):
        self.last_update_date = datetime.now()

    def update_balance(self):
        if datetime.now() - self.last_update_date >= timedelta(days=30):
            self.balance = self.balance * (self.rate + 1)
            self.update_account()

    def get_dictionary(self):
        dict = {
            'account_number': self.account_number,
            'balance': self.balance,
            'owner': self.owner.get_dictionary(),
            'rate': self.rate,
            'last_update_date': self.last_update_date
        }
        return dict
