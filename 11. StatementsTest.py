# 1. Use for, .split() and if to create a statement that will print out words that start with 's'
st = "Print only the words that start with s in this sentence"
print(st)
for word in st.split():
    if (word[0] == 's'):
        print(word)

# 2. Use range() to print all the even numbers from 0 to 10
print("\nUse range() to print all the even numbers from 0 to 10")
for num in range(0, 11):
    if (num % 2) == 0:
        print(num)
for num in range(0, 11, 2):
    print(num)

# 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
print("\nUse a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3")
divBy3 = [x for x in range(1, 51) if x % 3 == 0]
print("divisible by 3 -", divBy3)

# 4. Go through the string below and if the length of a word is even print "even!"
st = "Print every word in this sentence that has an even number of letters"
print("\n" + st)
for word in st.split():
    if len(word) % 2 == 0:
        print("even!")
    else:
        print(word)

# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print
# "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
print("\nFizzBuzz Problem")
for num in range(1, 101):
    is3 = num % 3 == 0
    is5 = num % 5 == 0
    if is3 and is5:
        print("FizzBuzz")
    elif is3:
        print("Fizz")
    elif is5:
        print("Buzz")
    else:
        print(num)

# 6. Use list comprehension to create a list of the first letters of every word in the string below:
st = "Create a list of the first letters of every word in this string"
print("\n" + st)
letters = [x[0] for x in st.split()]
print("first letters list -", letters)