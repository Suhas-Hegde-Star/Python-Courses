import math
import sys
import file1

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
            file1.exponentation(num= any, ra= any, ans= any)
        elif wanted.lower() == "cube":
            file1.cube(num= any, cu= any)
        elif wanted.lower() == "cube root":
            file1.cube_root(num= any, cr= any)
        elif wanted.lower() == "area of circle":
            file1.circle(rad= any, area= any)
        elif wanted.lower() == "area of square":
            file1.square(side= any, area= any)
        elif wanted.lower() == "area of rectangle":
            file2.rect(length= any, breadth= any, area= any)
        elif wanted.lower() == "area of triangle":
            file2.tri(o= any, t=any, th= any, waa= any, area= any, s= any)
        elif wanted.lower() == "addition" or "add":
            file2.add(n1= any, n2= any)
        elif wanted.lower() == "subtraction" or "subtract":
            file2.sub(n1= any, n2= any)
        elif wanted.lower() == "multiplication" or "multiply":
            file2.mul(n1= any, n2= any)
        elif wanted.lower() == "division" or "divide":
            file2.div(n1= any, n2= any)
        elif wanted.lower() == "triangle numbers":
            file3.tri_num(i= any, want= any, n= any)
        else:
            print("Input may be invalid\nOR\nWe do not have the data")

ask(wanted= any)