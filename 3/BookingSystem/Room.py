from abc import ABC


class Room(ABC):
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.is_booked = False
        self.extras = []

    def book_room(self):
        pass

    def unbook_room(self):
        pass
