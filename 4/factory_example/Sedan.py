from Car import Car


class Sedan(Car):
    def __init__(self, brand, type, color, year):
        self.brand = brand
        self.type = type
        self.color = color
        self.year = year

    def assemble(self):
        pass

    def __str__(self):
        return "sedan"
