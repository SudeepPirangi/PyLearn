"""
Demonstrates Exception Handling in Python
"""

# 1. Handle the exception thrown by the code below by using try and except blocks
# for i in ['a', 'b', 'c']:
#     print(i ** 2)

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Oh! I see a type error")
else:
    print("Looks like there is no error. Are you even a programmer!")
finally:
    print("I don't care what you want, I am always gonna run 😤\n")

# 2. Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to pring 'All Done.'
# x = 5
# y = 0
# z = x/y

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("So dumb! Cannot divide with zero.")
else:
    print("Looks like there is no error. Are you even a programmer!")
finally:
    print("Aren't you done yet! 🫨\n")

# 3. Write a function that asks for an integer and prints the square of it. use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    """Asks for an input and throws error if you don't obey"""
    while True:
        try:
            number = int(input("Yo! Enter a number -> "))
            print(f"The square of {number} is {number ** 2}")
        except ValueError:
            print("Nah!! You are wrong")
            continue
        else:
            print("Attaboy")
            break
        finally:
            print("What are you looking at?\n")

ask()
