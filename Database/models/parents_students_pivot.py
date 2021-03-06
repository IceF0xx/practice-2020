from sqlalchemy import Column, Integer, ForeignKey

from Database.config import Base, __tables


class Pivot(Base):
    __tablename__ = 'students-parents'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    parent_id = Column(Integer, ForeignKey('parents.id'))


__tables['students-parents'] = Pivot
