from sqlalchemy import Column, Integer, String, Boolean

from Database.config import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    is_admin = Column(Boolean)
