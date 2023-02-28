# Keep ONLY the Duplicates
'The intersection_update() method will keep only the items that are present in both sets'

# Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)   # will be: {'apple'}

''' The intersection() method will return a new set, that 
only contains the items that are present in both sets '''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates
'''The symmetric_difference_update() method will keep 
only the elements that are NOT present in both sets '''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)    # will be: {'google', 'banana', 'microsoft', 'cherry'}

'''The symmetric_difference() method will return a new set, that
contains only the elements that are NOT present in both sets.'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)   # will be: {'google', 'banana', 'microsoft', 'cherry'}



