from CarFactory import CarFactory

car_factory = CarFactory()

sedan = car_factory.create_car("Sedan", "Toyota", "Yaris", "black", 2005)
suv = car_factory.create_car("SUV", "Toyota", "suv model", "white", 2010)

print(sedan)
print(suv)