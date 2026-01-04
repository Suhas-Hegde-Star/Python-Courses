import turtle

class shapes:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def draw(self):
        angle = 360 / self.sides
        for _ in range(self.sides):
            turtle.pendown()
            turtle.forward(self.length)
            turtle.right(angle)
            turtle.penup()
    
    def __add__(self, other):
        return shapes(self.sides + other.sides, self.length + other.length)

square = shapes(4, 50)
triangle = shapes(3, 50)
result = square + triangle
square.draw()
turtle.goto(-150, 0)
triangle.draw()
turtle.goto(150, 0)
result.draw()
turtle.done()
