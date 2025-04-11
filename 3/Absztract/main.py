from Car import Car
from Truck import Truck
from Vehicle import Vehicle


# Használat
def vehicle_test(vehicle: Vehicle):
    vehicle.start()
    vehicle.drive()

car = Car("Toyota", 180)
truck = Truck("Volvo", 120)

# Teszteljük mindkét járművet
vehicle_test(car)
vehicle_test(truck)