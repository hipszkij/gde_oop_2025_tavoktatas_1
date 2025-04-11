from abc import ABC, abstractmethod

# Abstract base class (Vehicle)
class Vehicle(ABC):
    def __init__(self, brand, max_speed):
        self.brand = brand        # Márka
        self.max_speed = max_speed  # Maximális sebesség

    @abstractmethod
    def start(self):
        """Absztrakt metódus, amit minden leszármazott osztálynak meg kell valósítania."""
        pass

    @abstractmethod
    def drive(self):
        """Absztrakt metódus, amit minden leszármazott osztálynak meg kell valósítania."""
        pass