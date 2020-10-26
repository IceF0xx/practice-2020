from Database.models.groups import Groups
from Database.models.students import Students
from Database.models.teachers import Teachers
from Database.models.users import Users
from .config import metadata, engine, Base


def init():
    Base.metadata.create_all(engine)
