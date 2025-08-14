import math

def circle(rad, area):
    rad = float(input("Enter the Radius of the Circle"))
    area = math.pow(rad, 2) * math.pi
    print("The area of the circle with", rad, "as the radius is", area)

def square(side, area):
    side = float(input("Enter the Length of the Square"))
    area = math.pow(side, 2)
    print("The area of the square with", side, "as the length is", area)

def rect(length, breadth, area):
    length = float(input("Enter the Length of the Rectangle"))
    breadth = float(input("Enter the Breadth of the Rectangle"))
    area = length * breadth
    print("The area of the square with", length, "length", "and", breadth, "breadth is", area)

def ask():
    while True:
        print("1. Area of Circle\n2. Area of a square\n. Area of a Rectangle\n4. Area of a Triangle")
        wanted = input("Enter the Suitable Number")
        if wanted == "1":
            circle(rad= any, area= any)
        elif wanted == "2":
            square(side= any, area= any)
        elif wanted == "3":
            rect(length= any, breadth= any, area= any)