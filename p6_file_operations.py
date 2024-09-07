myfile = open('test.txt')

print(myfile.read())
print('read again', myfile.read())

myfile.seek(0)
print('read again n again\n', myfile.read())

myfile.seek(0)
print(myfile.readlines())

myfile.close()

# open file from other directory
# newFile = open("/users/xyz/abc.txt")

with open('test.txt') as myNewFile:
    contents = myNewFile.read()
print('with open()\n', contents)

# mode = 'r' is read only
# mode = 'w' is write only (will overwrite files or create new!)
# mode = 'a' is append only (will add on to files)
# mode = 'r+' is write and read
# mode = 'w+' is write and read (will overwrite files or create new!)

with open('test.txt', mode = 'a') as myNewFile:
    myNewFile.write('\nFifth line')

with open('test.txt') as myNewFile:
    contents = myNewFile.read()
print('with open(2)\n', contents)

with open('created.txt', mode = 'w') as f2:
    f2.write('I created this from Python')
with open('created.txt', mode = 'r') as f2:
    contents = f2.read()
print('with open(3)\n', contents)
