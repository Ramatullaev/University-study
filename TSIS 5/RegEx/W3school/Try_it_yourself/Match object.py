'''Match Object
A Match Object is an object containing information about the search and the result.'''

# Do a search that will return a Match Object:
import re

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)                    # will be: <_sre.SRE_Match object; span=(5, 7), match='ai'>


'''The Match object has properties and methods used 
to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match'''

import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())                     # will be: (12, 17)


import re

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)



import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())                        # will be: Spain 

'Note: If there is no match, the value None will be returned, instead of the Match Object.'








