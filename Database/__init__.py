from .config import metadata, engine
from Database.models.students import Students
from Database.models.users import Users


def init():
    if len(metadata.sorted_tables) == 0:
        raise Exception("In __init__.py must be included tables")
    metadata.create_all(engine)