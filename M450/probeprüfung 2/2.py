class Monster:
    def __init__(self, name, x_coord, y_coord, freunde, werte):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.freunde = freunde
        self.werte = werte

    def __str__(self):
        return f"{self.name} ist bei der Koordinate ({self.x_coord}, {self.y_coord}) und ist befreundet mit {self.freunde}. Er hat folgende Werte: {self.werte}"
    


monster_list = {"Level 1": Monster("Mike", 80, 120, ("Big boy", "Nellie"), {"Energie": 100, "Schild": 50, "Angriff": 20}),
                "Level 2": Monster("Big Boy", 90, 110, ("Mike", "Nellie"), {"Energie": 100, "Schild": 40, "Angriff": 30})}

for level in monster_list:
    print(monster_list[level])