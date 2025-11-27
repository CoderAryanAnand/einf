"""
Erstellen Sie ein Python-Programm, das Charaktere (NPCs) aus einem Rollenspiel verwaltet.

Erstellen Sie eine Klasse Charakter, die folgende Informationen enthält:

    name: Name der Figur
    standort: X- und Y- Koordinate der Figur
    dialoge: mögliche Sätze, die die Figur sagen kann
    attribute: Eigenschaften wie Mut ist "gross" , Stärke ist 12, Wissen ist 22
    __str__(): Gibt alle Daten der Figur übersichtlich aus.


Schreiben Sie eine Funktion, die die Charaktere nach Regionen (z. B. Wald, Wüste, Schneegebiet) gruppiert und anschliessend alle Charaktere ausgibt.

Verwenden Sie die am besten geeigneten Datentypen.
"""

class Charakter:
    def __init__(self, name, standort, dialoge, attribute):
        self.name = name
        self.standort = standort
        self.dialoge = dialoge
        self.attribute = attribute
    
    def __str__(self):
        return f"Name: {self.name}\nStandort: X: {self.standort[0]}, Y: {self.standort[1]}\nDialoge: {self.dialoge}\nAttribute: {self.attribute}"
    

def create_chars():
    char_1 = Charakter("Bob", (12, 40), ["Hi!", "Bye!", "I don't know."], {"Mut": "gross", "Stärke": 12, "Wissen": 22})
    char_2 = Charakter("Alice", (42, 40), ["Hey!", "Tschüss!", "Ka broski."], {"Mut": "mittel", "Stärke": 22, "Wissen": 31})

    places = {"Wald": {char_1}, "Wüste": {char_2}}

    for place in places:
        print(place)
        for p in places[place]:
            print(p)


create_chars()