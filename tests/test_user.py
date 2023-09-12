import os
import unittest

from tests.testing_seed import schema, seed, MockTable, DBPATH
from model.orm import ORM

class TestORM(unittest.TestCase):
    dbpath = DBPATH

    # We want to create a mock database before each test.
    def setUp(self):
        schema(self.dbpath)
        seed(self.dbpath)

    # We want to delete the database at the end of each test.
    def tearDown(self):
        os.remove(self.dbpath)