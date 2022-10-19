from datetime import datetime, timedelta
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

    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0

    def update_account(self):
        pass

    def update_balance(self):
        pass


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

    def __init__(self, account_number, owner, rate):
        super().__init__(account_number, owner)

        self.rate = rate
        self.last_update_date = self.date = datetime.now()

    def update_account(self):
        self.last_update_date = datetime.now()

    def update_balance(self):
        if datetime.now() - self.last_update_date >= timedelta(days=30):
            self.balance = self.balance * (self.rate + 1)
            self.update_account()
