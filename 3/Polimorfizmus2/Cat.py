from Animal import Animal

class Cat(Animal):
    def __init__(self, name, color):
        # Calling the parent class constructor using super()
        super().__init__(name)
        self.color = color  # Adding an additional attribute specific to Cat

    def make_sound(self):  # Method overriding
        return "Meow meow!"