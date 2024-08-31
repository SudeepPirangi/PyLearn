print("\nif...elif...else\n")
# age = 25
# age = 17
age = 21
if age > 21:
    print("Welcome to the club!!")
elif age < 21:
    print("Get out!")
else:
    print("Hmmm..!")

print("\nfor loops\n")
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print("{} -> Even".format(num))
    else:
        print(f"{num} -> Odd")

dictionary = {
    "key1": 10,
    "key2": 20,
    "key3": 30
}
for item in dictionary:
    print(item)
for key, value in dictionary.items():
    print(f"{key}: {value}")
for value in dictionary.values():
    print(f"value is {value}")
for char in "Python":
    print("Char -", char)

print("\nbreak")
for num in numbers:
    if num == 4:
        break
    print(num)
print("\ncontinue")
for num in numbers:
    if num == 4:
        continue
    print(num)
print("\npass")
for num in numbers:
    # pass does nothing
    pass

print("\nWhile loop\n")
x = 0
while x < 4:
    print(f"x is {x}")
    x += 1
else:
    print("x is not less than 5")