from sqlalchemy import Column, Integer, String, Boolean, Date, Text, Table
from Database.config import metadata

Students = Table('students', metadata,
    Column('student_id', Integer, primary_key=True),
    Column('record_id', Integer, unique=True),
    Column('first_name', String, nullable=False),       # Имя
    Column('second_name', String, nullable=False),      # Фамилия
    Column('last_name', String),                        # Отчество
    Column('sex', Boolean),
    Column('dob', Date),
    Column('address', String),
    Column('phone', String),
    Column('parents', Text),
)