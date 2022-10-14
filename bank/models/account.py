from datetime import datetime
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    account_number = Column(String)
    balance = Column(Numeric)
    owner_id = Column(Integer, ForeignKey('clients.id'))
    owner = relationship('Client', backref='account')

    type = Column(String)

    __mapper_args__ = {
        'polymorphic_on': 'type',
        'polymorphic_identity': 'account',
    }


    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance


class PersonalAccount(Account):
    __mapper_args__ = {
        'polymorphic_identity': 'personal_account',
    }


class SavingsAccount(Account):
    rate = Column(Numeric)
    last_update_date = Column(DateTime, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'savings_account',
    }

    def __init__(self, account_number, owner, balance, rate):
        super().__init__(account_number, owner, balance)

        self.rate = rate
        self.last_update_date = self.date = datetime.now()
