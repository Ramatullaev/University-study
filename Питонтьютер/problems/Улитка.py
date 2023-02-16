h = int(input())
a = int(input())
b = int(input())
cnt = 0
cnt2 = 0
while h > 0:
    if cnt % 2 == 0:
        h = h - a
        cnt += 1
        cnt2+=1
    else:
        h = h + b
        cnt+=1
print(cnt2)
