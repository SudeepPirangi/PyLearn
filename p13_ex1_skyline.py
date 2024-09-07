"""
Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. 
The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

Remember, don't run the function, simply provide the definition.

To give an idea what the function would look like when tested:

myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'
"""

def myfunc(value):
    """Exercise function"""
    new_string = ""
    print(value)
    for index, char in enumerate(value):
        if index % 2 == 0:
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string

print(myfunc('Anthropomorphism'))
