class Car:
    id: int
    name: str
    speed: int

    def __init__(self, id, name, speed):
        self.id = id
        self.name = name
        self.speed = speed

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'speed': self.speed
        }

    def __repr__(self):
        return str(self.__dict__)
