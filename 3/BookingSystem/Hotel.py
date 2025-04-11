class Hotel:
    def __init__(self, name):
        self._name = name
        self._rooms = []

    @property
    def name(self):
        return self._name

    @property
    def rooms(self):
        for room in self._rooms:
            print(f" Szobaszám: {room.room_number}, Price: {room.price} huf - Foglalt: {room.is_booked}")

    @rooms.setter
    def rooms(self, new_room):
        self._rooms.append(new_room)

    def book_by_room_number(self, room_number):
        for room in self._rooms:
            if room.room_number == room_number:
                return room.book_room()

    def unbook_by_room_number(self, room_number):
        for room in self._rooms:
            if room.room_number == room_number:
                return room.unbook_room()
