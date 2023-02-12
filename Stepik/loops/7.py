b = int(input())
sum = 0
max = 0
if b == 0:
    sum += 1
if max < sum:
    max = sum

while b!=-1:
    if b == 1:
        sum = 0
    b = int(input())
    if b == 0:
        sum += 1
    if max < sum:
        max = sum
print(max)

