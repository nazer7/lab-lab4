def squares(a: int, b: int):
    for i in range(a, b + 1):
        yield i * i
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
for x in squares(a, b):
    print(x)
