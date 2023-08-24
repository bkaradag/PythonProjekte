import random


werfen = int(input("Wie viel werfen Sie?"))


for i in range(werfen):
    erste_Wurf = random.randint(1, 6)
    zweite_Wurf = random.randint(1, 6)

    print(f"Wurf 1 : {erste_Wurf}, Wurf 2: {zweite_Wurf}")