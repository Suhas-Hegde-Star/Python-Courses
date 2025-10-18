import math

def circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    return 2 * math.pi * radius

deff = int(input("Enter the radius of the circle: "))
print(circumference(deff))