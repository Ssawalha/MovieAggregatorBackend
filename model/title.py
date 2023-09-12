from collections import OrderedDict
from model.orm import ORM

class Title(ORM):
    '''Python class which inherits from the class ORM.\n
    Showing represents a single record, which contains:\n
    pk - PRIMARY KEY | database primary key, autoincrements\n
    title - VARCHAR | movie title\n
    batch_id - Foriegn Key VARCHAR | pk from batches table\n 
    language - VARCHAR | language of movie audio\n
    age_rating - VARCHAR | age rating of movie\n
    description - TEXT | movie description\n
    image_url - TEXT | movie poster image url\n
    trailer_url - TEXT | movie trailer url\n
    rotten_tomatoes_score - VARCHAR | score of movie on rotten tomatoes\n
    imdb_score - VARCHAR | score of movie on imdb
    '''

    tablename = "titles"
    fields = ['pk','title','batch_id','language','age_rating','description','image_url','trailer_url','rotten_tomatoes_score','imdb_score']

    createsql = '''CREATE TABLE {} (
        pk INTEGER PRIMARY KEY AUTOINCREMENT, 
        title VARCHAR,
        batch_id INTEGER,
        language VARCHAR,
        age_rating VARCHAR,
        description VARCHAR,
        image_url VARCHAR,
        trailer_url VARCHAR,
        rotten_tomatoes_score VARCHAR,
        imdb_score VARCHAR,
        FOREIGN KEY (batch_id) REFERENCES batches(pk)
    );'''.format(tablename)

    def __init__(self, **kwargs):
        self.values = OrderedDict()
        self.values['pk'] = kwargs.get('pk')
        self.values['title'] = kwargs.get('title')
        self.values['batch_id'] = kwargs.get('batch_id')
        self.values['language'] = kwargs.get('language')
        self.values['age_rating'] = kwargs.get('age_rating')
        self.values['description'] = kwargs.get('description')
        self.values['image_url'] = kwargs.get('image_url')
        self.values['trailer_url'] = kwargs.get('trailer_url')
        self.values['rotten_tomatoes_score'] = kwargs.get('rotten_tomatoes_score')
        self.values['imdb_score'] = kwargs.get('imdb_score')

    def __repr__(self):
        msg = '<Title pk:{pk}, title:{title}, batch_id:{batch_id}>'
        return msg.format(**self.values)

    @classmethod
    def all_with_batch_id(cls, batch_id):
        '''return all Showing rows with batch_id (batch_id is a foreign key in this db)'''
        return cls.all_from_where_clause('WHERE batch_id = ?', (batch_id,))
    
    # all with language
    # all with age_rating
    # all with rating higher than
    # all with rating lower than
    # all with batch_id