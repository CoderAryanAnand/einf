import random

pl1 = 0
pl2 = 0
i = 0

while pl1 < 30 and pl2 < 30:
    i += 1
    pl1_turn = random.randint(1,6)
    print(f"Round {i}")

    pl1 += pl1_turn
    if pl1 > 29:
        # Positions
        print(f"Player 1 is at {pl1}")
        print(f"Player 2 is at {pl2}")
        break
    


    pl2_turn = random.randint(1,6)

    pl2 += pl2_turn

    # Positions
    print(f"Player 1 is at {pl1}")
    print(f"Player 2 is at {pl2}\n\n")


if pl1 >= 30:
    print("Player 1 won!")
else:
    print("Player 2 won!")
