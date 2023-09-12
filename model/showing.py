from collections import OrderedDict
from model.orm import ORM

class Showing(ORM):
    '''Python class which inherits from the class ORM.\n
    Showing represents a single record, which contains:\n
    pk - PRIMARY KEY | database primary key, autoincrements\n
    title_id - Foreign Key VARCHAR | pk from titles table\n
    location_id - Foreign Key VARCHAR | pk from locations table\n
    batch_id - Foreign Key VARCHAR | pk from batches table\n
    start_time - TEXT | timestamp of the showing's start time\n
    end_time - TEXT | timestamp of the showing's end time
    '''

    tablename = "showings"
    fields = ['pk','title_id','location_id','batch_id','start_time','end_time']

    createsql = '''CREATE TABLE {} (
        pk INTEGER PRIMARY KEY AUTOINCREMENT, 
        location_id INTEGER,
        title_id INTEGER,
        batch_id INTEGER,
        start_time TEXT,
        end_time TEXT,
        FOREIGN KEY (location_id) REFERENCES locations(pk), 
        FOREIGN KEY (title_id) REFERENCES titles(pk),
        FOREIGN KEY (batch_id) REFERENCES batches(pk)
    );'''.format(tablename)

    def __init__(self, **kwargs):
        self.values = OrderedDict()
        self.values['pk'] = kwargs.get('pk')
        self.values['location_id'] = kwargs.get('location_id')
        self.values['title_id'] = kwargs.get('title_id')
        self.values['batch_id'] = kwargs.get('batch_id')
        self.values['start_time'] = kwargs.get('start_time')
        self.values['end_time'] = kwargs.get('end_time')

    def __repr__(self):
        msg = '<Showing pk:{pk}, location_id:{location_id}, title_id:{title_id}, batch_id:{batch_id}>'
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