import inspect
from datetime import datetime
from enum import Enum

from sqlalchemy import select, update, delete, insert
from sqlalchemy.inspection import inspect as sq_inspect

from .config import __tables, engine


class Operation(Enum):
    remove = 0
    insert = 1
    update = 2


def get_table_names():
    return __tables


def exec(op: Operation, table_name, *args):
    if op == Operation.remove:
        return __remove_from_table(table_name, *args)
    elif op == Operation.insert:
        return __insert_data_in_table(table_name, *args)
    else:
        return __update_table_value(table_name, *args)


def __remove_from_table(table_name, id_val):
    with engine.connect() as conn:
        table = __tables[table_name]
        id = get_primary_key(table)
        q = delete(table).where(id == id_val)

        conn.execute(q)


def __update_table_value(table_name, data):
    with engine.connect() as conn:
        table = __tables[table_name]
        data['new_value'] = validate_input(data['new_value'])
        id = get_primary_key(table)
        column = get_column(table_name, data['column_name'])
        q = update(table) \
            .where(id == data['id']) \
            .values({column: data['new_value']})
        try:
            conn.execute(q)
        except:
            print('invalid update value')


def __insert_data_in_table(table_name, data):
    with engine.connect() as conn:
        table = __tables[table_name]
        data = list(map(lambda str: validate_input(str), data))
        q = insert(table).values(data)
        conn.execute(q)


def execute_raw_sql(sql_statement: str):
    with engine.connect() as conn:
        try:
            raw_data = conn.execute(sql_statement)
            data = []
            for row in raw_data:
                data.append(list(row))

            tokens = sql_statement.split(' ')
            table_name_pos = tokens.index('from') + 1
            table_name = tokens[table_name_pos]
            return {'data': data, 'tablename': table_name}

        except:
            return {"error": 'true', "message": "invalid syntax"}


def fetch_data_from_table(table_name) -> dict:
    with engine.connect() as conn:
        q = select([__tables[table_name]])
        return {'data': [list(map(lambda v: str(v), row)) for row in conn.execute(q)],
                'columns': __tables[table_name].__table__.columns.keys()}


def get_column(table_name, column_name):
    table = __tables[table_name]
    attrs = inspect.getmembers(table, lambda param: not (inspect.isroutine(param)))
    column = list(filter(lambda a: not a[0].startswith('_')
                                   and a[0] != 'metadata'
                                   and a[0] != 'id'
                                   and a[0] == column_name, attrs))[0][1]

    return column


def get_primary_key(table):
    return sq_inspect(table).primary_key[0]


def validate_input(str) -> object:
    o = __string_to_date(str) or __string_to_bool(str)
    if o:
        return o

    return str


def __string_to_date(s: str):
    try:
        return datetime.strptime(s, '%d/%m/%Y')
    except:
        return None


def __string_to_bool(val):
    if type(val) == str and val.lower() in ['true', 'false']:
        return bool(val)
    return None
