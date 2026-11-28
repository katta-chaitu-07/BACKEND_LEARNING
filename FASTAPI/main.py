# Import statements
from fastapi import FastAPI, Depends

from model import Product
from database import engine, SessionLocal
import database_model

from sqlalchemy.orm import Session

# Object creation
app = FastAPI()

# Database connection information
print("Database URL:", engine.url.database)

print("Registered tables:", database_model.Base.metadata.tables.keys())

# Create database tables
database_model.Base.metadata.create_all(bind=engine)


# HTTP method
@app.get("/")
def greet():
    return "Welcome to the FastAPI ...!"


# Initial products
products = [
    Product(
        id=1,
        name="Laptop",
        price=135000,
        quantity=25,
        description="Gaming laptop under budget"
    ),

    Product(
        id=2,
        name="Mobile Phone",
        price=50000,
        quantity=100,
        description="Gaming mobile"
    )
]


# Initialize database
def init_db():

    db = SessionLocal()

    try:

        count = db.query(database_model.Product).count()

        if count == 0:

            for product in products:

                db.add(
                    database_model.Product(**product.model_dump())
                )

            db.commit()

    finally:
        db.close()


init_db()


# Database dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# GET all products
@app.get("/products")
def get_products(db: Session = Depends(get_db)):

    db_products = db.query(database_model.Product).all()

    return db_products