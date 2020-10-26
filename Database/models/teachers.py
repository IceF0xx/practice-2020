from sqlalchemy import Column, String, Boolean, Text, Integer

from Database.config import Base


class Teachers(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)  # Имя
    second_name = Column(String, nullable=False)  # Фамилия
    last_name = Column(String)  # Отчество
    sex = Column(Boolean)
    description = Column(Text)

    def __repr__(self):
        return f"<Teacher(ID={self.id}, First Name={self.first_name})>"
