import math
def degree_to_radian(degree: float) -> float:
    return degree * (math.pi / 180)
degree = float(input("Enter degree: "))
radian = degree_to_radian(degree)
print(f"Output radian: {radian:.6f}")