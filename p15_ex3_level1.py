"""Level 1 exercise problems"""

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald("macdonald") --> MacDonald

def old_macdonald(name):
    """Question above"""
    mac = name[:3].capitalize()
    donald = name[3:].capitalize()
    return mac + donald

print(old_macdonald("macdonald"))

# MASTER YODA: Given a sentence, return a sentence with the workds reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(sentence):
    """Question above"""
    word_list = sentence.split()
    return " ".join(word_list[::-1])

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

def almost_there(num):
    """Question above"""
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
