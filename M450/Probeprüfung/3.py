"""
Mexico ist ein Würfelspiel und funktioniert für zwei Spieler wie folgt:

Beide Spieler haben zu Beginn 6 Leben.

In einer Runde würfelt zuerst der erste Spieler mit zwei Würfeln und zählt die Punkte zusammen. Danach würfelt der zweite Spieler mit zwei Würfeln und zählt seine Punkte zusammen. Der Spieler mit der niedrigeren Punktzahl hat die Runde verloren und verliert ein Leben. Wenn die Punktzahl gleich ist, verliert niemand ein Leben. Wer zuerst keine Leben mehr hat, verliert das Spiel.

Schreiben Sie ein Programm, dass zwei Spieler simuliert und gegeneinander spielen lässt. Geben Sie in jeder Runde die gewürfelten Punkte, die Leben der Spieler und wer gewonnen hat aus.

Geben Sie am Schluss des Spiels die Leben beider Spieler aus.

Hinweis:

Zufallszahlen können Sie folgendermassen erzeugen:

import random
x = random.randint(1, 10) # Zufallszahl zwischen 1 und 10 
"""

import random

player1_lives = 6
player2_lives = 6

while player1_lives > 0 and player2_lives > 0:
    player1_roll1 = random.randint(1, 6)
    player1_roll2 = random.randint(1, 6)
    player1_score = player1_roll1 + player1_roll2

    player2_roll1 = random.randint(1, 6)
    player2_roll2 = random.randint(1, 6)
    player2_score = player2_roll1 + player2_roll2

    print(f"Spieler 1 würfelt: {player1_roll1} + {player1_roll2} = {player1_score}")
    print(f"Spieler 2 würfelt: {player2_roll1} + {player2_roll2} = {player2_score}")

    if player1_score < player2_score:
        player1_lives -= 1
        print("Spieler 1 verliert die Runde und verliert ein Leben.")
    elif player2_score < player1_score:
        player2_lives -= 1
        print("Spieler 2 verliert die Runde und verliert ein Leben.")
    else:
        print("Unentschieden, niemand verliert ein Leben.")

    print(f"Leben von Spieler 1: {player1_lives}, Leben von Spieler 2: {player2_lives}\n")

if player1_lives <= 0:
    print("Spieler 2 gewinnt das Spiel!")
else:
    print("Spieler 1 gewinnt das Spiel!")
print(f"Endleben - Spieler 1: {player1_lives}, Spieler 2: {player2_lives}")