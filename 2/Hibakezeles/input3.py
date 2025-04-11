number = input("Írj be egy számot: ")

try:
    parsedNumber = int(number)
except ValueError:
    print("Nem szám típusú, amit beírtál")
else:
    if parsedNumber < 10:
        raise ValueError("10-nél nagyobb számot adj meg")
    else:
        print("Megfelelő szám")