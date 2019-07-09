#!/usr/bin/env python3

"""
Create the PostgreSQL database for querying technical reports
"""

import psycopg2

DB_NAME = 'boojum'
DB_HOST = 'localhost' 
DB_USER = 'boojum'


def init_db():
    """ Initialize the database """
    #conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER)
    conn = psycopg2.connect(database=DB_NAME)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS reports")
    cur.execute("""
        CREATE TABLE reports (id SERIAL,
                              title TEXT,
                              author TEXT,
                              pubdate DATE,
                              description TEXT,
                              handle TEXT, 
                              file TEXT)
    """)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    init_db()

