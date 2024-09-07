""" Level 2 exercise problems """

# Find 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) -> True
# has_33([1, 3, 1, 3]) -> False
# has_33([3, 1, 3]) -> False

def has_33(arr):
    """Question above"""
    for i in range(0, len(arr) - 1):
        # if arr[i] == 3 and arr[i + 1] == 3:
        if arr[i: i + 2] == [3, 3]:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllll000'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(word):
    """Question above"""
    new_word = ""
    for char in word:
        new_word += char * 3
    return new_word

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeeds 21, return 'BUST'
# blackjack(5, 6, 7) --> 18
# blackjack(9, 9, 9) --> 'BUST'
# blackjack(9, 9, 11) --> 19

def blackjack(a, b, c):
    """Question above"""
    three_sum = sum((a, b, c))
    if three_sum <= 21:
        return three_sum
    elif three_sum > 21 and 11 in [a, b, c]:
        return three_sum - 10
    else:
        return 'BUST'

print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

# SUMMER OF 69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    """Question above"""

    if 6 not in arr:
        return sum(arr)

    pos6 = arr.index(6)
    pos9 = arr.index(9)
    return sum(arr[:pos6]) + sum(arr[pos9 + 1:])

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
