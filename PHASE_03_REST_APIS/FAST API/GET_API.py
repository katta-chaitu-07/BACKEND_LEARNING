
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

