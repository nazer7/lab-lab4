def squaregen(N: int):
    for i in range(N + 1):
        yield i * i
N = 10
squares = squaregen(N)
print(f"Squares up to {N}: {[square for square in squares]}")