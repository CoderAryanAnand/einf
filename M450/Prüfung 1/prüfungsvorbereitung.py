"""
### Aufgabe (Stufe schwer): **Mini-Einkaufslisten-Manager**

Schreibe ein Programm, das eine kleine Einkaufsliste verwaltet.

* Das Programm fragt die Nutzerin/den Nutzer, wie viele Artikel eingetragen werden sollen.
* Danach werden die Artikel **mit Mengenangabe** (z. B. „Brot 2“) eingegeben und in einer **Liste** gespeichert.
* Schreibe eine **Funktion**, die überprüft, ob ein gesuchter Artikel in der Liste steht.
* Wenn er vorhanden ist, gib die Menge aus, sonst `"Artikel nicht gefunden"`.
* Bonus: Falls die Menge größer als 5 ist, soll zusätzlich `"Große Menge!"` ausgegeben werden.

👉 Es müssen dabei verwendet werden: **Sequenzen, Schleife, Verzweigung, Variablen, Ein-/Ausgabe, Liste, Funktion**.

---

### Beispiel-Eingaben und Ausgaben

| Eingaben                                                                          | Ausgabe                       |
| --------------------------------------------------------------------------------- | ----------------------------- |
| Anzahl: 3<br>Artikel: `Brot 2`, `Milch 1`, `Apfel 6`<br>Suche: `Apfel`            | `Apfel: 6`<br>`Große Menge!`  |
| Anzahl: 2<br>Artikel: `Ei 12`, `Butter 1`<br>Suche: `Butter`                      | `Butter: 1`                   |
| Anzahl: 4<br>Artikel: `Zucker 3`, `Kaffee 2`, `Milch 5`, `Tee 1`<br>Suche: `Salz` | `Artikel nicht gefunden`      |
| Anzahl: 1<br>Artikel: `Wasser 7`<br>Suche: `Wasser`                               | `Wasser: 7`<br>`Große Menge!` |
| Anzahl: 3<br>Artikel: `Birne 2`, `Apfel 3`, `Traube 4`<br>Suche: `Apfel`          | `Apfel: 3`                    |

"""

from prüfungtools import get_valid_number

shopping_length = get_valid_number("Wie viele Sachen müssen gekauft werden? ")


shopping_list = {}

i = 0

while i < shopping_length:
    while True:
        try:        
            stuff = input("").split(" ")
            _ = int(stuff[1])
            break
        except (ValueError, IndexError):
            print("Invalid input")
    
    if stuff[0] in shopping_list:
        shopping_list[stuff[0]] = shopping_list[stuff[0]] + int(stuff[1])
        continue
    shopping_list[stuff[0]] = int(stuff[1])
    i += 1

for item in shopping_list:
    if shopping_list[item] >= 5:
        print(f"You have {shopping_list[item]} of {item}.")

