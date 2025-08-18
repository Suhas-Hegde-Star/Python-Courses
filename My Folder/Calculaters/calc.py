import math
import sys

def square(num, sq):
    num = int(input("Enter the number"))
    sq = num ** 2
    print("The square of", num, "is", sq)

def root(num, rot):
    num = int(input("Enter the number"))
    rot = math.sqrt(num)
    print("The square root of", num, "is", rot)

def cube(num, cu):
    num = int(input("Enter the number"))
    cu = num ** 3
    print("The cube of", num, "is", cu)

def cube_root(num, cr):
    num = int(input("Enter the number"))
    cr = math.sqrt(math.sqrt(num))
    print("The cube root of", num, "is", cr)

def exponentation(num, ra, ans):
    num = int(input("Enter the base"))
    ra = int(input("Enter the exponent"))
    ans = num ** ra
    print("The number", num, "raised to", ra, "is", ans)

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

def tri(o, t, th, waa, area, s):
    while True:
        waa = input("Is the tiangle equlateral(Type y or n)")
        if waa.lower() == "y":
            o = float(input("Enter the length of the side"))
            s = (o + o + o) / 2
            area = math.sqrt(s * (s - o) * (s - o) * (s - o))
            print("The area of the triangle is:", area)
        elif waa.lower() == "n":
            o = float(input("Enter the length of side a: "))
            t = float(input("Enter the length of side b: "))
            th = float(input("Enter the length of side c: "))
            s = (o + t + th) / 2
            area = math.sqrt(s * (s - o) * (s - t) * (s - th))
            print("The area of the triangle is:", area)
        else:
            print("Invalid Input. Try again")

def add(n1, n2):
    n1 = float(input("Enter the first number"))
    n2 = float(input("Enter the first number"))
    print("The sum of", n1, "and", n2, "is", n2 + n1)

def sub(n1, n2):
    n1 = float(input("Enter the first number"))
    n2 = float(input("Enter the first number"))
    print("The difference of", n1, "and", n2, "is", n2 - n1)

def add(n1, n2):
    n1 = float(input("Enter the first number"))
    n2 = float(input("Enter the first number"))
    print("The product of", n1, "and", n2, "is", n2 * n1)

def add(n1, n2):
    n1 = float(input("Enter the first number"))
    n2 = float(input("Enter the first number"))
    print( n1, "divided by", n2, "is", n2 / n1)

def ask(wanted):
    while True:
        wanted = input("Enter what you want(Basic Words)")
        if wanted.lower() == "square":
            square(num= any, sq= any)
        elif wanted.lower() == "exit":
            print("Bye\nSee you next time")
            sys.exit
        elif wanted.lower() == "square root":
            root(num= any, rot= any)
        elif wanted.lower() == "exponentation":
            exponentation(num= any, ra= any, ans= any)
        elif wanted.lower() == "cube":
            cube(num= any, cu= any)
        elif wanted.lower() == "cube root":
            cube_root(num= any, cr= any)
        elif wanted.lower() == "area of circle":
            circle(rad= any, area= any)
        elif wanted == "area of square":
            square(side= any, area= any)
        elif wanted == "area of rectangle":
            rect(length= any, breadth= any, area= any)
        elif wanted == "area of triangle":
            tri(o= any, t=any, th= any, waa= any, area= any, s= any)
        else:
            print("Input may be invalid\nOR\nWe do not have the data")