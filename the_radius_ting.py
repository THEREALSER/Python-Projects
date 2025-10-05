import math

r = float(input("Enter Radius: "))

area = math.pi * r * r
perimeter = 2 * math.pi * r

print(f"Area of the circle: {area:.2f}")
print(f"Perimeter of circle: {perimeter:.2f}")