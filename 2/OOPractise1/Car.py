# Az osztály definiálása
class Car:
    # Konstruktor, amely az objektum inicializálásáért felelős
    def __init__(self, brand, model, year):
        self.brand = brand  # Publikus attribútum
        self.model = model  # Publikus attribútum
        self.__year = year  # Privát attribútum (kettős aláhúzás jelzi a privát mivoltát)

    # Metódus (funkció) a Car osztályon belül
    def start(self):
        print(f"The {self.brand} {self.model} is starting.")

    # Getter a privát attribútum eléréséhez
    def get_year(self):
        return self.__year

    # Setter a privát attribútum módosításához
    def set_year(self, year):
        if year > 1885:  # Az első autó 1886-ban készült, ezért ezt a logikát használjuk
            self.__year = year
        else:
            print("Invalid year for a car!")

    # Példa egy polimorfizmusra (öröklés és metódus felülírás esetén)
    def honk(self):
        print("Beep beep!")

# Öröklődés: A Tesla osztály örökli a Car osztályt
class Tesla(Car):
    # Új metódus, amely csak a Tesla-ra vonatkozik
    def autopilot(self):
        print(f"The {self.brand} {self.model} is now on autopilot.")

    # Felülírjuk az örökölt honk metódust (polimorfizmus)
    def honk(self):
        print("Tesla silent honk!")

# Objektum létrehozása
my_car = Car("Toyota", "Corolla", 2020)
my_tesla = Tesla("Tesla", "Model S", 2021)

# Objektumok használata (metódusok hívása, attribútumok elérése)
my_car.start()  # "The Toyota Corolla is starting."
my_car.honk()   # "Beep beep!"

my_tesla.start()  # "The Tesla Model S is starting."
my_tesla.autopilot()  # "The Tesla Model S is now on autopilot."
my_tesla.honk()  # "Tesla silent honk!" (polimorfizmus)
