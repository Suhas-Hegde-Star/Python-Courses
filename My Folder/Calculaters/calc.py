import math
import sys

def square(num, sq):
    num = int(input("Enter the number"))
    sq = num ** 2
    print("Tne square of", num, "is", sq)

def root(num, rot):
    num = int(input("Enter the number"))
    rot = math.sqrt(num)
    print("Tne square of", num, "is", rot)

def cube(num, cu):
    num = int(input("Enter the number"))
    cu = num ** 3
    print("Tne square of", num, "is", cu)

def cube_root(num, cr):
    num = int(input("Enter the number"))
    cr = math.sqrt(math.sqrt(num))
    print("Tne square of", num, "is", cr)