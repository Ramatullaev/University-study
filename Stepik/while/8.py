x = int(input())
cnt = 0
if x % 2 == 0:
    cnt += 1
while x != 0:
    if x % 2 == 0 and x != 0:
        cnt += 1
    x = int(input())
    
print(cnt)