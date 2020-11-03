from sqlalchemy import Column, Integer, String, Boolean, Date

from Database.config import Base
from ..config import __tables


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    record_id = Column(Integer, unique=True)
    first_name = Column(String)  # Имя
    second_name = Column(String)  # Фамилия
    last_name = Column(String)  # Отчество
    sex = Column(Boolean)
    dob = Column(Date)
    address = Column(String)
    phone = Column(String)
    group_id = Column(String)

    def __repr__(self):
        return f'<Student(ID={self.id}, First Name={self.first_name}, Second Name={self.second_name})>'


__tables[Students.__tablename__] = Students
