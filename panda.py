x = int(input())
min = 0
i = x
while i < x:
    if x % i == 0:
        min = i
        if min <= i:
            min = i
            
    i -= 1
print(min)

