from Animal import Animal


class Cat(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)

    def make_sound(self):  # Method overriding
        return "Meow meow!"

