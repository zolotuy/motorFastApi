from fastapi import FastAPI
from pydantic import BaseModel

from salon import Salon


class Car(BaseModel):
    id: int
    name: str
    speed: int


app = FastAPI()

salon = Salon()


@app.get('/')
def get_all_cars():
    return salon.get_all_cars()


@app.get('/{name}')
def get_car_by_name(name: str):
    car = salon.get_car_by_name(name)
    if car is not None:
        return car
    else:
        return "There is no car with name: " + name


@app.post('/addCar')
def add_car(car: Car):
    name = car.name
    speed = car.speed
    return salon.add_car(name, speed)


@app.put('/updateCar')
def update_car(car: Car):
    updated_car = salon.update_car(car.id, car.name, car.speed)
    if updated_car is not None:
        return updated_car
    else:
        return "There is no car with id: " + str(car.id)


@app.delete('/deleteCar/{id}')
def delete_car(id: int):
    is_deleted = salon.delete_car_by_id(id)
    if is_deleted:
        return "car with id = " + str(id) + " was successfully deleted"
    else:
        return "There is no car with id: " + str(id)
