import enum
from datetime import datetime
from sqlalchemy import Column, Integer, Enum, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship


class TransactionTypes(enum.Enum):
    withdrawal = 1
    deposit = 2
    transfer_to = 3
    transfer_from = 4


class Transaction:
    __tablename__ = 'transactions'

    date: datetime
    amount: int
    transaction_type: enum.Enum(TransactionTypes)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', backref='transaction')

    def __init__(self, amount, transaction_type, account, date=None):
        self.amount = amount
        self.transaction_type = transaction_type
        self.account = account
        if date is None:
            self.date = datetime.now()
        else:
            self.date = date
