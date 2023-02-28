#Modify Strings
a = "Hello, World!"
print(a.upper())    # will be: HELLO, WORLD!

a = "Hello, World!"
print(a.lower())      # will be: hello, world!

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" ()

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("Hello", "Jonh"))    # will be: Jonh, World!

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 