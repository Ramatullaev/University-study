a = int(input())
if a % 2 == 1:
    print(*range(1, a, 2), sep='')
else:
    b = a-1
    print(*range(1, b, 2), sep='')

