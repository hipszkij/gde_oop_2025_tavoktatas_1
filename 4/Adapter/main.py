from CarInterface import CarInterface
from OldCar import OldCar
from OldCarAdapter import OldCarAdapter
from NewCar import NewCar

# Az új rendszer, ami csak a drive() metódust ismeri
def test_car(car: CarInterface):
    car.drive()


old_car = OldCar()
adapted_old_car = OldCarAdapter(old_car) # OldCar-t adapterrel kötjük be az új rendszerbe

new_car = NewCar() # NewCar már kompatibilis az új rendszerrel

# Az új rendszer meghívja a drive() metódust
print("Testing OldCar with Adapter:")
test_car(adapted_old_car)  # Az adapter által működik az OldCar az új rendszerrel

print("\nTesting NewCar:")
test_car(new_car)  # NewCar közvetlenül használható az új rendszerrel