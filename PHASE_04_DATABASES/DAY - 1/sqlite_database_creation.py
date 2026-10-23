import sqlite3 as sq

connection = sq.connect("products.db")

print("Database is successfully connected")

connection.close()