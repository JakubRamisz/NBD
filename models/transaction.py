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
    account_id: str
    date: datetime = datetime.now()

    def get_dictionary(self):
        dict = {
            'amount': self.amount,
            'transaction_type': str(self.transaction_type.name),
            'account': self.account_id,
            'date': str(self.date),

        }
        return dict
