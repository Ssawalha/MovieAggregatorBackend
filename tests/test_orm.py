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

    def test_one_from_where_clause(self):
        test_row = MockTable.one_from_where_clause("WHERE A = ?",("a1",))
        self.assertIsInstance(test_row, MockTable,"Check that a MockTable object is returned")
        self.assertEqual(test_row['A'], 'a1', "Check that field A has the value we are expecting from our seed")
        self.assertEqual(test_row['B'], 123.50, "Check that field B has the value we are expecting from our seed")
        self.assertEqual(test_row['C'], "hello world!","Check that field C has the value we are expecting from our seed")

if __name__ == '__main__':
    unittest.main()