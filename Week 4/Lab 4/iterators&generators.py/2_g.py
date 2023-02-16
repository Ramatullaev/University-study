def even_numbers(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = int(input("Enter a number: "))
even_nums = even_numbers(n)
print(','.join(str(i) for i in even_nums))
