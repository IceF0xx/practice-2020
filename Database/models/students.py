from sqlalchemy import Column, Integer, String, Boolean, Date
from ..config import tables
from Database.config import Base


class Students(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    record_id = Column(Integer, unique=True)
    first_name = Column(String, nullable=False)  # Имя
    second_name = Column(String, nullable=False)  # Фамилия
    last_name = Column(String)  # Отчество
    sex = Column(Boolean)
    dob = Column(Date)
    address = Column(String)
    phone = Column(String)
    group_id = Column(String)

    def __repr__(self):
        return f'<Student(ID={self.student_id}, First Name={self.first_name}, Second Name={self.second_name})>'

tables[Students.__tablename__] = Students
