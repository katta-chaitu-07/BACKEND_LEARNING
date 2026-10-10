from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 25000}
]

# Define the structure of incoming product data
class Product(BaseModel):
    id: int
    name: str
    price: float

# POST: Add a new product
@app.post("/products", status_code=201)
def create_product(product: Product):
    for existing_product in products:
        if existing_product["id"] == product.id:
            return {"message": "Product ID already exists"}

    new_product = product.model_dump()
    products.append(new_product)

    return {
        "message": "Product created successfully",
        "product": new_product
    }