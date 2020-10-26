import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'sqlite:///college.db'

metadata = sa.MetaData()
engine = sa.create_engine(DB_URL)
Base = declarative_base()
