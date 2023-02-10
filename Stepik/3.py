a = int(input())
b = [int(i) for i in input().split()]
sum = 0
for i in b:
    if i % 3 == 0 and i % 10 ==0:
        sum += 1
print(sum)