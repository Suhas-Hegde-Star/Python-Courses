import sys
import a_a
import p2
import nums
import Exit

def ask(wanted):
    while True:
        wanted = input("Enter what you want(Basic Words)\n")
        if wanted.lower() == "square":
            a_a.square(num= any, sq= any)
        elif wanted.lower() == Exit.exit:
            print("Bye\nSee you next time")
            sys.exit
        elif wanted.lower() == "square root":
            a_a.root(num= any, rot= any)
        elif wanted.lower() == "exponentation":
            a_a.exponentation(num= any, ra= any, ans= any)
        elif wanted.lower() == "cube":
            a_a.cube(num= any, cu= any)
        elif wanted.lower() == "cube root":
            a_a.cube_root(num= any, cr= any)
        elif wanted.lower() == "area of circle":
            a_a.circle(rad= any, area= any)
        elif wanted.lower() == "area of square":
            a_a.square(side= any, area= any)
        elif wanted.lower() == "area of rectangle":
            p2.rect(length= any, breadth= any, area= any)
        elif wanted.lower() == "area of triangle":
            p2.tri(o= any, t=any, th= any, waa= any, area= any, s= any)
        elif wanted.lower() == "addition" or "add":
            print("hi")
            p2.add(n1= any, n2= any)
        elif wanted.lower() == "subtraction" or "subtract":
            p2.sub(n1= any, n2= any)
        elif wanted.lower() == "multiplication" or "multiply":
            p2.mul(n1= any, n2= any)
        elif wanted.lower() == "division" or "divide":
            p2.div(n1= any, n2= any)
        elif wanted.lower() == "triangle numbers":
            nums.tri_num(i= any, want= any, n= any)
        else:
            print("Input may be invalid\nOR\nWe do not have the data")

ask(wanted= any)