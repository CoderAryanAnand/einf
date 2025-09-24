einkaufsliste = set()

while True:
    user_input = input("Zu einkaufen: ")
    if not user_input:
        break

    einkaufsliste.add(user_input)

for thing in einkaufsliste:
    print(thing)