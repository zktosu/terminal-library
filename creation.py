import sqlite3

DB_NAME = "database.db"
con = sqlite3.connect(DB_NAME)
# create books table 
books_table = """
CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
author TEXT NOT NULL,
is_issued BOOLEAN 
)
"""
cur = con.cursor()
cur.execute(books_table)
con.close()
