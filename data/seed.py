from datetime import datetime
from constants import DBPATH

from model.orm import ORM
from model.user import User
from model.location import Location
from model.batch import Batch
from model.title import Title
from model.showing import Showing

def seed(dbpath=DBPATH):
    ORM.dbpath = DBPATH

    # CREATE ROW FOR USER
    default = User(username='default', first='john',last='doe',api_key='a1b2c3')
    default.set_password('123')
    try:
        default.save()
    except Exception as e:
        print('Failed to add user:', str(e))

    # CREATE ROWS FOR LOCATIONS
    default = Location(brand='brand_a', name='a', city='city',address='123 xyz',website='www.brand_a.com')
    try:
        default.save()
    except Exception as e:
        print('Failed to add location:', str(e))

    default = Location(brand='brand_b', name='b', city='city',address='456 zyx',website='www.brand_b.com')
    try:
        default.save()
    except Exception as e:
        print('Failed to add location:', str(e))

    default = Location(brand='brand_a', name='second location', city='city',address='456 zyx',website='www.brand_a.com')
    try:
        default.save()
    except Exception as e:
        print('Failed to add location:', str(e))

    # CREATE ROW FOR BATCH
    default = Batch(status='successful', run_time=str(datetime.now()), error_details="")
    try:
        default.save()
    except Exception as e:
        print('Failed to add Batch:', str(e))

    # CREATE ROWS FOR TITLES
    default = Title(title='movie a',batch_id=1,language='english',age_rating='PG-13',description='Movie A')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Title:', str(e))

    default = Title(title='movie b',batch_id=1,language='english',age_rating='PG-13',description='Movie B')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Title:', str(e))

    default = Title(title='movie c',batch_id=2,language='english',age_rating='PG-13',description='Movie C')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Title:', str(e))

    # CREATE ROWS FOR SHOWINGS
    default = Showing(title_id=1,location_id=1,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

    default = Showing(title_id=1,location_id=2,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

    default = Showing(title_id=1,location_id=1,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

    default = Showing(title_id=2,location_id=1,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

    default = Showing(title_id=2,location_id=2,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

    default = Showing(title_id=2,location_id=3,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

    default = Showing(title_id=3,location_id=1,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

    default = Showing(title_id=3,location_id=2,batch_id=1,start_time='',end_time='')
    try:
        default.save()
    except Exception as e:
        print('Failed to add Showing:', str(e))

if __name__ == "__main__":
    seed()

