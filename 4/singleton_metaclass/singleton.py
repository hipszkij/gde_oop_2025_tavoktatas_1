#A metaclass segítségével a Singleton mintát közvetlenül az osztály definiálásakor vezérelhetjük.
# A metaclasses olyan osztályok, amelyek más osztályokat hoznak létre.
# Ezzel egy központi helyen megvalósítható az összes példány kezelése.

#A SingletonMeta metaclass tárolja az _instances dictionary-ben az osztály példányait.
class Singleton(type):
    _instances = {}

    #Az __call__ metódus felelős az osztályok példányosításáért.
    # Ha az adott osztálynak még nincs példánya az _instances dictionary-ben,
    # akkor új példányt hoz létre és eltárolja.
    # Ha már létezik, akkor visszaadja a korábban létrehozott példányt.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CarRegistry(metaclass=Singleton):
    def __init__(self):
        self.cars = {}

    def register_car(self, owner, make, model):
        self.cars[owner] = {"make": make, "model": model}

    def get_car_details(self, owner):
        return self.cars.get(owner, "No car registered for this owner.")

# Usage
registry1 = CarRegistry()
registry1.register_car("John Doe", "Toyota", "Corolla")

registry2 = CarRegistry()
registry2.register_car("John Smith", "Toyota", "Yaris")

print(registry1 is registry2)  # Output: True

print(registry2.get_car_details("John Smith"))  # Output: {'make': 'Toyota', 'model': 'Corolla'}
