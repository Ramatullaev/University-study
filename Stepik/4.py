a = int(input())
b = [int(i) for i in input().split()]
sum = 0
for i in b:
    if (int(i//10)*(i%10))>35:
        sum += i
print(sum)