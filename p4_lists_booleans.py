# Lists
myList = ["abc", 123, 3.14, True]
print(myList)
print(myList[2])
print(myList[1:])
print(myList[::-1])

newList = [100, 12.4]
print(myList + newList)

# lists are mutable
myList[0] = "🐍"
print(myList)

newList.append('add')
print(newList)

popped = newList.pop()
print(popped, newList)

popped = myList.pop(1)
print(popped, myList)

newList = [12, 45, 1, 16]
newList.sort()
print(newList)

# list comprehension - comeback after 10. Methods.py
stringList = []
for char in 'Hello World':
    stringList.append(char)
print("stringList -", stringList)

newStringList = [char for char in "Hello Planet"]
print("newStringList - ", newStringList)

numList = [num ** 2 for num in range(1, 11)]
print("numList - ", numList)

evenSquares = [num ** 2 for num in range(1, 11) if num % 2 == 0]
print("evenSquares - ", evenSquares)

celcius = [0, 10, 20, 36, 40]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print("celcius - ", celcius)
print("fahrenheit - ", fahrenheit)

# Booleans
print(type(True), type(False))
print(3 > 7)
print(3 < 7)
print(1 == "1")