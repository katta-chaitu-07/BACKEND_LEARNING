<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 25000}
]

# GET: Retrieve all products
@app.get("/products")
def get_products():
    return {"products": products}

# GET: Retrieve a product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}
=======

#import the FastAPI class from the package fastapi

from fastapi import FastAPI


# FastAPI  application instance 

app = FastAPI()  # app is the fast api instance 

vehicle = [
    {
        "Type " : "car",
        "Brand" : "Toyota",
        "Price" : 2500000, 
    },
    {
        "Type " : "Bus",
        "Brand" : "Volvo",
        "Price " : 15000000
    }
]

@app.get("/vehicle")
def vehicle_types():
    return vehicle

>>>>>>> d8c5222 (GET and POST methods are implemented in FAstapi)
