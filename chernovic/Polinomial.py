def checkPal(text):
    return text == text[:: -1]

pal = checkPal("oppo")
print(pal)

