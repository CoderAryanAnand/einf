"""
Fragen Sie den Benutzer/die Benutzerin nach einer Anzahl und füllen Sie eine Liste mit so vielen zufälligen Werten zwischen und mit 1 bis 20.

Fragen Sie den Benutzer/die Benutzerin nach einer Zahl zwischen und mit 1 bis 20. Wiederholen Sie diese Frage so oft, bis die eingegebene Zahl zwischen und mit 1 bis 20 ist, und machen Sie erst dann weiter.

Geben Sie die Anzahl der Elemente in der Liste aus, die grösser oder gleich dieser Zahl sind. 
"""

import random

list_length = int(input("Geben Sie die Anzahl der Elemente in der Liste an: "))
random_list = [random.randint(1, 20) for _ in range(list_length)]

user_number = int(input("Geben Sie eine Zahl zwischen 1 und 20 ein: "))
while user_number < 1 or user_number > 20:
    user_number = int(input("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 20 ein: "))

count = sum(1 for number in random_list if number >= user_number)
print(f"Die Liste enthält {count} Elemente, die grösser oder gleich {user_number} sind.")