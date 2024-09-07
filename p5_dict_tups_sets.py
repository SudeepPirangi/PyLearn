# Dictionaries
dictnry = { 'k1': 100, 'k2': [200, 300], 'k3': {'k4': 4, 'k5': 5}}
print(dictnry)
print(dictnry['k2'])
print(dictnry['k3']['k5'])

dictnry['k1'] = 120
print(dictnry['k1'], type(dictnry))

keys = dictnry.keys()
print(keys, type(keys))
print(dictnry.values())

# Tuples are immutable
tup = (100, '200', False, False)
print(tup, type(tup))

print('tup False counts', tup.count(False))
print(tup.index(False))

# Sets holds only unique values
myset = set()
myset.add(1)
myset.add(2)
myset.add(2)
print('set', myset)
print(set([1,1,1,2,3,2,4,3,3]))
print(set('Mississippi'))