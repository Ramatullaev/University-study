#Slicing
'''You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.'''

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])      # will be: llo

#Slice From the Start
'''Get the characters from the start to position 5 (not included)'''
b = "Hello, World!"
print(b[:5])    # will be: Hello

#Slice To the End
'''Get the characters from position 2, and all the way to the end:'''
b = "Hello, World!"
print(b[2:])    # will be: llo< World!

#Negative Indexing
'''Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''

b = "Hello, World!"
print(b[-5:-2]     # will be: orl


