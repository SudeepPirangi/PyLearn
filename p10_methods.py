from random import shuffle, randint

print("\nmin() and max()\n")
l1 = [10, 34, 1, 29, 36, 89, 53]
print("min(l1) -", min(l1))
print("max(l1) -", max(l1))

print("l1 - ", l1)
shuffle(l1)
print("shuffled l1 - ", l1)

print("randint(0, 100) - ", randint(0, 100))
print("randint(0, 100) - ", randint(0, 100))

print("\ninput()\n")
name = input("What is your name?\n")
print("Name is", name)