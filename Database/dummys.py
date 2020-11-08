from datetime import date

from .utils import exec, Operation


def fill_groups():
    groups = [
        [0, '32927/1'],
        [1, '42927/1'],
        [2, '42927/2'],
        [3, '42927/3'],
        [4, '32927/2'],
    ]
    try:
        for g in groups:
            exec(Operation.insert, 'groups', g)
    except Exception as e:
        print(e)


def fill_parents():
    parents = [
        [0, 'Foo', 'Bar', '', False, 'Mobile: 8-999-209-33-12'],
        [1, 'Michael', 'Barr', 'Johnson', True, 'Mobile: 8-800-555-35-35'],
        [2, 'Jeffrey', 'Epstein', '', True, 'Did not kill him self'],
        [3, 'Daenerys', 'Targaryen', '', False, 'Mother of dragons'],
        [4, 'Sakurajima', 'Mai', '', False, 'The actress, number: 8-800-400-31-32'],
        [5, 'Naruto', 'Uzumaki', '', True, 'Future Hokage'],
        [6, 'Some', 'Other', 'Name', True, 'Does not have any mobile phone'],
    ]
    try:
        for p in parents:
            exec(Operation.insert, 'parents', p)
    except Exception as e:
        print(e)


def fill_students():
    students = [
        [0, 0, 'John', 'Doe', 'Empty', True, date(2001, 2, 3), '4871  Losh Lane', '+36 55 079 621', 0],
        [1, 1, 'Donatas', 'Wandal', 'Piraino', True, date(2001, 11, 15), '3433  Park Avenue', '+36 55 677 387', 1],
        [2, 2, 'Atem', 'Merla', 'Kovačić', True, date(2000, 1, 23), '1647  Tibbs Avenu', '+36 55 360 568', 2],
        [3, 3, 'Helene', 'Debdas', 'Kozioł', True, date(2002, 5, 16), '3934  Bicetown Road', '+36 55 545 691', 4],
        [4, 4, 'László', 'Bandi', 'Kalmár', True, date(2000, 2, 5), '3401  Hiney Road', '+36 55 050 209', 1],
        [5, 5, 'Nimród', 'Lívia', 'Novák', True, date(2000, 9, 11), '3246  Oliver Street', '+36 55 067 771', 2],
        [6, 6, 'Kanako', 'Takashi', '', True, date(2000, 8, 2), '3764  Holly Street', '503-427-6425', 3],
        [7, 7, 'Saori', 'Miku', '', True, date(2000, 8, 3), '4073  Melm Street', '817-317-1719', 4],
        [8, 8, 'Mao', 'Ryota', '', False, date(2001, 9, 23), '4128  Chapmans Lan', '203-525-3144', 1],
        [9, 9, 'Charmaine', 'B', 'McClain', False, date(2000, 7, 14), '4787  Ethels Lane', '561-288-3164', 3],
        [10, 10, 'Cathie', 'A', 'Crockett', False, date(1999, 10, 13), '4073  Melm Street', '505-779-473', 2],
    ]

    try:
        for s in students:
            exec(Operation.insert, 'students', s)
    except Exception as e:
        print(e)


def fill_pivot():
    rels = [
        [0, 0, 0],
        [1, 7, 3],
        [2, 1, 2],
        [3, 7, 6],
        [4, 3, 1],
        [5, 4, 1],
        [6, 6, 3],
        [7, 1, 2],
        [8, 6, 5],
        [9, 9, 3],
        [10, 10, 1],
        [11, 1, 0],
        [12, 3, 4],
        [13, 2, 2],
        [14, 8, 1],
        [15, 8, 2],
    ]

    try:
        for r in rels:
            exec(Operation.insert, 'students-parents', r)
    except Exception as e:
        print(e)


def fill_users():
    users = [
        [0, 'miko', 0],
        [1, 'azure', 1],
        [2, 'alexcher', 3],
        [3, 'asper', 3],
    ]

    try:
        for u in users:
            exec(Operation.insert, 'users', u)
    except Exception as e:
        print(e)
