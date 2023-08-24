import random


handgeste = ["Schere", "Stein", "Papier"]


def spielen():
    user = input("'sc' für Schere, 'st' für Stein, 'p' für Papier eingeben.")
    computer = random.choice(handgeste)

    if user == computer:
        return "Beide gewonnen"

    if gewonnen(user, computer):
        return "Du hast gewonnen"

    return "Du hast verloren"


def gewonnen(user, computer):
    if (user == "st" and computer == "Schere") or (user == "p" and computer == "Stein") or (user == "sc" and computer == "Papier"):
        return True


print(spielen())