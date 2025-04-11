from Vehicle import Vehicle

# Concrete class - Truck
class Truck(Vehicle):
    def start(self):
        print(f"A {self.brand} teherautó elindul.")

    def drive(self):
        print(f"A {self.brand} teherautó halad {self.max_speed} km/h maximális sebességgel, és nagy terhet szállít.")