import random


print("Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&.0123456789"

number = input("Wie viele Passwords möchten Sie generieren?")
number = int(number)

length = input("Wie lange muss sein?")
length = int(length)

print("Passwords:")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)