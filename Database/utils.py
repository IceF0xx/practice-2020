from sqlalchemy import select

from .config import tables, engine

def get_table_names():
    return [table for table in tables]


def fetch_data_from_table(table_name) -> dict:
    with engine.connect() as conn:
        q = select([tables[table_name]])
        return {'data':[row for row in conn.execute(q)],
                'columns': tables[table_name].__table__.columns.keys()}
