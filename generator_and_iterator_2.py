def evengen(n: int):
    for i in range(0, n + 1, 2):
        yield i
n = int(input("Enter a number: "))
even_numbers = evengen(n)
print(", ".join(map(str, even_numbers)))