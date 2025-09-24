wort_liste = {"Bus": "bus", "Zug": "train", "Auto": "car"}

points = 0
for word in wort_liste:
    user_input = input(f"Übersetzung vom Wort: {word}\n")
    if user_input == wort_liste[word]:
        print("Richtig!")
        points += 1
        continue
    print("Falsch.")

print(f"Du hast {points} Wörter richtig gehabt.")