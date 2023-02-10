n = int(input())
b = input()
a = []
cnt = 0
s = ''
cnt2 = 0
for x in b:
    s += x
    if x == ' ' or cnt2 == len(b) - 1:
        a.append(int(s))
        s = ''
    cnt2 += 1
for i in a:
    if i % 10 == 8:
        cnt+=1
print(cnt)
