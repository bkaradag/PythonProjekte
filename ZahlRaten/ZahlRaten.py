import random


def raten(x):
    random_nummer = random.randint(1, x)
    versuch = 0

    while versuch != random_nummer:
        versuch = int(input(f"Ich habe mir eine  Zahl von 1 bis {x} ausgedacht:"))

        if versuch < random_nummer:
            print("zu klein!")
        elif versuch > random_nummer:
            print("zu groß!")

        print(versuch)

    print("Glückwunsch, du hast die Zahl gefunden.")


def computer_raten(x):
    klein = 1
    gross = x
    feedback = ""

    while feedback != "r":
        versuch = random.randint(klein, gross)
        feedback = input(f"ist {versuch} zu groß(g), zu klein(k), oder richtig(r)?")

        if feedback == "g":
            gross = versuch - 1
        elif feedback == "k":
            klein = versuch + 1

    print("Computer hat die Zahl gefunden.")


# guess(10)
computer_raten(20)
