from sqlalchemy.orm import Session

from Database.models.groups import Groups
from Database.models.parents import Parents
from Database.models.parents_students_pivot import Pivot
from Database.models.students import Students
from Database.models.users import Users
from .config import engine, Base


def init():
    Base.metadata.create_all(engine)
    session = Session(engine)
    return session
