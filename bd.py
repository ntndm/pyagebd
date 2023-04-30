import sqlite3

con = sqlite3.connect('agenda.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_time TEXT NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )""")
con.commit()

con.close()
