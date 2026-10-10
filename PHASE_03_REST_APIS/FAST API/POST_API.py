<<<<<<< HEAD
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
=======

from fastapi import FastAPI


app = FastAPI()

vehicle = [
    {
        "id" : 1,
        "Type " : "car",
        "Brand" : "Toyota",
        "Price" : 2500000, 
    },
    {
        "id" : 2,
        "Type " : "Bus",
        "Brand" : "Volvo",
        "Price " : 15000000
    }
]

@app.get("/vehicle")
def get_vehicle():
    return vehicle

@app.post("/vehicle")
def add_vehicles(vehicle_id : dict):
    vehicle.append(vehicle_id)

    return{
        "vehicle_id " : vehicle_id,
        "message" : "vehicle successfully added"
    }

 
>>>>>>> d8c5222 (GET and POST methods are implemented in FAstapi)
