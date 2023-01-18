from uuid import uuid4, UUID
from datetime import datetime, timedelta


class Account:
    def __init__(self, balance, owner, id=uuid4()):
        self.balance = balance
        self.owner = owner
        if isinstance(id, str):
            self.id = UUID(id)
        else:
            self.id = id

    def update_account(self):
        pass

    def update_balance(self):
        pass

    def dict(self):
        result = {
            'id': str(self.id),
            'balance': self.balance,
            'owner': self.owner.dict()
        }
        return result


class PersonalAccount(Account):
    def __init__(self, balance, owner, id=uuid4()):
        super().__init__(balance, owner, id=id)
        self.type  = 'personal_account'


    def dict(self):
        result = {
            'id': str(self.id),
            'balance': self.balance,
            'owner': self.owner.dict(),
            'type': self.type
        }
        return result


class SavingsAccount(Account):
    def __init__(self, balance, owner, rate, id=uuid4()):
        super().__init__(balance, owner, id=id)
        self.type  = 'savings_account'
        self.rate = rate
        self.last_update_date = datetime.now()


    def update_account(self):
        self.last_update_date = datetime.now()

    def update_balance(self):
        if datetime.now() - self.last_update_date >= timedelta(days=30):
            self.balance = self.balance * (self.rate + 1)
            self.update_account()

    def dict(self):
        result = {
            'id': str(self.id),
            'balance': self.balance,
            'owner': self.owner.dict(),
            'type': self.type,
            'rate': self.rate,
            'last_update_date': str(self.last_update_date)
        }
        return result
