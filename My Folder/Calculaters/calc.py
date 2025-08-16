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

def ask(wanted):
    while True:
        wanted = input("Enter what you want(Basic Words)")
        if wanted.lower == "square":
            square(num= any, sq= any)
        elif wanted.lower == "exit":
            print("Bye\nSee you next time")
            sys.exit
        elif wanted.lower == "square root":
            root(num= any, rot= any)
        else:
            print("Input may be invalid\nOR\nWe do not have the data")