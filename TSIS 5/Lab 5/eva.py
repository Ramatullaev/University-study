import re

text = "this_is_a_test and_this_is_another one"
pattern = r"[a-z]+_[a-z]+"
matches = re.findall(pattern, text)

print(matches)
