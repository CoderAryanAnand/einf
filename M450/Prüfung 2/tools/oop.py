# --- SCHUMMELZETTEL 1: KLASSEN & DATENSTRUKTUREN (Based on 1.py & 2.py) ---

class GameItem:
    # 1. Konstruktor (Goal 13): Initialisiert Attribute
    def __init__(self, name, wert, position):
        self.name = name          # String
        self.wert = wert          # Integer (z.B. Energie/Leistung in 1.py)
        self.pos = position       # Tuple (x, y) (z.B. Koordinaten in 2.py)
        self.active = True        # Boolean status

    # 2. Methoden (Goal 10): Verhalten implementieren
    def power_up(self, amount):
        self.wert += amount
        # Methode ruft andere Methode auf (Goal 11)
        self.check_status()

    def check_status(self):
        if self.wert > 100:
            print(f"{self.name} ist überladen!")

    # 3. String Repräsentation (Crucial for 2.py!)
    # Ermöglicht: print(my_object) -> Schöne Ausgabe
    def __str__(self):
        return f"Item: {self.name} | Wert: {self.wert} | Ort: {self.pos}"

# --- ANWENDUNG & LISTEN/DICTIONARIES (Goal 5, 18) ---

# Einzelnes Objekt erstellen
item1 = GameItem("Schwert", 50, (10, 20))
print(item1) # Ruft __str__ auf

# Liste von Objekten (Wie in 4.py für Meteore)
item_list = []
item_list.append(GameItem("Schild", 100, (50, 50)))
item_list.append(GameItem("Trank", 20, (100, 50)))

print("\n--- Liste Iteration ---")
for item in item_list:
    item.power_up(10)
    print(item)

# Dictionary von Objekten (EXAKT WIE IN 2.py)
# Key = String (Name/ID), Value = Objekt
monster_dict = {
    "Level 1": GameItem("Goblin", 30, (200, 200)),
    "Level 2": GameItem("Boss", 500, (400, 400))
}

print("\n--- Dictionary Iteration (2.py Style) ---")
for level_key in monster_dict:
    # Zugriff auf das Objekt im Dictionary
    current_monster = monster_dict[level_key]
    print(f"{level_key}: {current_monster}")