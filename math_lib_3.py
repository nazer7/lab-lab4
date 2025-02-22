import math
def area(sides: int, length: float) -> float:
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
area = area(sides, length)
print(f"The area of the polygon is: {area:.6f}")
