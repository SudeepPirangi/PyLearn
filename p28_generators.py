"""
Exercises: Generators in Python
"""

import random

def stringify_result(any_func):
    """ Joins elements in a list as single string """
    def joiner(*args):
        """ Return joined list """
        items = any_func(*args)
        return " ".join(str(x) for x in items)
    return joiner

# 1. Create a generator that generates squares upto N
print("\n1. Generate square")

def squares_generator(limit):
    """ Generates square of the numbers till N """
    for num in range(limit):
        yield num**2

@stringify_result
def get_all_squares(*args):
    """ Returns a list of given number of squares"""
    squares = []
    for each in squares_generator(args[0]):
        squares.append(each)
    return squares

print(get_all_squares(10))

# 2. Create a generator that yields "n" random numbers between a "low" and a "high" numbers
print("\n2. Generate random numbers")

def generate_random_nums(n, low, high):
    """ Generates random numbers till from low to high """
    for _ in range(n):
        yield random.randint(low, high)

@stringify_result
def get_all_randoms(*args):
    """ Returns a list of given number of squares"""
    randoms = []
    n, low, high = args
    for each in generate_random_nums(n, low, high):
        randoms.append(each)
    return randoms

print(get_all_randoms(5, 200, 300))

# 3. Use the iter() function to convert the string "hello" to an iterator
print("\n3. Uses iter() and next()")

greeting = iter("hello")
print(next(greeting))
print(next(greeting))
print(next(greeting))

# 4. Using generators practically

# In regular approach we use a lot of memory to generate a big list
# but with "generator", we yield value only when needed that improves 
# space and time complexity

print("\n4. Generators in practice")

def regular_generator(n):
    """ A regular approach to generate 100 random numbers """
    nums = []
    counter = 0
    for _ in range(n):
        counter += 1
        nums.append(random.random())
    print(f"Regular generator counter - {counter}")
    return nums

def the_generator(n):
    """ A regular approach to generate 100 random numbers """
    counter = 0
    for _ in range(n):
        counter += 1
        yield random.random()
    print("THE generator counter - {counter}")

regulars = regular_generator(100)
for x in regulars[1:4]:
    print(x)

generated = the_generator(100)
print("\nGenerated randoms")
print(next(generated))
print(next(generated))
print(next(generated))

# t. Fibonacci with generator
print("5. Fibonacci")

def fib(limit):
    """ Generates fibonacci series efficiently """
    a, b = [0, 1]
    for _ in range(limit):
        yield a
        a, b = b, a + b

def generate_fibonacci(n):
    """ Calls for fibonacci series """
    for num in fib(n):
        print(num)

generate_fibonacci(10)
