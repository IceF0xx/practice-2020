from Database.config import metadata
from sqlalchemy import Column, Integer, String, Boolean, Table


Users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, unique=True),
    Column('is_admin', Boolean)
)

print(2)