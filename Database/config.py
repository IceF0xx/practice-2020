import sqlalchemy as sa

DB_URL = 'sqlite:///college.db'
metadata = sa.MetaData()
engine = sa.create_engine(DB_URL)
