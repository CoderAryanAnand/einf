class Auto:
    def __init__(self, farbe, marke):
        self.farbe = farbe
        self.marke = marke
        self.geschwindigkeit = 0
    
    def schneller(self, wie_viel):
        self.geschwindigkeit += wie_viel
        return f"Ich fahre jetzt {self.geschwindigkeit} km/h."
    
    def bremsen(self):
        self.geschwindigkeit -= 10
        return f"Ich fahre jetzt {self.geschwindigkeit} km/h."
    
    def hupen(self):
        return "Tüütüütz"
    
    def __str__(self):
        return f"Auto Marke: {self.marke}, Farbe: {self.farbe}, Geschwindigkeit: {self.geschwindigkeit} km/h"

"""
b) Objekte erstellen
Erstellen Sie mehr als ein unterschiedliches Auto-Objekt und lassen Sie diese fahren.

c) Klasse erweitern
Erweitern Sie das Auto so, dass das Hup-Geräusch verändert werden kann.
"""
auto1 = Auto("rot", "Toyota")
print(auto1.schneller(50))
print(auto1.hupen())
auto2 = Auto("blau", "BMW")
print(auto2.schneller(70))
print(auto2.bremsen())
print(auto2.hupen())

class AutoMitAnpassbaremHupen(Auto):
    def __init__(self, farbe, marke, hup_geraeusch="Tüütüütz"):
        super().__init__(farbe, marke)
        self.hup_geraeusch = hup_geraeusch
    
    def hupen(self):
        return self.hup_geraeusch
    
print(auto1)