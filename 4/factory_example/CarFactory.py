from Sedan import Sedan
from SUV import SUV
from Truck import Truck


class CarFactory:
    def __init__(self):
        pass

    def create_car(self, object_type, brand, type, color, year):
        if object_type == 'Sedan':
            return Sedan(brand, type, color, year)
        elif object_type == 'SUV':
            return SUV(brand, type, color, year)
        elif object_type == 'Truck':
            return Truck(brand, type, color, year)
