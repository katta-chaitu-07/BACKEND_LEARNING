

from fastapi import FastAPI,HTTPException

app = FastAPI()


products = [
    {
        "id" : 1,
        "name" : "Laptop",
        "price" : 125000
    },
    {
        "id":2,
        "name":"phone",
        "price": 35000
    }
]

@app.get("/products/{product_id}")
def get_products(product_id : int):

    for product in products:

        if product["id"] == product_id :

            return product

    raise HTTPException(
        status_code = 404,
        detail = "product not found"
            )