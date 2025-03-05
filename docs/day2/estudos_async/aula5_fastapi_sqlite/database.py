import sqlite3

conn = sqlite3.connect('base.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS pessoas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT
               );
               """)

pessoas = [
    {'name': 'Joao'},
    {'name': 'Marcos'},
    {'name': 'Carlos'},
]

cursor.executemany("""
INSERT INTO pessoas (name)
                   VALUES (:name)""", pessoas)
conn.commit()
