import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(700, 700)
turtle.shape("turtle")
turtle.speed(0.5)
turtle.pensize(7)
turtle.goto(0, 0)

p = turtle.Turtle()

def triangle():
    for i in range (3):
        p.fd(100)
        p.right(120)

p.penup()
p.goto(-50, -30)
p.pendown()
triangle()

p.penup()
p.goto(50, -80)
p. pendown()
p.rt(180)
triangle()

turtle.done()