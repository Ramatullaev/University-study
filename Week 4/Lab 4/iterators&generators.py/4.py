def squares(a, b):
    for i in range(a, b+1):
        i = i ** 2
        yield i

for sfo in squares(int(input()), int(input())):
    print(sfo, end = ", ")