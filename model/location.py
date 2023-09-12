from collections import OrderedDict
from model.orm import ORM

class Location(ORM):
    '''Python class which inherits from the class ORM.\n
    Location represents a single record, which contains:\n
    pk - PRIMARY KEY | database primary key, autoincrements\n
    brand - VARCHAR | name of brand\n
    name - VARCHAR | name of location\n
    city - VARCHAR | the city of the location\n
    address - VARCHAR | the address of the location\n
    website - VARCHAR | the url of the location website
    '''

    tablename = "locations"
    fields = ['pk','brand','name','city','address','website']

    createsql = '''CREATE TABLE {} (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        brand VARCHAR, 
        name VARCHAR, 
        city VARCHAR,
        address VARCHAR,
        website VARCHAR
    );'''.format(tablename)

    def __init__(self, **kwargs):
        self.values = OrderedDict()
        self.values['pk'] = kwargs.get('pk')
        self.values['brand'] = kwargs.get('brand')
        self.values['name'] = kwargs.get('name')
        self.values['city'] = kwargs.get('city')
        self.values['address'] = kwargs.get('address')
        self.values['website'] = kwargs.get('website')

    def __repr__(self):
        msg = '<Location pk:{pk} brand:{brand}, name:{name}, city:{city}>'
        return msg.format(**self.values)

    @classmethod
    def all_with_brand(cls, brand):
        '''return all Location rows for a brand'''
        return cls.all_from_where_clause('WHERE brand = ?', (brand,))