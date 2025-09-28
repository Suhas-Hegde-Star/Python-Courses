import time
import turtle
import sys

turtle.Screen().bgcolor("green")
turtle.Screen().setup(700, 700)
turtle.shape("turtle")
turtle.speed(0.5)

p = turtle.Turtle()

ns = int(input("Enter the number of sides"))
np = int(input("Enter side length"))
nn = 360 / ns

time.sleep(1)

for i in range(ns):
    p.fd(np)
    p.right(nn)

turtle.hideturtle()
turtle.done()

time.sleep(10)
sys.exit()