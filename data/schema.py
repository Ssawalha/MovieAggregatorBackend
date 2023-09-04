from constants import DBPATH
import sqlite3

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        # USERS TABLE
        cur.execute(DROPSQL.format(tablename="users"))
        SQL = '''CREATE TABLE users (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR NOT NULL,
            password_hash TEXT,
            first VARCHAR,
            last VARCHAR,
            api_key VARCHAR(256),
            UNIQUE(username),
            UNIQUE(api_key),
        );'''
        cur.execute(SQL)

        # TITLES TABLE
        cur.execute(DROPSQL.format(tablename="titles"))
        SQL = '''CREATE TABLE titles (
            pk INTEGER PRIMARY KEY AUTOINCREMENT, 
            title VARCHAR,
            FOREIGN KEY (batch_id) REFERENCES batches(batch_id) VARCHAR,
            language VARCHAR,
            age_rating VARCHAR,
            description VARCHAR,
            image_url VARCHAR,
            trailer_url VARCHAR,
            rotten_tomatoes_score VARCHAR,
            imdb_score VARCHAR
        );'''
        cur.execute(SQL)

        # SHOWINGS TABLE
        cur.execute(DROPSQL.format(tablename="showings"))
        SQL = '''CREATE TABLE showings (
            pk INTEGER PRIMARY KEY AUTOINCREMENT, 
            FOREIGN KEY (location_id) REFERENCES locations(location_id) VARCHAR, 
            FOREIGN KEY (title_id) REFERENCES titles(title_id) 
            start_time VARCHAR,
            end_time VARCHAR,
            FOREIGN KEY (batch_id) REFERENCES batches(batch_id) VARCHAR
        );'''
        cur.execute(SQL)

        # LOCATIONS TABLE
        cur.execute(DROPSQL.format(tablename="locations"))
        SQL = '''CREATE TABLE accounts (
            pk INTEGER PRIMARY KEY AUTOINCREMENT, 
            brand VARCHAR, 
            name VARCHAR, 
            city VARCHAR,
            address VARCHAR,
            website VARCHAR,
        );'''
        cur.execute(SQL)