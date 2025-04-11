# TypeError példa

# Definiálunk egy egyszerű függvényt, amely két számot ad össze
def osszead(a, b):
    return a + b

# Meghívjuk a függvényt, de az egyik paraméter nem szám, hanem string
try:
    eredmeny = osszead(5, "10")
    print(f"Eredmény: {eredmeny}")
except TypeError as e:
    print(f"TypeError történt: {e}")
