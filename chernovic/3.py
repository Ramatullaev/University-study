a = int(input())
b = int(input())
if a % 2 == 0:
    print(*range(a-1 , b-1 , -2))
else:
    print(*range(a , b-1 , -2))
    
    