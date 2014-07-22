import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()
cur.execute('drop table if exists Tracks')
cur.execute('create table Tracks(title text, plays integer)')

conn.close()