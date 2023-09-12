from data.schema import schema
from data.seed import seed

def setup():
    schema()
    seed()
    return None

setup()