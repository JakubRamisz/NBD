import enum
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4, UUID
from models.account import PersonalAccount, SavingsAccount, Account


class TransactionTypes(enum.Enum):
    withdrawal = 1
    deposit = 2
    transfer_to = 3
    transfer_from = 4


@dataclass
class Transaction:
    amount: int
    transaction_type: TransactionTypes
    account: Account
    date: datetime = datetime.now()
    _id: uuid4 = field(default_factory=uuid4)

    def __post_init__(self):
        if isinstance(self.account, dict):
            if self.account['type'] == 'savings_account':
                self.account = SavingsAccount(**self.account )
            else:
                self.account = PersonalAccount(**self.account )

        if isinstance(self.date, dict):
            self._id = datetime(self._id)

        if isinstance(self._id, dict):
            self._id = UUID(self._id)


    def get_dictionary(self):
        dict = {
            'amount': self.amount,
            'transaction_type': str(self.transaction_type),
            'account': self.account.get_dictionary(),
            'date': str(self.date),
            '_id': str(self._id)
        }
        return dict
