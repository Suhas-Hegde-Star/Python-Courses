import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().title("MAZE")
turtle.speed("fastest")
turtle.pensize(7)
turtle.goto(0, 0)
turtle.hideturtle()

p = turtle.Turtle()
s = 0

while True:
    for i in range(4):
        p.fd(s + 0.5)
        p.lt(170)
        s -= 5
    s += 1