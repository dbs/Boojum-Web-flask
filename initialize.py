#!/usr/bin/env python3

"""
Create the PostgreSQL database for querying technical reports
"""

import postgresql

DB_NAME = 'boojum'
DB_HOST = 'localhost' 
DB_USER = 'boojum'

DB = postgresql.open(host=DB_HOST, database=DB_NAME, user=DB_USER)

def init_db():
    """ Initialize the database """
    DB.execute("DROP TABLE IF EXISTS reports")
    DB.execute("""
        CREATE TABLE reports (id SERIAL,
                              title TEXT,
                              author TEXT,
                              pubdate DATE,
                              description TEXT,
                              handle TEXT, 
                              file TEXT)
    """)

if __name__ == "__main__":
    init_db()

