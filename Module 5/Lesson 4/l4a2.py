import math as m

class location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display_location(self):
        return f"\n\n\n\nX Coordinate: {self.x}.\nY Coordinate: {self.y}.\n\n\n\n"

    def calculate_distance(self, other):
        return m.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __str__(self):
        return f"Location({self.x}, {self.y})"
    
    def __len__(self):
        return self.x + self.y

    def __add__(self, other):
        return location(self.x + other.x, self.y + other.y)

p1 = location(4, 4)
p2 = location(8, 8)
print(p1.display_location())
print(p2.display_location())
print("Distance between p1 and p2:", p1.calculate_distance(p2))
print("String representation of p1:", p1)
print("Length of p1 (x + y):", len(p1))
p3 = p1 + p2
print("New location after adding p1 and p2:", p3.display_location())