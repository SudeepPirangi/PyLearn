"""Demonstrates *args and **kwargs in Python"""

def get_percent(a, b):
    """Calculate 10% of given arguments sum"""
    return sum((a, b)) * 0.1

print(get_percent(10, 20))

# In the above scenario you cannot add unknown number of arguments
def get_10_percent(*args):
    """caluclate % of any number of args passed"""
    # converts args into a tuple
    print(args)
    return sum((args)) * 0.1

print(get_10_percent(10, 20, 30))
print(get_10_percent(10, 20, 30, 40))
print(get_10_percent(10, 20, 30, 40, 100))

# **kwargs or keyword args is used when you want to convert your arguments to a dictionary
def some_func(**kwargs):
    """looks for fruits and veggies"""
    print(kwargs)
    if "fruit" in kwargs:
        print('I love {}'.format(kwargs["fruit"]))
    else:
        print(f"I don't like {kwargs["veggie"]}")

some_func(fruit = "apple", veggie = "carrot")

# Another example of args and kwargs together
def other_function(*args, **kwargs):
    """Demonstrate args and kwargs together"""
    print(args)
    print(kwargs)
    print(f"My first arg is {args[0]}, key 'fruit' from kwargs is {kwargs["fruit"]}")

other_function(10, 20, 30, fruit = "apple", pet = "dog")
