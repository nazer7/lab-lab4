def area(base: float, height: float) -> float:
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = area(base, height)
print(f"Expected Output: {area:.1f}")