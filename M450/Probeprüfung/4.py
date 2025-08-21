"""
Schreiben Sie ein Programm, das sich eine zufällige Zahl zwischen 1 und 100 (inklusive) merkt, und den Benutzer die Zahl raten lässt. Das Programm gibt für jeden Rateversuch aus, ob die gemerkte Zahl grösser, kleiner oder genau die Zahl ist, die der Benutzer geraten hat.

Wenn die korrekte Zahl erraten wurde, ist das Spiel zu Ende und der Benutzer soll gefragt werden, ob er nochmals spielen möchte.

Das Programm soll sich für jedes Spiel eine neue Zufallszahl ausdenken.

Hinweis:

Zufallszahlen können Sie folgendermassen erstellen:

import random
x = random.randint(1, 10) # Zufallszahl zwischen 1 und 10 
"""

import random

while True:
	computer_number = random.randint(1, 100)

	user_guess = int(input("Rate die Zahl zwischen 1-100: "))
	
	while user_guess != computer_number:
		if user_guess < computer_number:
			print("Meine Zahl ist grösser")
			user_guess = int(input("Rate nochmals: "))
			continue
		else:
			print("Meine Zahl ist kleiner")
			user_guess = int(input("Rate nochmals: "))
			continue
	
	print("Gratulation! Du hast die Zahl erraten!")
	again = input("Willst du nochmals spielen? (y/n)")
	if again.lower() == "y":
		continue
	else:
		break