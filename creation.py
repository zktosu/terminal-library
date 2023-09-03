import sqlite3

DB_NAME = "database.db"
con = sqlite3.connect(DB_NAME)
# create books table 
books_table = """
CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT NOT NULL,
title TEXT NOT NULL,
is_issued BOOLEAN 
)
"""
con.execute(books_table)

