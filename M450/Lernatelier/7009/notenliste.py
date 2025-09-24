user_input = "1"
noten = {}
while user_input != "0":
    user_input = input("Gib das Fach ein (0 zum beenden): ")
    if user_input == "0":
        break
    grade = int(input("Gib die Note ein: "))

    noten[user_input] = grade


for fach in noten:
    print(f"Im Fach {fach} hast du die Note {noten[fach]}.")

keys = [key for key, value in noten.items() if value == max(noten.values())]
print(f"Die beste Note war: {max(noten.values())}, im Fach {keys[0]}")