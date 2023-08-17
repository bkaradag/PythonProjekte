import requests
from bs4 import BeautifulSoup

url = "https://kur.doviz.com"
response = requests.get(url)
html_index = response.content
soup = BeautifulSoup(html_index, "html.parser")

waehrung = soup.find_all("span", {"class": "name"})
kurs = soup.find_all("span", {"class": "value"})

list_waehrung = []
list_kurs = []

for a in waehrung:
    list_waehrung.append(a.text)
for b in kurs:
    list_kurs.append((b.text).replace(",", "."))

print(list_waehrung)
print(list_kurs)

print("""***********

DÖVİZ UYGULAMASI

Auswahl:

1)Moment
2)EURO ---> TÜRKISCHE LIRA
3)TÜRKISCHE LIRA ---> EURO
4)DOLLAR ---> TÜRKISCHE LIRA
5)TÜRKISCHE LIRA ---> DOLLAR
6)PFUND ---> TÜRKISCHE LIRA
7)TÜRKISCHE LIRA ---> PFUND
8)EURO ---> DOLLAR
9)DOLLAR ---> EURO
0)EXIT

************""")

while True:
    auswahl = input("Auswahl:")
    if auswahl == "1":
        for i, j in zip(waehrung, kurs):
            print(i.text, ":", j.text)
    elif auswahl == "2":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge * float(list_kurs[2])
        print("{} Euro gleich {} Türkische Lira.".format(menge, ausgabe))
    elif auswahl == "3":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge / float(list_kurs[2])
        print("{} Türkische Lira gleich {} Euro.".format(menge, ausgabe))
    elif auswahl == "4":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge * float(list_kurs[1])
        print("{} Dollar gleich {} Türkische Lira.".format(menge, ausgabe))
    elif auswahl == "5":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge / float(list_kurs[1])
        print("{} Türkische Lira gleich {} Dollar.".format(menge, ausgabe))
    elif auswahl == "6":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge * float(list_kurs[3])
        print("{} Pfund gleich {} Türkische Lira.".format(menge, ausgabe))
    elif auswahl == "7":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge / float(list_kurs[3])
        print("{} Türkische Lira gleich {} Pfund.".format(menge, ausgabe))
    elif auswahl == "8":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge * float(list_kurs[2]) / float(list_kurs[1])
        print("{} Euro gleich {} Dollar.".format(menge, ausgabe))
    elif auswahl == "9":
        menge = float(input("Menge eingeben:"))
        ausgabe = menge * float(list_kurs[1]) / float(list_kurs[2])
        print("{} Dollar gleich {} Euro.".format(menge, ausgabe))
    elif auswahl == "0":
        print("Program wurde beendet.")
        break
    else:
        print("Auswahl nicht vorhanden.")