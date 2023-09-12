from collections import OrderedDict
from model.orm import ORM

class Batch(ORM):
    '''Python class which inherits from the class ORM.\n
    Showing represents a single record, which contains:\n
    pk - PRIMARY KEY | database primary key, autoincrements\n
    status -  VARCHAR NOT NULL | Successful or Failure\n
    run_time - TEXT | Time of batch run\n
    error_details - TEXT | What went wrong?\n
    '''

    tablename = "batches"
    fields = ['pk','status','run_time','error_details']

    createsql = '''CREATE TABLE {} (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        status VARCHAR NOT NULL,
        run_time TEXT,
        error_details TEXT
    );'''.format(tablename)

    def __init__(self, **kwargs):
        self.values = OrderedDict()
        self.values['pk'] = kwargs.get('pk')
        self.values['status'] = kwargs.get('status')
        self.values['run_time'] = kwargs.get('run_time')
        self.values['error_details'] = kwargs.get('error_details')

    def __repr__(self):
        msg = '<Batch pk:{pk}, status:{status}>'
        return msg.format(**self.values)

    # @classmethod
    # def all_with_brand(cls, brand):
    #     '''return all Location rows for a brand'''
    #     return cls.all_from_where_clause('WHERE brand = ?', (brand,))

    # all with location_id
    # all with title_id
    # all with batch_id
    # all with title_id after x time
    # all with title_id before x time
    # all with title_id between x time and y time