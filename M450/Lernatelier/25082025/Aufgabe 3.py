"""
Aufgabe 3: Wörter zählen

Schreibe ein Programm, das Wörter von der Nutzerin/dem Nutzer einliest und zählt, wie viele Wörter mit einem bestimmten Buchstaben beginnen.

Die Wörter sollen in einer Liste gespeichert werden.

Mit einer Schleife wird jedes Wort geprüft.

Mit einer Verzweigung wird gezählt, ob das Wort mit dem gesuchten Buchstaben beginnt.

Verwende eine Funktion, die die Zählung übernimmt.

Beispieltabelle:

Eingaben (Wörter, gesuchter Buchstabe)	Ausgabe
["Apfel", "Banane", "Ananas"], "A"	"2 Wörter beginnen mit A"
["Katze", "Hund", "Kuh"], "K"	"2 Wörter beginnen mit K"
["rot", "blau", "gelb"], "g"	"1 Wörter beginnen mit g"
["Sonne", "Mond"], "M"	"1 Wörter beginnen mit M"
["Auto", "Ampel", "Ast"], "A"	"3 Wörter beginnen mit A"
"""
def word_counter(words:str, letter:str):
    counter = 0
    for word in words:
        if word[0].lower() == letter.lower():
            counter += 1
    return counter

words = [input("Wort: ") for _ in range(3)]
letter = input("Buchstabe: ")

print(word_counter(words, letter))