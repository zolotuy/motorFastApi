from car import Car


class Salon:
    cars = [Car(1, "car1", 100), Car(2, "car2", 200), Car(3, "car3", 300)]

    def __init__(self) -> None:
        super().__init__()

    def get_all_cars(self):
        cars = self.cars
        return self.cars

    def get_car_by_name(self, name):
        for car in self.cars:
            if car.name == name:
                return car

    def get_car_by_id(self, id):
        for car in self.cars:
            if car.id == id:
                return car

    def add_car(self, name, speed):
        max_id = 0
        for car in self.cars:
            if car.id > max_id:
                max_id = car.id
        max_id += 1
        new_car = car(max_id, name, speed)
        self.cars.append(new_car)
        return self.get_car_by_id(max_id)

    def update_car(self, id, name, speed):
        for car in self.cars:
            if car.id == id:
                car.name = name
                car.speed = speed
        return self.get_car_by_id(id)

    def delete_car_by_id(self, id):
        print(id)
        car = self.get_car_by_id(id)
        print(car)
        if car is not None:
            self.cars.remove(car)
            return True
        else:
            return False

    def __repr__(self):
        return str(self.__dict__)
