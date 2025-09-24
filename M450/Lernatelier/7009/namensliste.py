
monate = {"Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"}

user_input = input("Gib einen Monat ein: ")
if user_input in monate:
    print(f"{user_input} ist ein Monat.")
else:
    print(f"{user_input} ist kein Monat.")