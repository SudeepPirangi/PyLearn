print("\nRange: range()")

print("\nrange(stop)")
for num in range(5):
    print(num)

print("\nrange(start, stop)")
for num in range(2, 5):
    print(num)

print("\nrange(start, stop, step)")
for num in range(0, 5, 2):
    print(num)

print("\nEnumerator: enumerate()\n")

python = "PYTHON"
for item in enumerate(python):
    print(item)
    (pos, value) = item # Tuple unpacking
    print(f"position {pos} -> value {value}")

print("\nZip: zip()\n")
l1 = [ 1, 2, 3, 4, 5, 6 ]
l2 = [ 'a', 'b', 'c' ]
l3 = [ 'x', 'y', 'z', 'r']
for item in zip(l1, l2, l3):
    print(item)

print('\nIn keyword: in - checks for existence\n')
print("x" in [1, 2, 3])
print(1 in [1, 2, 3])
print("x" in ["z", "x", "y"])
print("orl" in "Hello World")
someDict = { "key": "value" }
print("key" in someDict)
print("value" in someDict.values())