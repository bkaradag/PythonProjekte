import json
import random
import string


# JSON Datei importen
with open("woerter.json", "r", encoding="utf-8") as f:
    woerter = json.load(f)


def get_woerter(woerter):
    w = random.choice(woerter)

    while "-" in w or " " in w:
        w = random.choise(woerter)
    return w.upper()


def spiel():
    w = get_woerter(woerter)
    w_buchstb = set(w)
    alphabet = set(string.ascii_uppercase)
    v_buchstb = set()  # verwendete Buchstaben

    while len(w_buchstb) > 0:
        print("Sie haben die folgenden verwendet: ", " ".join(v_buchstb))

        w_list = [buchstaben if buchstaben in v_buchstb else "-" for buchstaben in w]
        print("aktueller Wort: ", " ".join(w_list))

        user_buchstb = input("Buchstaben raten: ").upper()
        if user_buchstb in alphabet - v_buchstb:
            v_buchstb.add(user_buchstb)
            if user_buchstb in w_buchstb:
                w_buchstb.remove(user_buchstb)

        elif user_buchstb in v_buchstb:
            print("Sie haben schon verwendet.")

        else:
            print("ungültige Eingabe")


spiel()
