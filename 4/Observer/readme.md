# Observer Design Pattern in Python

This project demonstrates the **Observer Design Pattern** in Python. The Observer pattern is a behavioral design pattern that allows an object (the **subject**) to notify multiple observer objects about any state changes, without having a tight coupling between them.

### Problem Statement

In our example, we simulate a **WeatherStation** that can notify multiple devices (observers) about temperature changes. The observers could be different display devices, such as:
1. **PhoneDisplay**: Displays the temperature on a mobile phone.
2. **LCDDisplay**: Displays the temperature on an LCD screen.

Whenever the temperature in the `WeatherStation` changes, all registered observers get notified about the change, and they update their display accordingly.

### Components of the Pattern

- **Subject (WeatherStation)**: The subject maintains a list of observers and notifies them of any state changes (in this case, temperature changes).
- **Observer Interface**: Defines an interface for objects that should be notified when the subject's state changes.
- **Concrete Observers (PhoneDisplay, LCDDisplay)**: These implement the `Observer` interface and react to changes in the subject by updating their own state.

### Code Example

```python
# Subject (WeatherStation)
class WeatherStation:
    def __init__(self):
        self._observers = []  # List to store observers
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"WeatherStation: Temperature changed to {temperature}°C")
        self._temperature = temperature
        self.notify_observers()  # Notify all registered observers

# Observer interface
class Observer:
    def update(self, temperature):
        pass

# Concrete Observer - PhoneDisplay
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"PhoneDisplay: The new temperature is: {temperature}°C")

# Concrete Observer - LCDDisplay
class LCDDisplay(Observer):
    def update(self, temperature):
        print(f"LCDDisplay: Display updated: {temperature}°C")

# Usage
weather_station = WeatherStation()

# Create two observers
phone_display = PhoneDisplay()
lcd_display = LCDDisplay()

# Register observers with the weather station
weather_station.register_observer(phone_display)
weather_station.register_observer(lcd_display)

# Change the temperature and notify observers
weather_station.set_temperature(25)
weather_station.set_temperature(30)

# Remove one observer
weather_station.remove_observer(lcd_display)

# Change the temperature again
weather_station.set_temperature(28)
