"""
Methods and Functions exercise
"""
import math
# Write a function that computes the volume of a Sphere given its radius.
# The volume of a sphere is given as (4/3) * pie * r ** 3
print("\n1. Volume of a Sphere")

def vol(r):
    """Calculates the volume of a sphere"""
    return (4/3) * (math.pi) * r ** 3

print("Volume of sphere with radius 2 is", vol(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)
print('\n2. Does number exist in the given range')
def ran_check(num, low, high):
    """Checks nums existence in range low to high"""
    return num in range(low, high + 1)

print(ran_check(5, 2, 7))

# Write a Python function that accepts a string and calulates the number of upper case letters and lower case letters.
# Sample String: "Hello Mr. Rogers, how are you this fine Tuesday?"
# Expected Output:
#     No. of Upper Case characters: 4
#     No. of Lower case characters: 33

print("\n3. Calculate the number of upper and lower case letters")

def up_low(s):
    """Calculater the number of upper and lower case letters"""
    upper, lower = (0, 0)
    for char in s:
        if char.isalpha():
            if char.isupper():
                upper += 1
            else:
                lower += 1
    return (upper, lower)

s = "Hello Mr. Rogers, how are you this fine Tuesday?"
upper, lower = up_low(s)
print("No. of Upper Case characters:", upper)
print("No. of Lower Case characters:", lower)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# sample List: [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
# unique List: [1, 2, 3, 4, 5]

print("\n4. Print uniques list")

def unique_list(lst):
    """Return unique list of items"""
    return list(set(lst))

print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

# Write a Python function to multiply all the numbers in a list.
# sample list: [1, 2, 3, -4]
# expected output: -24

print('\n5. Multiply all the elements in the list')

def multiply(nums):
    """Multiplies all the elements"""
    x = nums[0]
    for num in nums[1:]:
        x *= num
    return x

print(multiply([1, 2, 3, -4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.

print("\n6. Palindrome")

def palindrome1(s):
    """checks if a word or phrase is Palindrome"""
    word = s.replace(" ", "")
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            break
    if left >= right:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
def palindrome(s):
    """Uses built-in functions"""
    s = s.replace(" ", "")
    return s == s[::-1]

print("helleh -->", palindrome("helleh"))
print("madam -->", palindrome("madam"))
print("kayak -->", palindrome("kayak"))
print("sudeep -->", palindrome("sudeep"))
print("race car -->", palindrome("race car"))
print("nurses run -->", palindrome("nurses run"))

# Write a Python function to check whether a string is pangram or not
# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example: "The quick brown fox jumps over the lazy dog"

print("\n7. Pangram")

def is_pangram(sentence):
    """Check if the sentence is a pangram"""
    sentence = set(sentence.lower().replace(" ", ""))
    return len(sentence) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog"))
