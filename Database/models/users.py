from sqlalchemy import Column, Integer, String, Boolean
from ..config import tables
from Database.config import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    is_admin = Column(Boolean)

tables[Users.__tablename__] = Users
