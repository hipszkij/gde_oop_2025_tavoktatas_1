from Vehicle import Vehicle

# Concrete class - Car
class Car(Vehicle):
    def start(self):
        print(f"A {self.brand} személyautó elindul.")

    def drive(self):
        print(f"A {self.brand} személyautó halad {self.max_speed} km/h maximális sebességgel.")
