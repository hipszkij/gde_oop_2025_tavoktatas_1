class GradeCalculator:
    def __init__(self, test_score, dev_score):
        self.test_score = test_score
        self.dev_score = dev_score

    def calculate_final_score(self):
        # Az összesített pontszám számítása: teszteredmény és fejlesztési feladat átlaga
        return (self.test_score + self.dev_score) / 2

    def get_final_grade(self):
        # Végső pontszám kiszámítása
        final_score = self.calculate_final_score()

        # Érdemjegy meghatározása az összesített pontszám alapján
        if final_score >= 90:
            return '5'
        elif final_score >= 80:
            return '4'
        elif final_score >= 70:
            return '3'
        elif final_score >= 60:
            return '2'
        else:
            return '1'

    def __str__(self):
        # Az érdemjegy sztring formátumban való megjelenítése
        return f"A kapott osztályzat: {self.get_final_grade()}"


# Osztály példányosítása és érdemjegy számítása
calculator = GradeCalculator(85, 90)
print(calculator)

