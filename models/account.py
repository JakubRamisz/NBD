from uuid import uuid4, UUID
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import ClassVar
from models.client import Client

@dataclass
class Account:
    account_number: str
    balance: float
    owner: Client
    type: ClassVar
    _id: uuid4 = field(default_factory=uuid4)

    def __post_init__(self):
        if isinstance(self.owner, dict):
            self.owner = Client(**self.owner)

        if isinstance(self._id, dict):
            self._id = UUID(self._id)


    def update_account(self):
        pass

    def update_balance(self):
        pass

    def dict(self):
        result = {
            '_id': str(self._id),
            'account_number': self.account_number,
            'balance': self.balance,
            'owner': self.owner.dict(),
            'type': self.type
        }
        return result


@dataclass
class PersonalAccount(Account):
    type: str = 'personal_account'


@dataclass
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

    def dict(self):
        result = {
            '_id': str(self._id),
            'account_number': self.account_number,
            'balance': self.balance,
            'owner': self.owner.dict(),
            'type': self.type,
            'rate': self.rate,
            'last_update_date': str(self.last_update_date)
        }
        return result
