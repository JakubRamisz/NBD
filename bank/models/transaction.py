import enum
from datetime import datetime
from sqlalchemy import Column, Integer, Enum, DateTime, Numeric
from models.base import Base


class TransactionTypes(enum.Enum):
    withdrawal = 1
    deposit = 2
    transfer_to = 3
    transfer_from = 4


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    amount = Column(Numeric)
    transaction_type = Column(Enum(TransactionTypes))


    def __init__(self, amount, transaction_type, date=None):
        self.amount = amount
        self.transaction_type = transaction_type
        if date is None:
            self.date = datetime.now()
        else:
            self.date = date
