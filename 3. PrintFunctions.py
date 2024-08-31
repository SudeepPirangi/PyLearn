print("Simple")

world = "World"
print("Hello " + world)

# Using format function
print("{} using format".format("Printing"))
print("The {} {} {}".format("fox", "quick", "brown"))
print("The {1} {2} {0}".format("fox", "quick", "brown"))
print("The {q} {b} {f}".format(f="fox", q="quick", b="brown"))

# float formatting {value:width.precisionf}
pi = 22/7
print("Value of {pi}".format(pi=pi))
print("Value of {pi:5.4f}".format(pi=pi))
print("Value of {pi:1.2f}".format(pi=pi))

# Using f strings (requires Python 3.6 or higher)
greeting = "Hello"
name = "Sudeep"
print("Hello, my name is {}", format(name))
print(f"Hello, my name is {name}")
print(f"{greeting}, my name is {name}")