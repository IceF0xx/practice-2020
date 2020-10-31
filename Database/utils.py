import inspect

from sqlalchemy import select, update
from sqlalchemy.inspection import inspect as sq_inspect

from .config import tables, engine


def get_table_names():
    return tables


def fetch_data_from_table(table_name) -> dict:
    with engine.connect() as conn:
        q = select([tables[table_name]])
        return {'data': [list(row) for row in conn.execute(q)],
                'columns': tables[table_name].__table__.columns.keys()}


def update_table_value(table_name, updated_data):
    with engine.connect() as conn:
        table = tables[table_name]
        primary_key = sq_inspect(table).primary_key[0]
        column = get_column(table_name, updated_data['column_name'])

        q = update(table) \
            .where(primary_key == updated_data['id']) \
            .values({column: updated_data['new_value']})

        conn.execute(q)


def get_column(table_name, column_name):
    table = tables[table_name]
    attrs = inspect.getmembers(table, lambda param: not (inspect.isroutine(param)))
    column = list(filter(lambda a: not a[0].startswith('_')
                                   and a[0] != 'metadata'
                                   and a[0] != 'id'
                                   and a[0] == column_name, attrs))[0][1]

    return column
