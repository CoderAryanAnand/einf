"""
Aufgabe 2: Notenschnitt berechnen

Schreibe ein Programm, das die Noten einer Klasse einliest und den Durchschnitt berechnet.

Frage zuerst, wie viele Noten eingegeben werden sollen.

Lies dann die Noten ein und speichere sie in einer Liste.

Berechne den Durchschnitt mit einer Funktion.

Wenn der Schnitt besser als 4.0 ist, gib aus: "Klasse bestanden", sonst "Klasse nicht bestanden".

Beispieltabelle:

Eingaben (Anzahl, Noten)	Ausgabe
3, Noten: 5, 4, 3	"Durchschnitt: 4.0", "Klasse bestanden"
4, Noten: 2, 2, 3, 1	"Durchschnitt: 2.0", "Klasse bestanden"
2, Noten: 5, 5	"Durchschnitt: 5.0", "Klasse nicht bestanden"
5, Noten: 4, 4, 4, 4, 4	"Durchschnitt: 4.0", "Klasse bestanden"
3, Noten: 6, 5, 6	"Durchschnitt: 5.7", "Klasse nicht bestanden"
"""

num_grades = int(input("Wie viele Noten?"))

grades = [int(input("Note: ")) for _ in range(num_grades)]
avg = sum(grades) / len(grades)
print("bestanden" if avg >=4 else "failed")