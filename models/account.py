from uuid import uuid4, UUID
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from models.client import Client

@dataclass
class Account:
    account_number: str
    balance: float
    owner: Client
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

    def get_dictionary(self):
        dict = {
            '_id': str(self._id),
            'account_number': self.account_number,
            'balance': self.balance,
            'owner': self.owner.get_dictionary()
        }
        return dict


@dataclass
class PersonalAccount(Account):
    pass


@dataclass
class SavingsAccount(Account):
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
            '_id': str(self._id),
            'account_number': self.account_number,
            'balance': self.balance,
            'owner': self.owner.get_dictionary(),
            'rate': self.rate,
            'last_update_date': self.last_update_date
        }
        return dict
