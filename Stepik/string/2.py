
ls = []
while True:
    a = int(input())
    if a == 0:
        break
    ls.append(a)
mxx = max(ls)
mnn = min(ls)
mx = ls.index(mxx)
mn = ls.index(mnn)
ls[mn],ls[mx] = mxx,mnn
print(*ls, sep = '\n')



