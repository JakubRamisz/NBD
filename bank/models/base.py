from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://nbd:nbdpassword@127.0.0.1:5432/nbddb',
                        isolation_level='SERIALIZABLE')
Session = sessionmaker(bind=engine)


Base = declarative_base()
