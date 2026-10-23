import sqlite3 as sq

connection = sq.connect("ecommerce.db")

cursor = connection.cursor()


cursor.execute("""
      SELECT *FROM products;
""")

products = cursor.fetchall()

for product in products:
    print(product)



connection.close()