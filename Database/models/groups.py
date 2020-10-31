from sqlalchemy import Column, String, ForeignKey
from ..config import tables
from Database.config import Base

class Groups(Base):
    __tablename__ = 'groups'

    id = Column(String, ForeignKey('students.group_id'), primary_key=True)
    specialization = Column(String)

    def __repr__(self):
        return f'<Group(id={self.id}, specialization={self.specialization})>'

tables[Groups.__tablename__] = Groups
