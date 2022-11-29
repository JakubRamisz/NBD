from uuid import uuid4, UUID
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import ClassVar
from redis_om import HashModel


class Account(HashModel):
    account_number: str
    client_id: str
    balance: float = 0

    def update_account(self):
        pass

    def update_balance(self):
        pass

    def get_dictionary(self):
        dict = {
            'account_number': self.account_number,
            'balance': self.balance,
            'client': self.client_id
        }
        return dict


class PersonalAccount(Account):
    type: str = 'personal_account'


class SavingsAccount(Account):
    type: str = 'savings_account'
    rate: float = 0.1
    last_update_date: datetime = datetime.now()

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
            'client': self.client_id,
            'type': self.type,
            'rate': self.rate,
            'last_update_date': self.last_update_date
        }
        return dict
