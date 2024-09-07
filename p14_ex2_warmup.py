""" Warmup exercise problems """

# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one of both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def is_even(num):
    """Checks if a given number is even"""
    return num % 2 == 0

def lesser_of_two_evens(a, b):
    """Complies with the conditions given in question above"""
    if (is_even(a) and is_even(b)):
        return min(a, b)
    else:
        return max(a, b)

print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
print(lesser_of_two_evens(7, 5))

# ANIMAL CRACKERS: Write a function takes a two-word string and retuns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(two_word):
    """Look at the question above"""
    word_list = two_word.lower().split()
    return word_list[0][0] == word_list[1][0] 

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20, 10) --> True
# makes_twenty(12, 8) --> True
# makes_twenty(2, 3) --> False

def makes_twenty(a, b):
    """question above"""
    return a == 20 or b == 20 or sum((a, b)) == 20

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
