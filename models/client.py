from sqlalchemy import Column, Integer, String
from models.base import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
