import math

def calculate_circle_area(radius):
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * radius * radius

def calculate_circle_circumference(radius):
    radius = float(input("Enter the radius of the circle: "))
    return 2 * math.pi * radius

def calculate_square_area(side):
    side = float(input("Enter the side length of the square: "))
    return side * side

def calculate_square_perimeter(side):
    side = float(input("Enter the side length of the square: "))
    return 4 * side

def calculate_rectangle_area(length, width):
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length * width

def calculate_rectangle_perimeter(length, width):
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return 2 * (length + width)

def calculate_triangle_area(base, height): 
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height

def calculate_triangle_perimeter(side1, side2, side3):
    side1 = float(input("Enter the length of side 1 of the triangle: "))
    side2 = float(input("Enter the length of side 2 of the triangle: "))
    side3 = float(input("Enter the length of side 3 of the triangle: "))
    return side1 + side2 + side3

def calculate_sphere_area(radius): 
    radius = float(input("Enter the radius of the sphere: "))
    return 4 * math.pi * radius * radius

def calculate_sphere_volume(radius): 
    radius = float(input("Enter the radius of the sphere: "))
    return (4/3) * math.pi * radius * radius * radius

def calculate_cube_area(side):
    side = float(input("Enter the side length of the cube: "))
    return 6 * side * side

def calculate_cube_volume(side):
    side = float(input("Enter the side length of the cube: "))
    return side * side * side