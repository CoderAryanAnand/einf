"""
Aufgabe 1: Zahlen raten mit Hinweisen

Schreibe ein Programm, das eine geheime Zahl in einer Liste von möglichen Zahlen auswählt und die Nutzerin/den Nutzer raten lässt.

Verwende eine Liste mit möglichen Zahlen.

Die Nutzerin/der Nutzer soll so lange raten, bis die richtige Zahl gefunden wurde.

Nach jedem Versuch gibt das Programm einen Hinweis, ob die Zahl größer oder kleiner ist.

Baue die Spiellogik in eine Funktion ein.

Beispieltabelle:

Eingabe (Rateversuche)	Ausgabe
3, 5, 7	"Zu klein!", "Zu groß!", "Richtig!"
1, 2	"Zu klein!", "Richtig!"
9	"Zu groß!", "Richtig!"
4	"Richtig!"
2, 3, 4, 5	"Zu klein!", "Zu klein!", "Zu groß!", "Richtig!"
"""

import random

def main():
    random_number_list = [random.randint(1, 10) for _ in range(5)]
    bot_choice = random.choice(random_number_list)
    
    user_number = 100

    while user_number != bot_choice:
        user_number = int(input("Rate die Zahl zwischen 1 und 10: "))
        while user_number < 1 or user_number > 10:
            user_number = int(input("Die eingegebene Zahl war nicht zwischen 1 und 10.\nRate die Zahl zwischen 1 und 10: "))
        if user_number == bot_choice:
            print("Richtig!")
            break
        print("Zu gross!" if user_number > bot_choice else "Zu klein!")




main()