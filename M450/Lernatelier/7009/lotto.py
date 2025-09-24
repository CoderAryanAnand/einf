import random

lotto_zahlen = set()

while len(lotto_zahlen) < 6:
    lotto_zahlen.add(random.randint(1,42))

print(f"Lottozahlen: {lotto_zahlen}")