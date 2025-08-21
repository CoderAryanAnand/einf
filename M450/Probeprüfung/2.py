"""
Schreiben Sie ein Programm, das den Benutzer/die Benutzerin nach einer Stunde fragt und alle Minuten zweistellig bis zur nächsten Stunde ausgibt.

Beispiel:

Eingabe: 5

5:00
5:01
5:02
5:03
...
5:58
5:59
"""

hour = int(input("Geben Sie eine Stunde (0-23) ein: "))

for minute_ten in range(0, 6):
    for minute_one in range(0, 10):
        minute = str(minute_ten) + str(minute_one)
        print(f"{hour}:{minute}")