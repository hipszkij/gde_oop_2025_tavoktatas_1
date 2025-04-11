class Polygon:
    color = 'piros'
    def __init__(self, sides):
        self.sides = sides
        self.__oldalszelesseg = 2

    def getoldalszelleseg(self):
        return self.__oldalszelesseg

    def __str__(self):
        return "Én egy polygon vagyok"


my_polygon = Polygon(4)

print(my_polygon._Polygon__oldalszelesseg)

print(my_polygon.getoldalszelleseg())
# print(my_polygon)


