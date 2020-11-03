from sqlalchemy import Column, Integer, String

from Database.config import Base
from ..config import __tables


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    role = Column(Integer)


__tables[Users.__tablename__] = Users
