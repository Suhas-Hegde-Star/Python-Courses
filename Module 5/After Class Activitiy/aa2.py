class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def circumference(self):
        pi = 22/7
        return 2 * pi * self.radius
    
qwerty = Circle(int(input("Enter radius of circle: ")))
print("Area of Circle:", qwerty.area())
print("Circumference of Circle:", qwerty.circumference())