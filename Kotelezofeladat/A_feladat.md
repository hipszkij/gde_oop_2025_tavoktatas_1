# Autókölcsönző Rendszer

Ez a projekt egy egyszerű autókölcsönző rendszert valósít meg, amelyben autókat lehet bérelni, lemondani a bérlést, és megtekinteni az aktuális bérlések listáját.

## Általános elvárások

- Pythonban készítsétek a vizsgafeladatot.
- Csináljatok egy "adatok.txt" fájlt, amiben töltsétek ki a neveteket, szakotokat és Neptun kódotokat.
- A kész projektet osszátok meg a saját GitHub repositorytokban PUBLIC-ra, és a repository URL-jét küldjétek el emailben a **hipszki.janos@gde.hu** címre.
- **Határidő: 2025.06.01.**
- Elküldés előtt tegyétek meg a következőket:
  - Egy browser incognito ablakában nézzétek meg az elküldendő GitHub repositoryt (látható, fent van az utolsó commit is).
  - Clone-ozzátok ki a repositoryt PyCharm-ban, és nézzétek meg, hogy futtatható-e (így fogom én is tesztelni, el kell induljon a projekt, hogy értékelni tudjam).

## Fő osztályok

- **Auto (absztrakt osztály):** Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).
- **Személyauto:** A személyautók specifikus attribútumait tartalmazó osztály.
- **Teherauto:** A teherautók specifikus attribútumait tartalmazó osztály.
- **Autokolcsonzo:** Tartalmazza az autókat és saját attribútumot is, például a kölcsönző nevét.
- **Berles:** Az autóbérléshez szükséges osztály, amely egy autó bérlését egy napra tárolja.

## Funkciók

- **Autó bérlése:** Az autók bérelhetők egy napra, és a bérlés visszaadja az árat.
- **Bérlés lemondása:** A felhasználó lemondhatja a meglévő bérlését.
- **Bérlések listázása:** Az összes aktuális bérlés listázása.

## Adatvalidáció

- Ellenőrzi, hogy az autó elérhető-e bérlésre, és a bérlési dátum érvényes-e.
- Biztosítja, hogy csak létező bérléseket lehessen lemondani.

## Felhasználói interfész

- Egyszerű felhasználói interfész, amely lehetővé teszi a következő műveleteket:
  - Autó bérlése
  - Bérlés lemondása
  - Bérlések listázása

## Előkészítés

A rendszer indulásakor egy autókölcsönző áll rendelkezésre, amely 3 autót és 4 bérlést tartalmaz. Ezt az adatot a program indulásakor előre betöltjük a rendszerbe, így a felhasználó már használatra kész rendszert kap.
