from sqlalchemy import Column, String, ForeignKey

from Database.config import Base
from ..config import __tables


class Groups(Base):
    __tablename__ = 'groups'

    id = Column(String, ForeignKey('students.group_id'), primary_key=True)
    specialization = Column(String)

    def __repr__(self):
        return f'<Group(id={self.id}, specialization={self.specialization})>'


__tables[Groups.__tablename__] = Groups
