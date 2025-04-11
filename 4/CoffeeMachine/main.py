from SmallCoffeeMachineBuilder import SmallCoffeeMachineBuilder

coffee_machine_builder = SmallCoffeeMachineBuilder()

coffee_machine = (coffee_machine_builder
                  .set_water_tank(1)
                  .set_bean_tank(2)
                  .build())


