# NewCar osztály (már kompatibilis az új rendszerrel, van drive() metódusa)

from CarInterface import CarInterface

class NewCar(CarInterface):
    def drive(self):
        print("NewCar: Driving smoothly with modern features.")