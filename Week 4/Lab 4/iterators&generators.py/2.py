def even_gen(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

for luck in even_gen(int(input())):
    print(luck, end = ",")