#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#Check String
'''To check if a certain phrase or character
 is present in a string, we can use the keyword in.'''

 txt = "The best things in life are free!"
print("free" in txt)
# will be True
print()

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
# will be True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

