# Concrete Observer - Telefonos alkalmazás
from Observer import Observer

class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"PhoneDisplay: Az új hőmérséklet: {temperature}°C")