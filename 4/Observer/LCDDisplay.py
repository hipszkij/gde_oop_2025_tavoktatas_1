# Concrete Observer - LCD Kijelző
from Observer import Observer

class LCDDisplay(Observer):
    def update(self, temperature):
        print(f"LCDDisplay: A kijelző frissítve: {temperature}°C")