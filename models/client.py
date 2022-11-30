from dataclasses import dataclass


@dataclass
class Client:
    first_name: str
    last_name: str

    def dict(self):
        result = {
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        return result
