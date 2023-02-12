x = float(input())
y = int(input())
sum = 0
while x<y:
    x *= 1.1
    sum += 1
    if x > y:
        break
print(sum+1)