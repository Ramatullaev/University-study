def boston(sfo):
    while sfo >= 0:
        yield sfo
        sfo -= 1

for bos in boston(int(input())):
    print(bos)
