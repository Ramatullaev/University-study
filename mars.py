a = [int(i) for i in input().split()]
for i in range(0, len(a)):
    mn = a.index(min(a[:i+1]))
    mx = a.index(max(a[:i+1]))
a[mn] , a[mx] = a[mx], a[mn]
print(a)