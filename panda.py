a = [int(i) for i in input().split()]
x = int(input())

for i in range(len(a)):
    if x > a[i]:
        a.insert(i, x)
        break
else:
    a.append(x)

print(a.index(x) + 1)



