""" Challenging exercise problem """

# SPY GAME: Write a function that takes in a list of integers and return True if it contains 007 in order
# spy_game([1, 2, 4, 0, 0, 7, 5]) --> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) --> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) --> False

def spy_game1(arr):
    """Question above"""
    if 0 not in arr:
        return False
    pos = arr.index(0)
    if 0 not in arr[pos + 1:]:
        return False
    pos = arr[pos + 1:].index(0)
    return 7 in arr[pos + 1:]

def spy_game(nums):
    """Better approach"""
    code = [0, 0, 7]
    for num in nums:
        if len(code) == 0:
            return True
        if num == code[0]:
            code.pop(0)
    return len(code) == 0

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to an including a given number
# By convention we'll treat 0 and 1 as not prime
# count_primes(100) --> 25

def count_primes1(num):
    """Question above"""
    if num < 2:
        return 0

    primes = [2, 3, 5, 7]
    for n in range(8, num + 1):
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
            primes.append(n)
    print(primes)
    return len(primes)

def count_primes(num):
    """Better solution"""
    primes = [2]
    x = 3

    while x <= num:
        # check if x is prime
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)

print(count_primes(100))
