''' The open() function returns a file object, which 
has a read()method for reading the content of the file:'''

f = open("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt", "r")
print(f.read())

print()
''' By default the read() method returns the whole text, 
but you can also specify how many characters you want to return:'''

f = open("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt", "r")
print(f.read(12))

print()
'''Read Lines
You can return one line by using the readline() method:'''

f = open("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt", "r")
print(f.readline())

print()
# by calling readline() two times, you can read the two first lines:

f = open("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt", "r")
print(f.readline())
print(f.readline())

print()
# By looping through the lines of the file, you can read the whole file, line by line:

f = open("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt", "r")
for x in f:
  print(x)


'''Close Files
It is a good practice to always close the file when you are done with it.'''

f = open("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt", "r")
print(f.readline())
f.close()

'''Note: You should always close your files, in some cases, due to 
buffering, changes made to a file may not show until you close the file.'''
