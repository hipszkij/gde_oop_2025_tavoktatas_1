class Logger:
    _instance = None
    _logs = []

    #A __new__ metódus felelős egy új objektum létrehozásáért,
    #mielőtt azt a __init__ metódus inicializálná.
    #A __new__ segítségével biztosíthatjuk, hogy mindig ugyanaz az objektum legyen visszaadva,
    #így létrehozhatjuk a Singleton mintát.
    def __new__(cls):
        #feltétellel csak akkor hozunk létre új példányt,
        #ha korábban nem létezett, különben a már meglévő példányt adjuk vissza.
        if cls._instance is None:
            print("Creating the Logger instance")
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        self._logs.append(message)
        print(f"Logged: {message}")

    def get_logs(self):
        return self._logs
