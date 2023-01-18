from datetime import datetime
from uuid import uuid4, UUID


class Transaction:
    def __init__(self, account, amount, transaction_type, date=datetime.now(), id=uuid4()):
        self.amount = amount
        self.transaction_type = transaction_type
        self.account = account

        if isinstance(date, str):
            self.date = datetime(date)
        else:
            self.date = date

        if isinstance(id, str):
            self.id = UUID(id)
        else:
            self.id = id


    def dict(self):
        result = {
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'account': self.account.dict(),
            'date': str(self.date),
            'id': str(self.id)
        }
        return result
