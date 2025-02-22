def gen(n: int):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter a number: "))
divisible_numbers = gen(n)
print(", ".join(map(str, divisible_numbers)))
