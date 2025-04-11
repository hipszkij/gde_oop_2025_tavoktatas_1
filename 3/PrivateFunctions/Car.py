class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, new_value):
        self._make = new_value

    def to_string(self):
        print(f"Make: {self._make}, Model: {self._model}")


car = Car("Toyota", "Corolla")
car.to_string()
car.set_make("valami")
car.to_string()

print(car.get_make())



