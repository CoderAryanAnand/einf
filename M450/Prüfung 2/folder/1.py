"""
Implementieren Sie die unten spezifizierte Klasse.

zeichne(): Soll ausgeben "Ich würde zeichnen."

umfang(): Soll den Umfang der Figur zurückgeben.

flaeche(): Soll die Fläche der Figur zurückgeben.

Erzeugen Sie ein Objekt der Figur und geben Sie das Resultat aller Methoden aus.

Geben Sie den Quelltext direkt per copy-paste (richtig formatiert) ab.
"""

class Quadrat:

    def __init__(self, seite, fuellfarbe):
        self.seite = seite
        self.fuellfarbe = fuellfarbe

    def zeichne(self):
        print("Ich würde zeichnen.")

    def umfang(self):
        return self.seite * 4
    
    def flaeche(self):
        return self.seite ** 2
    

big_square = Quadrat(3, "rot")

big_square.zeichne()
print(big_square.umfang())
print(big_square.flaeche())