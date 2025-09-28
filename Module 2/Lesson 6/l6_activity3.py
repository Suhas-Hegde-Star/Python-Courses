import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(700, 700)
turtle.Screen().title("MAZE")
turtle.shape("turtle")
turtle.speed(0.5)
turtle.pensize(7)
turtle.goto(0, 0)
turtle.hideturtle()

p = turtle.Turtle()
s = 0

while True:
    for i in range(4):
        p.fd(s + 1)
        p.lt(91)
        s -= 5
    s += 1

turtle.done