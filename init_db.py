import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE expenses (
id INTEGER PRIMARY KEY AUTOINCREMENT,
category TEXT,
amount INTEGER,
description TEXT
)
''')

conn.close()

print("Database created")