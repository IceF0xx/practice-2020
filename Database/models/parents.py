from sqlalchemy import Column, String, Boolean, Text, Integer
from ..config import tables
from Database.config import Base


class Parents(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)  # Имя
    second_name = Column(String, nullable=False)  # Фамилия
    last_name = Column(String)  # Отчество
    sex = Column(Boolean)
    description = Column(Text)

    def __repr__(self):
        return f"<Teacher(ID={self.id}, First Name={self.first_name})>"

tables[Parents.__tablename__] = Parents
