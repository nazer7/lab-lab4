def area(height: float, base1: float, base2: float) -> float:
    return 0.5 * (base1 + base2) * height
height = float(input("Enter height: "))
base1 = float(input("Enter base, first value: "))
base2 = float(input("Enter base, second value: "))

area = area(height, base1, base2)
print(f"Expected Output: {area:.1f}")
