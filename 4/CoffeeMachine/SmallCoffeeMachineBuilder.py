from CoffeeMachineBuilder import CoffeeMachineBuilder
from CoffeeMachine import CoffeeMachine


class SmallCoffeeMachineBuilder(CoffeeMachineBuilder):
    def __init__(self):
        self.coffee_machine = CoffeeMachine()

    def set_water_tank(self, new_water_tank_size):
        self.coffee_machine.water_tank(new_water_tank_size)
        return self

    def set_bean_tank(self, new_bean_tank_size):
        self.coffee_machine.bean_tank(new_bean_tank_size)
        return self

    def build(self):
        return self.coffee_machine
