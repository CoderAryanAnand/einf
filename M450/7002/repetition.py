# Repetitionsauftrag ("Die Basics")
#
# WICHTIG: Alle Dinge, die in doppelten eckigen Klammern stehen 
#          bitte durch die aktuellen Informationen ersetzen.
#          Beispiele:
#            * [[IHR NACHNAME]] wäre bei mir Schneider
#            * [[ANZAHL BUCHSTABEN IHRES VORNAMENS]] wäre bei mir 7 (Michael)
#

#
# Aufgabe 1: 
#
# Fragen Sie die Benutzerin/den Benutzer nach ihrem/seinem Namen.
# Geben Sie danach folgenden Text aus: 
# "Hallo [[EINGEGEBENER NAME]], ich heisse [[IHR VORNAME]]." 

name = input("Wie heisst du? ")
print(f"Hallo {name}, ich heisse COMPUTERPROGRAMM.")

#
# Aufgabe 2: 
#
# Fragen Sie die Benutzerin/den Benutzer nach zwei Zahlen.
# Geben Sie danach folgenden Text aus: 
# "[[ERSTE ZAHL]] + [[ZWEITE ZAHL]] + [[ANZAHL BUCHSTABEN IHRES VORNAMENS]] = [[RESULTAT]]." 
num1 = int(input("Gib die erste Zahl ein: "))
num2 = int(input("Gib die zweite Zahl ein: "))

print(f"{num1} + {num2} + {5} = {num1 + num2 + 5}.")

#
# Aufgabe 3:
# 
# Fragen Sie die Benutzerin/den Benutzer nach ihrem/seinem Vornamen.
# Wenn er oder Sie den gleichen Vornamen hat wie Sie, geben Sie aus "Oh, wir heissen gleich!".
# Sonst geben Sie aus "Ich heisse [[IHR VORNAME]].".
first_name = input("Wie heisst du? ")
print("Oh, wir heissen gleich!" if first_name == "COMPUTERPROGRAMM" else "Ich heisse COMPUTERPROGRAMM.")

#
# Aufgabe 4:
# 
# Fragen Sie die Benutzerin/den Benutzer nach ihrem/seinem Nachnamen.
# Wenn Ihr Nachname weniger Buchstaben hat, geben Sie aus: "Mein Name hat weniger Buchstaben"
# Wenn Ihr Nachname gleich viele Buchstaben hat, geben Sie aus: "Mein Name hat gleich viele Buchstaben"
# Wenn Ihr Nachname mehr Buchstaben hat, geben Sie aus: "Mein Name hat mehr Buchstaben"

last_name = input("Wie heisst dein Nachname? ")
if len(last_name) < 5:  
    print("Mein Name hat mehr Buchstaben")
elif len(last_name) == 5:
    print("Mein Name hat gleich viele Buchstaben")
else:
    print("Mein Name hat weniger Buchstaben")
#
# Aufgabe 5:
# 
# Fragen Sie die Benutzerin/den Benutzer nach einer Zahl.
# Scheiben Sie ein Programm, das alle Zahlen 
# von 1 bis [[EINGEGEBENE ZAHL]]+[[ANZAHL BUCHSTABEN IHRES VORNAMENS + ANZAHL BUCHSTABEN IHRES NACHNAMENS]] ausgibt

random_number = int(input("Gib eine Zahl ein: "))
print(i for i in range(1, random_number+5+5))

#
# Aufgabe 6:
# 
# Fragen Sie die Benutzerin/den Benutzer nach einer Zahl zwischen
# [[ANZAHL BUCHSTABEN IHRES NAMENS]] und 30 (Grenzen inklusive).
# Wenn die Zahl ausserhalb dieses Bereichs liegt, soll nochmals
# nachgefragt werden.

user_number = int(input("Gib eine Zahl zwischen 5 und 30 ein: "))
while user_number < 5 or user_number > 30:
    user_number = int(input("Die Zahl muss zwischen 5 und 30 liegen. Bitte gib eine neue Zahl ein: "))

#
# Aufgabe 7:
# 
# Eine Faustformel für den Anhalteweg mit dem Auto ist:
# Anhalteweg = [(Geschwindigkeit / 10) * (Geschwindigkeit / 10)] / 2 + (Geschwindigkeit / 10) * 3 
# Fragen Sie die Benutzerin/den Benutzer nach der Geschwindigkeit und geben Sie den Anhalteweg aus.
# Wenn eine Geschwindigkeit kleiner als 0 eingegeben wird, soll nochmals nachgefragt werden.
speed = int(input("Gib die Geschwindigkeit in km/h ein: "))
while speed < 0:
    speed = int(input("Die Geschwindigkeit muss grösser oder gleich 0 sein. Bitte gib eine neue Geschwindigkeit ein: "))

braking_distance = ((speed / 10) ** 2) / 2 + (speed / 10) * 3
print(f"Der Anhalteweg bei {speed} km/h beträgt {braking_distance} Meter.")


#
# Aufgabe 8:
# 
# Füllen Sie eine Liste mit 10 zufälligen Zahlen.
# Geben Sie die Liste, sowie die grösste und die 
# kleinste Zahl aus, ohne die Liste zu verändern.
# Zufallszahlen:
# import random
# random.randint(0, 100) # Erstellt eine Zufallszahl zwischen 1 und 100

import random 
random_numbers = [random.randint(0, 100) for _ in range(10)]
print("Zufallszahlen:", random_numbers)
print("Grösste Zahl:", max(random_numbers))
print("Kleinste Zahl:", min(random_numbers))