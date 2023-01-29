#You can loop through the list items by using a for loop:
beta = ["apple", "banana", "cherry"]
for x in beta:
  print(x)

'''You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.'''
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])    # will be: apple
                        #          banana
                        #          cherry

# Use the len() function to determine the length of the list, 
# then start at 0 and loop your way through the list items by referring to their indexes.                      
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
 