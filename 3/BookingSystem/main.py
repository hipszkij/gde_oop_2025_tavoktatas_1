from Hotel import Hotel
from SingleRoom import SingleRoom
from DoubleRoom import DoubleRoom
from Suite import Suit


class BookingSystem:
    def __init__(self):
        self._hotel = Hotel("Four seasons")
        self._init_data()

    def _init_data(self):
        self._hotel.rooms = SingleRoom(101, 10000)
        self._hotel.rooms = SingleRoom(102, 10000)
        self._hotel.rooms = SingleRoom(103, 10000)
        self._hotel.rooms = DoubleRoom(201, 20000)
        self._hotel.rooms = DoubleRoom(202, 20000)
        self._hotel.rooms = Suit(901, 100000)

    def user_interact(self):
        while True:
            print("1. Szobák listázása")
            print("2, Szoba foglalása")
            print("3. Szoba lemondása")
            print("4. Kilépés")

            choice = input("Válasz a fenti menüpontok közül: ")

            if choice == "1":
                self._hotel.rooms
            elif choice == "2":
                room = int(input("Add meg a szoba számát, amit szeretnél lefoglalni!"))
                self._hotel.book_by_room_number(room)
            elif choice == "3":
                room = int(input("Add meg a szoba számát, amit szeretnél lemondani!"))
                self._hotel.unbook_by_room_number(room)
            elif choice == "4":
                break


booking_system = BookingSystem()
booking_system.user_interact()
