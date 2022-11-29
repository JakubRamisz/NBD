from dataclasses import dataclass
from redis_om import HashModel



class Client(HashModel):
    first_name: str
    last_name: str

    def get_dictionary(self):
        dict = {
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        return dict
