import math
import sys

def rect(length, breadth, area):
    length = float(input("Enter the Length of the Rectangle "))
    breadth = float(input("Enter the Breadth of the Rectangle "))
    area = length * breadth
    print("The area of the square with", length, "length", "and", breadth, "breadth is", area)

def tri(o, t, th, waa, area, s):
    while True:
        waa = input("Is the tiangle equlateral(Type y or n) ")
        if waa.lower() == "y":
            o = float(input("Enter the length of the side "))
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
            print("Invalid Input. Try again ")

def add(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    print("The sum of", n1, "and", n2, "is", n2 + n1)

def sub(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    print("The difference of", n1, "and", n2, "is", n2 - n1)

def mul(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    print("The product of", n1, "and", n2, "is", n2 * n1)

def div(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    print( n1, "divided by", n2, "is", n2 / n1)

def tri_num(i, want, n):
    n = int(input("Till Which triangle number do you want? "))
    return [i * (i + 1) // 2 for i in range(1, n+1)]

def ask(wanted):
    while True:
        wanted = input("Enter what you want(Basic Words)\n")
        if wanted.lower() == "square":
            file1.square(num= any, sq= any)
        elif wanted.lower() == "exit":
            print("Bye\nSee you next time")
            sys.exit
        elif wanted.lower() == "square root":
            file1.root(num= any, rot= any)
        elif wanted.lower() == "exponentation":
            exponentation(num= any, ra= any, ans= any)
        elif wanted.lower() == "cube":
            cube(num= any, cu= any)
        elif wanted.lower() == "cube root":
            cube_root(num= any, cr= any)
        elif wanted.lower() == "area of circle":
            circle(rad= any, area= any)
        elif wanted.lower() == "area of square":
            square(side= any, area= any)
        elif wanted.lower() == "area of rectangle":
            rect(length= any, breadth= any, area= any)
        elif wanted.lower() == "area of triangle":
            tri(o= any, t=any, th= any, waa= any, area= any, s= any)
        elif wanted.lower() == "addition" or "add":
            add(n1= any, n2= any)
        elif wanted.lower() == "subtraction" or "subtract":
            sub(n1= any, n2= any)
        elif wanted.lower() == "multiplication" or "multiply":
            mul(n1= any, n2= any)
        elif wanted.lower() == "division" or "divide":
            div(n1= any, n2= any)
        elif wanted.lower() == "triangle numbers":
            tri_num(i= any, want= any, n= any)
        else:
            print("Input may be invalid\nOR\nWe do not have the data")

ask(wanted= any)