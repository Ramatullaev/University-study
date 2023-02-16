a = int(input())
b = int(input())
n = int(input())
price_a = n * a
price_b = n * b
y = 0
t = 0
if price_b >= 100:
    t = price_b % 100
    y = price_b // 100
    print(price_a + y, t)
else:
    print(price_a, price_b)
    