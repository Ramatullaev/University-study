def mandela(n):
    for sf in range(0, n+1):
        if (sf % 3 == 0) and (sf % 4 == 0):
            yield sf 

for tokyo in mandela(int(input())):
    print(tokyo, end = ", ")