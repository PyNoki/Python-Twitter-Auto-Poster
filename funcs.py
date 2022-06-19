import sqlite3
import random
from pprint import pprint

# create table with names and types
def create_table():
    
    conn = sqlite3.connect('pictures.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS pictures(
        id integer PRIMARY KEY autoincrement NOT NULL,
        datetimetext text,
        picture text UNIQUE
        )""")

create_table()