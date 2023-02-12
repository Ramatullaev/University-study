def checkString(string):
    local_sum = 0
    for i in string:
        if i == "0":
            local_sum += 1
    return local_sum
cnt = 0
sum = 0
while True:
    a = input()
    if a == '0':
        break
    sum = checkString(a)
    if sum >= 2:
        cnt += 1

print(cnt)
