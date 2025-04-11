class Teglalap:
    def __init__(self, szelesseg, magassag):
        self._szelesseg = szelesseg
        self._magassag = magassag

    # Getter metódus a szelesseg attribútumhoz
    def get_szelesseg(self):
        return self._szelesseg

    # Setter metódus a szelesseg attribútumhoz
    def set_szelesseg(self, ertek):
        if ertek > 0:
            self._szelesseg = ertek
        else:
            raise ValueError("A szélesség nem lehet nulla vagy negatív.")

    # Property létrehozása
    szelesseg = property(get_szelesseg, set_szelesseg)

# Példányosítás és használat
teglalap = Teglalap(10, 5)
print(f"A téglalap szélessége: {teglalap.szelesseg}")  # A getter meghívása

teglalap.set_szelesseg(15)
teglalap.szelesseg = 15 # A setter meghívása

teglalap.get_szelesseg()
print(f"A téglalap új szélessége: {teglalap.szelesseg}")

# Hibás érték beállítása (setter validáció)
try:
    teglalap.szelesseg = -5  # Hibát fog okozni
except ValueError as e:
    print(e)
