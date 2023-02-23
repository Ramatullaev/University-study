'Sure, here are some examples of regular expressions in Python along with code snippets:'

# atching a phone number in a string
import re
phone_number = "My phone number is 555-1234. Call me anytime!"

# Match a phone number pattern
pattern = r"\d{3}-\d{4}"

# Search for the pattern in the string
match = re.search(pattern, phone_number)

if match:
    print("Phone number found:", match.group())
else:
    print("No phone number found.")

