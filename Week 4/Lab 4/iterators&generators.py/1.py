def squares_generator(N):
    for i in range(1, N+1):
        yield i**2
for square in squares_generator(int(input())):
    print(square)
    