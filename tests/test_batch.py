import os
import unittest
from datetime import datetime

# from tests.testing_seed import schema, seed, MockTable, DBPATH
from constants import DB_TEST_NAME
from model.batch import Batch
from model.orm import ORM

class TestBatch(unittest.TestCase):
    dbpath = DB_TEST_NAME
    
    ORM.dbpath = dbpath

    def setUp(self):
        Batch.create_table()
        default = Batch(status="successful", run_time=str(datetime.now()),error_details="")
        default.save()

    def tearDown(self):
        os.remove(self.dbpath)


if __name__ == '__main__':
    unittest.main()