# import statement
from fastapi import FastAPI

from model import Product

from database import engine ,SessionLocal

import database_model

# object creation
app = FastAPI()

# database connection

print("Database URL:", engine.url.database)

print("Registered tables:", database_model.Base.metadata.tables.keys())

database_model.Base.metadata.create_all(bind=engine)

from sqlalchemy import text

with engine.connect() as conn:

    result = conn.execute(
        text("""
            SELECT
                current_database(),
                current_schema(),
                current_user,
                inet_server_addr(),
                inet_server_port()
        """)
    )

    print("PostgreSQL connection details:", result.fetchone())

    result = conn.execute(
        text("""
            SELECT table_schema, table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
    )

    print("Tables in public schema:", result.fetchall())

print("Table creation completed!")

# HTTP method
@app.get("/")
def greet():
    return "Welcome to the FastAPI ...!"


products =[

    Product(id = 1,name = "Laptop", price = 135000 , quantity = 25, description = "Gaming laptap under budget "),

    Product(id = 2 , name = "Mobile Phone" , price = 50000 , quantity = 100 , description = "Gaming mobile")
]

@app.get("/products")
def get_products():

    return products