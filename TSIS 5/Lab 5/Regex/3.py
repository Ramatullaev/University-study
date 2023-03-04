import re
file = open('/Users/snezhok/Desktop/PP2/TSIS 5/Lab 5/Regex/row.txt', 'r')

result = re.findall("[a-z]+_[a-z]+", file.read())
print(result)

