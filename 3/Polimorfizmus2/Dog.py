from Animal import Animal


class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the parent class constructor using super()
        super().__init__(name)
        self.breed = breed  # Adding an additional attribute specific to Dog

    def make_sound(self):  # Method overriding
        return "Woof woof!"