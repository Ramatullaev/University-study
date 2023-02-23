# Replacing text in a string using regular expressions
import re

text = "Hello, world! My name is Alice."

# Replace "Alice" with "Bob"
pattern = r"Alice"
replacement = "Bob"
new_text = re.sub(pattern, replacement, text)

print(new_text)
