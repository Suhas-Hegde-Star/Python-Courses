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

