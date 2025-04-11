# Subject (Megfigyelt)
class WeatherStation:
    def __init__(self):
        self._observers = []  # Lista a megfigyelők (Observer-ek) tárolására
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"WeatherStation: Hőmérséklet megváltozott {temperature}°C-ra")
        self._temperature = temperature
        self.notify_observers()  # Értesíti az összes megfigyelőt