word_list = []

for i in range(6):
    word = input(f"({i+1}) Gib mir ein Wort: ")
    word_list.append(word)


def kuerzestes(word_list):
    print(f"Das kürzeste Wort ist: '{sorted(word_list, key=len)[0]}' mit Länge {len(sorted(word_list, key=len)[0])}.")

kuerzestes(word_list)