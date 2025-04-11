from abc import ABC, abstractmethod


class CoffeeMachineBuilder(ABC):
    @abstractmethod
    def set_water_tank(self, new_water_tank_size):
        pass

    @abstractmethod
    def set_bean_tank(self, new_bean_tank_size):
        pass

    @abstractmethod
    def build(self):
        pass
