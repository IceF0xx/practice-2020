from sqlalchemy import Column, String, Integer, ForeignKey

from Database.config import Base


class Groups(Base):
    __tablename__ = 'groups'

    id = Column(String, primary_key=True)
    curator_id = Column(Integer, ForeignKey('teachers.id'))
    specialization = Column(String)

    def __repr__(self):
        return f'<Group(id={self.id}, specialization={self.specialization})>'
