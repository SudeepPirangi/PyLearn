"""
Demonstrates map, filter and lambdas in Python
"""
print("\nMap function")

myList = [1, 2, 3, 4, 5]

def squares(n):
    """Returns square of a number"""
    return n ** 2

print(map(squares, myList))
for n in map(squares, myList):
    print(n)
print(list(map(squares, myList)))

print("\nFilter function")

def is_odd(n):
    """Checks if the given number is odd"""
    return n % 2 == 1

print(filter(is_odd, myList))
for n in filter(is_odd, myList):
    print(n)
print(list(filter(is_odd, myList)))

print("\nLambda functions")

print(list(map(lambda n: n ** 2, myList)))
print(list(filter(lambda n: n % 2 == 1, myList)))
