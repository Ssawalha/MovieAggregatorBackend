from constants import DB_TEST_NAME

import os
import sqlite3
from collections import OrderedDict

from model.orm import ORM

DIR = os.path.dirname(__file__)
DBFILENAME = DB_TEST_NAME
DBPATH = os.path.join(DIR, DBFILENAME)

class MockTable(ORM):
    tablename = "mocktable"
    fields = ["A","B","C"]

    createsql = """CREATE TABLE {} (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        A VARCHAR NOT NULL,
        B FLOAT,
        C TEXT
    );""".format(tablename)

    def __init__(self, **kwargs):
        self.values = OrderedDict()
        self.values['pk'] = kwargs.get('pk')
        self.values['A'] = kwargs.get('A')
        self.values['B'] = kwargs.get('B')
        self.values['C'] = kwargs.get('C')
    
    def __repr__(self):
        msg = "<MockTable pk:{pk}, A:{A}, B:{B}, C:{C}>"
        return msg.format(**self.values)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename=MockTable.tablename))
        cur.execute(MockTable.createsql)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath
    test_row = MockTable(A="a1", B=123.50, C="hello world!")
    test_row.save()


if __name__ == "__main__":
    schema()
    seed()
    
