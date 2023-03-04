import re
file = open('/Users/snezhok/Desktop/PP2/TSIS 5/Lab 5/Regex/row.txt', 'r')

result = re.sub("[ ,.]",":", file.read())
print(result)

