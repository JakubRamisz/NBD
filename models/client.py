from uuid import uuid4, UUID

class Client:
    def __init__(self, first_name, last_name, id=uuid4()):
        self.first_name = first_name
        self.last_name = last_name
        if isinstance(id, str):
            self.id = UUID(id)
        else:
            self.id = id

    def __dict__(self):
        _dict = {
            'id': str(self.id),
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        return _dict
