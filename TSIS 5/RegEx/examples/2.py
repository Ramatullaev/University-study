# Extracting email addresses from a string
import re

text = "Contact me at alice@example.com or bob@example.com."

# Match an email address pattern
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Find all matches in the string
matches = re.findall(pattern, text)

if matches:
    print("Email addresses found:", matches)
else:
    print("No email addresses found.")
