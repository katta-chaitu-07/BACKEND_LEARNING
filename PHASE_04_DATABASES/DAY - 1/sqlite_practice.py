import sqlite3 as sq

connection  = sq.connect("ecommerce.db")

print("Database conncection is success")

cursor = connection.cursor()

#step -1 :- creating the table products
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
      ID INTEGER PRIMARY KEY,
      NAME TEXT NOT NULL,
      PRICE REAL NOT NULL,
      QUANTITY INTEGER NOT NULL
    )
    """
)

connection.commit()

print("Products table created sucessfully")

#step 2:- insert 



cursor.execute(""" SELECT *FROM products WHERE PRICE > ?""",(50000,))

print(cursor.fetchall())