import sqlite3

conn = sqlite3.connect("database.db")

print("Sucess")

conn.execute("CREATE TABLE students (name TEXT,addr TEXT,city TEXT,pin TEXT)")

print("table created")

conn.close()