import math
def area_of_circle(radius):
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    return 2 * math.pi * radius

area= area_of_circle(7)
circum =circumference_of_circle(7)

print(f"Area of circle with radius 7: {area:.2f}")
print(f"Circumference of circle with radius 7: {circum:.2f}")