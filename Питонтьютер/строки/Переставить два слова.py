text = input()
first = text[: text.find(" ")]
second = text[text.find(" ") + 1 :]
print(second , first)