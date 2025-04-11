# Adapter Design Pattern in Python

This project demonstrates the **Adapter Design Pattern** in Python. The Adapter pattern allows two incompatible interfaces to work together by introducing an intermediate adapter class.

### Problem Statement

In our case, we have:
1. **OldCar**: A class that doesn't have the `drive()` method and uses incompatible methods like `start_engine()` and `move()`.
2. **NewCar**: A class that is already compatible with the new system and provides the `drive()` method.

We need to make sure that both the `OldCar` and `NewCar` can be used in the new system, which expects a `drive()` method. To achieve this, we use the Adapter pattern to bridge the gap between the old and new classes.

### Files

- `CarInterface`: The target interface for the new system that requires a `drive()` method.
- `OldCar`: The legacy class that has incompatible methods.
- `OldCarAdapter`: The adapter class that makes `OldCar` compatible with the new system by implementing the `CarInterface`.
- `NewCar`: A modern car class that is already compatible with the new system.
- `main.py`: The driver code to test the functionality of both `OldCar` and `NewCar`.

### Code

```python
# Target interface (the new system works with this interface)
class CarInterface:
    def drive(self):
        raise NotImplementedError("Subclasses should implement this!")

# Adaptee class (OldCar doesn't have the expected interface)
class OldCar:
    def start_engine(self):
        print("OldCar: Engine started.")
    
    def move(self):
        print("OldCar: Car is moving.")

# Adapter class (Adapts OldCar to work with CarInterface)
class OldCarAdapter(CarInterface):
    def __init__(self, old_car):
        self.old_car = old_car

    def drive(self):
        # Adapt OldCar's methods to the new interface
        self.old_car.start_engine()
        self.old_car.move()

# NewCar class (Already compatible with the new system)
class NewCar(CarInterface):
    def drive(self):
        print("NewCar: Driving smoothly with modern features.")

# The new system that expects the CarInterface
def test_car(car: CarInterface):
    car.drive()

# Usage
old_car = OldCar()
adapted_old_car = OldCarAdapter(old_car)  # OldCar is adapted

new_car = NewCar()  # NewCar is already compatible

# Testing both OldCar and NewCar
print("Testing OldCar with Adapter:")
test_car(adapted_old_car)  # Using adapter for OldCar

print("\nTesting NewCar:")
test_car(new_car)  # Directly using NewCar
