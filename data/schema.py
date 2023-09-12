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
            UNIQUE(api_key) 
        );'''
        cur.execute(SQL)

        # LOCATIONS TABLE
        cur.execute(DROPSQL.format(tablename="locations"))
        SQL = '''CREATE TABLE locations (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            brand VARCHAR, 
            name VARCHAR, 
            city VARCHAR,
            address VARCHAR,
            website VARCHAR
        );'''
        cur.execute(SQL)

        # BATCHES TABLE
        cur.execute(DROPSQL.format(tablename="batches"))
        SQL = '''CREATE TABLE batches (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            status VARCHAR NOT NULL,
            run_time TEXT,
            error_details TEXT
        );'''
        cur.execute(SQL)

        # TITLES TABLE
        cur.execute(DROPSQL.format(tablename="titles"))
        SQL = '''CREATE TABLE titles (
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
        );'''
        cur.execute(SQL)

        # SHOWINGS TABLE
        cur.execute(DROPSQL.format(tablename="showings"))
        SQL = '''CREATE TABLE showings (
            pk INTEGER PRIMARY KEY AUTOINCREMENT, 
            location_id INTEGER,
            title_id INTEGER,
            batch_id INTEGER,
            start_time TEXT,
            end_time TEXT,
            FOREIGN KEY (location_id) REFERENCES locations(pk), 
            FOREIGN KEY (title_id) REFERENCES titles(pk),
            FOREIGN KEY (batch_id) REFERENCES batches(pk)
        );'''
        cur.execute(SQL)