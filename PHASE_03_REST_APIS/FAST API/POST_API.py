
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

 
