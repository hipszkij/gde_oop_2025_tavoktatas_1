from Food import Food
from Restaurant import Restaurant

food1 = Food(1, "Pizza", 1000)
food2 = Food(2, "Hamburger", 2000)

restaurant = Restaurant("Teszt étterem", [food1, food2])

#print(restaurant)
#restaurant.getMenuItems()

print("Új menü elem hozzáadása")
while True:
    try:
        id = len(restaurant) + 1
        inputItemName = input("Adj meg egy ételt: ")
        inputItemPrice = int(input("Add meg az étel árát: "))

        if inputItemPrice <= 0 or inputItemPrice >= 100000:
            raise ValueError("Az étel ára csak 0 és 100000 közötti lehet")

        food = Food(id, inputItemName, inputItemPrice)
        restaurant + food
        break
    except ValueError as e:
        print(e)


restaurant.getMenuItems()
