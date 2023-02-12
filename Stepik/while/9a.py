list1 = []
sum = 0
while True:
    x = int(input())
    if x == 0:
        break
    list1.append(x)
for i in range(1, len(list1)):# 
    if list1[i - 1] < list1[i]:
        sum+=1
print(sum) 
