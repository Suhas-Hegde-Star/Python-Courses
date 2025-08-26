import sys
import a_a
import p2
import Exit

def tri_num(n):
    n = int(input("Till Which triangle number do you want? "))
    print([i * (i + 1) // 2 for i in range(1, n+1)])

def ask(wanted):
    while True:
        wanted = input("Enter what you want(Basic Words)\n")
        if wanted.lower() == Exit.sq:
            a_a.square(num= any, sq= any)
        elif wanted.lower() == Exit.e:
            print("Bye\nSee you next time")
            sys.exit
        elif wanted.lower() == Exit.sq:
            a_a.root(num= any, rot= any)
        elif wanted.lower() == Exit.ex:
            a_a.exponentation(num= any, ra= any, ans= any)
        elif wanted.lower() == Exit.cu:
            a_a.cube(num= any, cu= any)
        elif wanted.lower() == Exit.cr:
            a_a.cube_root(num= any, cr= any)
        elif wanted.lower() == Exit.rad:
            a_a.circle(rad= any, area= any)
        elif wanted.lower() == Exit.asq:
            a_a.square(side= any, area= any)
        elif wanted.lower() == Exit.arr:
            p2.rect(length= any, breadth= any, area= any)
        elif wanted.lower() == Exit.art:
            p2.tri(o= any, t=any, th= any, waa= any, area= any, s= any)
        elif wanted.lower() == Exit.add:
            p2.add(n1= any, n2= any)
        elif wanted.lower() == Exit.sub:
            p2.sub(n1= any, n2= any)
        elif wanted.lower() == Exit.mul:
            p2.mul(n1= any, n2= any)
        elif wanted.lower() == Exit.div:
            p2.div(n1= any, n2= any)
        elif wanted.lower() == Exit.tnu:
            tri_num(n= any)
        else:
            print("Input may be invalid\nOR\nWe do not have the data")