x = int(input())
b = x
cnt = 0
while True:
    if x > b:
        cnt = cnt + 1
    b = x
    x = int(input())
    if x == 0:
        break
print(cnt)
