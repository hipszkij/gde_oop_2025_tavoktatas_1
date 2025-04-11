from WeatherStation import WeatherStation
from PhoneDisplay import PhoneDisplay
from LCDDisplay import LCDDisplay

# Használat
weather_station = WeatherStation()

# Létrehozunk két megfigyelőt
phone_display = PhoneDisplay()
lcd_display = LCDDisplay()

# Regisztráljuk a megfigyelőket az időjárás állomáson
weather_station.register_observer(phone_display)
weather_station.register_observer(lcd_display)

# Változtassuk meg a hőmérsékletet és figyeljük meg, hogy a megfigyelők értesítést kapnak
weather_station.set_temperature(25)
weather_station.set_temperature(30)

# Távolítsunk el egy megfigyelőt
weather_station.remove_observer(lcd_display)

# Ismét változtassuk meg a hőmérsékletet
weather_station.set_temperature(28)