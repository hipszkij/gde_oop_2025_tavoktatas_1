# Adapter osztály (összeköti az OldCar osztályt az új rendszerrel)
from CarInterface import CarInterface

class OldCarAdapter(CarInterface):
    def __init__(self, old_car):
        self.old_car = old_car

    def drive(self):
        # Adaptáljuk az OldCar viselkedését az új interfészhez
        self.old_car.start_engine()
        self.old_car.move()