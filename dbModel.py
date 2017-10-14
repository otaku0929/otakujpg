from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DB_connect = 'postgres://rjrtqczwllnrdw:6f23d3af95bbdd7511cdd1849d3eb712dcc140a0cfe24d12a88643f7d2de0ead@ec2-54-83-205-71.compute-1.amazonaws.com:5432/dehi5aeo5k42th'


class Images(Base):
    __tablename__ = 'Images'

    id = Column(Integer, primary_key=True)
    Url = Column(String)
    CreateDate = Column(DateTime(timezone=True), server_default=func.now())


if __name__ == '__main__':
    engine = create_engine(DB_connect)
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
